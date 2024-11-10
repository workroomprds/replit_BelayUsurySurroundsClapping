#!/bin/bash
# gets a response from Claude, times it, extracts the elapsed time only
{ time llm -t knockknockClaude ""; } 2>&1 | awk '/real/{print $2}'