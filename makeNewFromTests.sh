#!/bin/bash

# configuration
readonly MAX_ATTEMPTS=3
readonly TEST_FILE_PREFIX="./tests/test_"
readonly SOURCE_FILE_PREFIX="./src/"
#readonly STREAMING="--no-stream"  ## comment out to stream
readonly EXIT_SUCCESS=0
readonly EXIT_NO_PARAMETER=1
readonly EXIT_TEST_FILE_NOT_FOUND=2
readonly EXIT_TEST_FILE_SYNTAX_ERROR=3
readonly EXIT_TESTS_FAILED_AFTER_ITERATIONS=4

# Check if a parameter is provided
if [ $# -eq 0 ]; then
        echo "Error: No parameter provided."
        exit $EXIT_NO_PARAMETER
fi
# Get the module name from the parameter
module="$1"

# Check if the test file exists
test_file="$TEST_FILE_PREFIX$module"
if [ ! -f "$test_file" ]; then
        echo "Error: Test file $test_file does not exist."
        exit $EXIT_TEST_FILE_NOT_FOUND
fi

# check syntax of inbound test file
syntax_output=$(python -m py_compile "$test_file" 2>&1)
exit_code=$?
if [ -n "$exit_code" ] && [ "$exit_code" -ne 0 ]; then
        echo "Syntax error detected in $test_file: not sending for generation"
        echo "$syntax_output"
        exit $EXIT_TEST_FILE_SYNTAX_ERROR
fi
# At this point, the spoecified test file is worthwhile
#
# Make a new (empty) source file if needed
source_file="$SOURCE_FILE_PREFIX$module"
if [ ! -f "$source_file" ]; then
        echo "Source file $source_file does not exist. Creating an empty file."
        touch "$source_file"
fi

echo "Planning to change $source_file based on tests in $test_file"


# Extract tests from the test file
test_contents="$(< "$test_file")"

# Function to message on success
success_message() {
                coverage_output=$(coverage report -m "$source_file")
                ##echo $coverage_output
                coverage_percentage=$(echo "$coverage_output" | awk 'NR==5 {print $NF}')
                echo "Coverage for $source_file: $coverage_percentage" 
                echo "All tests in $test_file passed – code in $source_file is ready for inspection"
}

# Function to run tests and handle results
run_tests() {
        test_results="$(pytest --cov --quiet --tb=line "$test_file")"
        pytest_exit_code=$?
        echo "pytest_exit_code $pytest_exit_code"
        if [ $pytest_exit_code -eq 0 ]; then
                success_message
                return 0
        else
                echo "Tests failed."
                echo "$test_results"
                return 1
        fi
}
# Function to call the LLM
call_llm() { ## parameter 1 is new_conversation
        code_contents="$(< "$source_file")"
        if [ "$1" = true ]; then
            continue_flag=
            echo "Starting new conversation"
        else
            continue_flag="--continue"
            echo "Continuing conversation"
        fi
        echo "Attempting to generate new code with LLM"
        llm -t rewrite_python_to_pass_tests -p code "$code_contents" -p tests "$test_contents" -p test_results "$test_results"  "$continue_flag" $STREAMING > "$source_file"
        llm_exit_code=$?
        if [ $llm_exit_code -eq 0 ]; then
                echo "LLM generated a new $source_file. Passing over to tests in $test_file"
                return 0
        else
                echo "LLM failed to generate new code with error code $llm_exit_code – consider restoring source from change control"
                return 1
        fi
}

# Run initial tests
run_tests

# Set up "magic loop" to call LLM and run tests again
attempt=0
new_conversation=true

while [ $attempt -lt $MAX_ATTEMPTS ] && [ $pytest_exit_code -ne 0 ] ; do
	attempt=$((attempt+1))
        echo "Attempt $attempt"
        if [ $attempt -le $MAX_ATTEMPTS ]; then
                if call_llm "$new_conversation"; then
                    if run_tests; then
                        break
                    fi
                    new_conversation=false
                fi
        fi
 done

# commit changes if new code passes tests
if [ $attempt -ne 0 ] && [ $pytest_exit_code -eq 0 ]; then

        commitMessage="AI generated changes to $source_file to pass tests in $test_file"

        git add "$source_file" "$test_file" && git commit -m "$commitMessage"
        gitStatus=$?
        if [ $gitStatus -eq 0 ] ; then
                echo "Your tests, and the generated source, have been committed to the repository"
        else
                echo "While the generated code passes the tests, git stage or commit failed with error: $gitStatus . Perhaps the files match those already commited, so «git add» did nothing?"
        fi
fi

# closing messages
if [ $attempt -gt $MAX_ATTEMPTS ]; then
        echo "Maximum attempts reached ($MAX_ATTEMPTS)"
        if [ $pytest_exit_code -ne 0 ]; then
                echo "Exiting as generated code still does not pass tests"
                exit $EXIT_TESTS_FAILED_AFTER_ITERATIONS
        else
                success_message
                exit $EXIT_SUCCESS
        fi
fi