##!/bin/bash
#
## Get the current operating system
#OS=$(uname)
#
## Define the file extension based on the operating system
#if [ "$OS" = "Darwin" ]; then
#    FILE="/Users/chakrapani/AIWeGuardAPIs/Reports/API_Testing_$(date +\%d-\%m-\%Y_\%H:\%M:\%S).html"
#elif [ "$OS" = "MINGW64_NT-10.0" ]; then
#    FILE="Report_$(date +\%d-\%m-\%Y_\%H-\%M-\%S).html"
#else
#    echo "Unsupported operating system: $OS"
#    exit 1
#fi
#
## Determine the Python command based on the operating system
#if [ "$OS" = "Darwin" ]; then
#    PY_CMD="python3"
#elif [ "$OS" = "MINGW64_NT-10.0" ]; then
#    PY_CMD="python"
#else
#    echo "Unsupported operating system: $OS"
#    exit 1
#fi
#
## Print the file name
#echo "$FILE"
#
## Capture the output of the Bash script
#$PY_CMD -m pytest --capture=sys --html="$FILE" --self-contained-html -v --show-progress
#
### Save the output to an HTML file
##echo "$OUTPUT" > "$FILE"
#
## Send the output as an email using the Python script
#python3 /Users/chakrapani/AIWeGuardAPIs/Utilities/send_emails.py "$FILE"