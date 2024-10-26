#!/bin/bash
# Check if a parameter is provided
if [ $# -eq 0 ]; then
        echo "Error: No parameter provided."
        exit 1
fi
# Get the module name from the parameter
module="$1"
# Check if the source file exists
source_file="./src/$module"
if [ ! -f "$source_file" ]; then
        echo "Source file $source_file does not exist. Creating an empty file."
        touch "$source_file"
fi
# Check if the test file exists
test_file="./tests/test_$module"
if [ ! -f "$test_file" ]; then
        echo "Error: Test file $test_file does not exist."
        exit 1
fi

# check syntax of inbound test file
syntax_output=$(python -m py_compile "$test_file" 2>&1)
exit_code=$?
if [ -n "$exit_code" ] && [ "$exit_code" -ne 0 ]; then
        echo "Syntax error detected in $file: not sending for generation"
        echo "$syntax_output"
        exit 1
fi

echo "Planning to change $source_file based on tests in $test_file"


# Extract tests from the test file
test_contents="$(< $test_file)"

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
        test_results="$(pytest --cov --quiet --tb=line $test_file)"
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
        code_contents="$(< $source_file)"
        if [ "$1" = true ]; then
            continue_flag=""
        else
            continue_flag="-c"
        fi
        echo "Attempting to generate new code with LLM"
        llm -t rewrite_python_to_pass_tests "$continue_flag" --no-stream -p code  "$code_contents" -p tests "$test_contents" -p test_results "$test_results" '' > $source_file
        llm_exit_code=$?
        if [ $llm_exit_code -eq 0 ]; then
                echo "LLM generated a new $source_file. Passing over to tests in $test_file"
                return 0
        else
                echo "LLM failed to generate new code with error code $llm_exit_code – restore source from change control"
                return 1
        fi
}

# Run initial tests
run_tests

# Set up "magic loop" to call LLM and run tests again
max_attempts=3
attempt=0
while [ $attempt -lt $max_attempts ] && [ $pytest_exit_code -ne 0 ] ; do
	      attempt=$((attempt+1))
        echo "Attempt $attempt"
        if [ $attempt -le $max_attempts ]; then
                call_llm
                if [ $? -eq 0 ]; then
                        run_tests
                        if [ $? -eq 0 ]; then
                                break
                        fi
                fi
        fi
 done

# commit changes if new code passes tests
if [ $attempt -ne 0 ] && [ $pytest_exit_code -eq 0 ]; then
		commitMessage="AI generated changes to $source_file to pass tests in $test_file"
		git add $source_file $test_file && git commit -m "$commitMessage"
		if [ $? -eq 0 ]; then
			echo "Your tests, and the generated source, have been committed to the repository"
		else
			echo "git commit failed with error $?"
		fi

fi

# closing messages
if [ $attempt -gt $max_attempts ]; then
        echo "Maximum attempts reached ($max_attempts)"
        if [ $pytest_exit_code -ne 0 ]; then
                echo "Exiting as code does not pass tests"
                exit 1
        else
 
                success_message

        fi
fi