#!/bin/bash

## !! Check what's going on with swecond time through – I think it\s missing a "". USe llm logs -n 15 to look at last 15 logs

# configuration
readonly MAX_ATTEMPTS=1
readonly TEST_FILE_PREFIX="./tests/test_"
readonly SOURCE_FILE_PREFIX="./src/"
readonly LLM_TEMPLATE=rewrite_python_to_pass_tests_new_parms
readonly LLM_MODEL="claude-3.5-sonnet" ## comment out to use default, or if template contains model. Keep the -m at start
#readonly STREAMING="--no-stream"  ## comment out to stream

# Readable values
readonly TRUE=$(true)
readonly FALSE=$(false)
readonly EXIT_SUCCESS=0
readonly EXIT_NO_PARAMETER=1
readonly EXIT_TEST_FILE_NOT_FOUND=2
readonly EXIT_TEST_FILE_SYNTAX_ERROR=3
readonly EXIT_TESTS_FAILED_AFTER_ITERATIONS=4
readonly ALL_TESTS_PASSED_FIRST_TIME=5
readonly EXIT_NO_CODE_PASSED_TO_LLM=6
readonly EXIT_NO_TESTS_PASSED_TO_LLM=7
readonly EXIT_NO_TEST_RESULTS_PASSED_TO_LLM=8


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
        echo $test_file
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
exitIfTestsPassFirstTime() {
        if [ $pytest_exit_code -eq 0 ]; then
                echo "Tests already pass. No code generated. Exiting."
                exit $ALL_TESTS_PASSED_FIRST_TIME
        fi
}

# message on success
success_message() {
                coverage_output=$(coverage report -m "$source_file")
                ##echo $coverage_output
                coverage_percentage=$(echo "$coverage_output" | awk 'NR==5 {print $NF}')
                echo "Coverage for $source_file: $coverage_percentage" 
                echo "All tests in $test_file passed – code in $source_file is ready for inspection"
}

# run tests / checks and handle results
checkCode() {
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

# pass to AI via LLM tool
replaceSourceWithGeneratedCode() { ## parameter 1 is new_conversation
        # code_contents and test_results may be different each time
        echo "source_file $source_file"
        code_contents="$(< $source_file)"

        # validate and set paramaters for LLM
        if $new_conversation; then
            continue_flag= #intentionally not set
            echo "Starting new conversation"
        else
            continue_flag="--continue"
            echo "Continuing conversation"
        fi

        if [ -n "$code_contents" ]; then
                : # do nothing
                #llmCodeContentParameter=(-p "code" "$code_contents")
        else
                #llmCodeContentParameter=(-p "code" "$code_contents")
                echo "no code content passed to LLM tool"
                #exit $EXIT_NO_CODE_PASSED_TO_LLM
        fi

        if [ -n "$test_contents" ]; then
                :
                #llmTestContentParameter=(-p "tests" $test_contents")
        else
                echo "no test content passed to LLM tool"
                exit $EXIT_NO_TESTS_PASSED_TO_LLM
        fi

        #echo ${llmTestContentParameter[*]}
        #exit

        if [ -n "$test_results" ]; then
                :
                #llmTestResultContentParameter=(-p "test_results" "$test_results")
        else
                echo "no test_results content passed to LLM tool"
                exit $EXIT_NO_TEST_RESULTS_PASSED_TO_LLM
        fi

        echo "Attempting to generate new code with LLM"
       # echo "parameters: -t "$LLM_TEMPLATE" "$llmModelParameter"  ${llmCodeContentParameter[@]} ${llmTestContentParameter[@]} ${llmTestResultContentParameter[@]} $continue_flag $STREAMING"
        #exit

        echo llm -t $LLM_TEMPLATE \
                $llmModelParameter \
                -p code "$code_contents" \
                -p tests "$test_contents" \
                -p test_results "$test_results" \
                -p input "" \
                #"" > "$source_file"
                #$continue_flag \
                #$STREAMING \
                exit
        llm_exit_code=$?
        if [ $llm_exit_code -eq 0 ]; then
                echo "LLM generated a new $source_file. Passing over to tests in $test_file"
                return 0
        else
                echo "LLM failed to generate new code with error code $llm_exit_code – consider restoring source from change control"
                return 1
        fi
}

## MAIN starts here
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
checkCode
exitIfTestsPassFirstTime

# Set up "magic loop" to call LLM and run tests again
attempt=0
new_conversation=$TRUE
echo "Planning to change $source_file based on tests in $test_file"

while [ $attempt -lt $MAX_ATTEMPTS ] && [ $pytest_exit_code -ne 0 ] ; do
	attempt=$((attempt+1))
        echo "Attempt $attempt"
        if [ $attempt -le $MAX_ATTEMPTS ]; then
                if replaceSourceWithGeneratedCode; then
                    if checkCode; then
                        break # drop out lof the loop if tests pass
                    fi
                    new_conversation=$FALSE
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