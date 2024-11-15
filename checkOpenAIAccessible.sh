#!/bin/bash
# gets a response from GPT 4o, times it, extracts the elapsed time only
{ time llm -t knockknock -m gpt-4o-mini ""; } 2>&1 | awk '/real/{print $2}'