#!/bin/bash
# gets a response from GPT 4o, times it, extracts the elapsed time only
{ time llm -t knockknock -m 4o ""; } 2>&1 | awk '/real/{print $2}'