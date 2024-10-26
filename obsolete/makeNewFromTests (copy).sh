#!/bin/bash

# Check if a parameter is provided
if [ $# -eq 0 ]; then
		echo "Error: No parameter provided."
		exit 1
fi

## check the files, stop if no tests, make an empty if no source

source_file="./src/$1"
if [ ! -f "$source_file" ]; then
		echo "Source file $source_file does not exist. Creating an empty file."
		touch "$source_file"
fi

test_file="./tests/test_$1"
if [ ! -f "$test_file" ]; then
		echo "Error: Test file $test_file does not exist."
		exit 1
fi

echo "planning to change $source_file based on tests in $test_file"

# Extract tests from the test file
test_contents="$(< $test_file)"

# Use the llm command directly
##llm -t rewrite_python_to_pass_tests -p code "$code_contents" -p tests "$test_contents" -p test_results "$test_results" '' > ./src/$1
#llm -t rewrite_python_to_pass_tests -p code "$(< ./src/$1)" -p tests "$(< ./tests/test_$1)" -p test_results "$(pytest ./tests/test_$1)" '' > ./src/$1
##llm -t rewrite_python_to_pass_tests -p code "$(cat ./src/$1)" -p tests "$(cat ./tests/test_$1)" -p test_results "$(pytest ./tests/test_$1)" '' > ./src/$1

max_attempts=2
attempt=1
success_message() {
	echo "All tests in $test_file passed – code in $source_file is ready for inspection"
}

run_tests() {
		test_results="$(pytest --quiet --tb=line $test_file)"
		pytest_exit_code=$?
		echo "pytest_exit_code $pytest_exit_code"
		if [ $pytest_exit_code -eq 0 ]; then
				success_message
		fi
}

run_tests

while [ $attempt -le $max_attempts ] && [ $pytest_exit_code -ne 0 ] ; do
		echo "Attempt $attempt"

		# Check if pytest passed all tests
		if [ $pytest_exit_code -eq 0 ]; then
				echo "All tests passed – do you ever see this message?"
				break
		else
				code_contents="$(< $source_file)"
				## echo "$code_contents"
				echo "Tests failed on attempt $attempt."
				echo "$test_results"
				if [ $attempt -le $max_attempts ]; then
						echo "Attempting to generate new code with LLM"
						llm -t rewrite_python_to_pass_tests -p code "$code_contents" -p tests "$test_contents" -p test_results "$test_results" '' > $source_file
						llm_exit_code=$?
						if [ $llm_exit_code -eq 0 ]; then
								echo "LLM generated a new $source_file. Passing over to tests in $test_file"
								run_tests
						else
								echo "LLM failed to generate new code with error code $llm_exit_code – restore source from change control"
						fi
				fi
		fi
		attempt=$((attempt+1))
done


if [ $attempt -gt $max_attempts ]; then
	echo "Maximum attempts reached"
	if [ $pytest_exit_code -ne 0 ]; then
			echo "Exiting as code does not pass tests"
			exit 1
	else
			success_message
	fi
fi