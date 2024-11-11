#!/bin/bash

# configuration
readonly MAX_ATTEMPTS=3
readonly TEST_FILE_PREFIX="./tests/test_"
readonly SOURCE_FILE_PREFIX="./src/"
readonly LLM_TEMPLATE=refactor_python_to_pass_tests
readonly LLM_MODEL="claude-3.5-sonnet" ## comment out to use default, or if template contains model.
#readonly STREAMING="--no-stream"  ## comment out to stream

# human-readable values
readonly TRUE=0
readonly FALSE=1
readonly EXIT_SUCCESS=0
readonly EXIT_NO_PARAMETER=1
readonly EXIT_TEST_FILE_NOT_FOUND=2
readonly EXIT_TEST_FILE_SYNTAX_ERROR=3
readonly EXIT_TESTS_FAILED_AFTER_ITERATIONS=4
readonly SOME_TESTS_FAILED_FIRST_TIME=5

numberOfArgs=$#
firstParameter=$1

## FUNCTIONS
# Check if a parameter is provided
checkParameters() {
        if [ $numberOfArgs -eq 0 ]; then
                echo "Error: No parameter provided."
                exit $EXIT_NO_PARAMETER
        fi
}

# Check test file existence and syntax
checkTestFile() {
        #check if the test file exists
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
}

# make an empty one if neccessary
fixSourceFile() {
        if [ ! -f "$source_file" ]; then
                echo "Source file $source_file does not exist. Creating an empty file."
                touch "$source_file"
        fi
}

# no point in TDDing if the tests pass...
exitIfTestsFailFirstTime() {
        echo "Tests currently fail. Refactoring not attempted. Exiting."
        exit $SOME_TESTS_FAILED_FIRST_TIME
}

# run tests / checks and handle results
checkCode() {
        test_results="$(pytest --cov --quiet --tb=line "$test_file")"
        pytest_exit_code=$?
        echo "pytest_exit_code $pytest_exit_code"
        if [ "$first_time_through" -eq $TRUE ]; then
                if [ $pytest_exit_code -ne 0 ]; then
                        exitIfTestsFailFirstTime
                else
                        echo "Tests pass. Continuing with refactoring"
                fi
        else
                if [ $pytest_exit_code -eq 0 ]; then
                        exit_triumphantly
                else
                        echo "Tests failed."
                        echo "$test_results"
                        return 1
                fi
        fi
}

# pass to AI via LLM tool
replaceSourceWithGeneratedCode() { ## parameter 1 is first_time_through
        # code_contents and test_results may be different each time
        code_contents="$(< "$source_file")"
        if [ "$first_time_through" -eq $TRUE ]; then
            continue_flag="" #intentionally not set
            echo "Starting new conversation"
            first_time_through=$FALSE
        else
            continue_flag="--continue"
            echo "Continuing conversation"
        fi
        
        echo "Attempting to generate new code with LLM"
        llm -t $LLM_TEMPLATE \
                $llmModelParameter \
                -p code "$code_contents" \
                -p tests "$test_contents" \
                -p test_results "$test_results" \
                -p input "" \
                $continue_flag \
                $STREAMING \
                "" \
                > "$source_file"
        llm_exit_code=$?
        if [ $llm_exit_code -eq 0 ]; then
                echo "LLM generated a new $source_file. Passing over to tests in $test_file"
                return 0
        else
                echo "LLM failed to generate new code with error code $llm_exit_code – consider restoring source from change control"
                return 1
        fi
}

# commit changes if new code passes tests
commit_changes () {
        commitMessage="AI refactored $source_file, while still to passing tests in $test_file"

        git add "$source_file" "$test_file" && git commit -m "$commitMessage"
        gitStatus=$?
        if [ "$gitStatus" -eq $TRUE ] ; then
                echo "Your tests, and the generated source, have been committed to the repository"
        else
                echo "While the generated code passes the tests, git stage or commit failed with error: $gitStatus . Perhaps the files match those already commited, so «git add» did nothing?"
        fi
}

# message on success
exit_triumphantly() {
                commit_changes
                coverage_output=$(coverage report -m "$source_file")
                ##echo $coverage_output
                coverage_percentage=$(echo "$coverage_output" | awk 'NR==5 {print $NF}')
                echo "Coverage for $source_file: $coverage_percentage" 
                echo "All tests in $test_file passed – code in $source_file is ready for inspection"
                exit $EXIT_SUCCESS
}



## MAIN starts here
echo "++EXPERIMENTAL REFACTORING TO PASS TESTS++"
# Do validation
checkParameters
# Get the module name from the parameter
module=$firstParameter
# Set file names
test_file="$TEST_FILE_PREFIX$module"
source_file="$SOURCE_FILE_PREFIX$module"
# Check existence and syntax of test file
checkTestFile
# Extract tests from the test file
test_contents="$(< "$test_file")"
# Make a new (empty) source file if needed
fixSourceFile
# Set model paramater for llm
if [ -n "$LLM_MODEL" ]; then
        llmModelParameter="-m $LLM_MODEL"
        else
        llmModelParameter=## intentionally not set
fi
# Run initial tests, and exit if they all work
first_time_through=$TRUE
checkCode

# Set up "magic loop" to call LLM and run tests again
attempt=0
echo "Planning to change $source_file based on tests in $test_file"

# Magic Loop here
while [ $attempt -lt $MAX_ATTEMPTS ] ; do # no need for  && [ $pytest_exit_code -ne 0 ]
	attempt=$((attempt+1))
        echo "Attempt $attempt"
        if [ $attempt -le $MAX_ATTEMPTS ]; then
                if replaceSourceWithGeneratedCode; then
                    checkCode ## which can EXIT_SUCCESSFULLY
                fi
        fi
 done

# persistenly trying hasn't helped: closing message
echo "Maximum attempts reached ($MAX_ATTEMPTS)"
echo "Exiting as generated code still does not pass tests"
exit $EXIT_TESTS_FAILED_AFTER_ITERATIONS
