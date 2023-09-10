#!/usr/bin/env bash/bin/sh
#

#FILE="Report_$(date +%d-%m-%Y_%H:%M:%S).html"
#echo "$FILE"
#python3 -m pytest --capture=sys --html="$FILE"

#!/usr/bin/env bash

# Get the current operating system
OS=$(uname)

# Define the file extension based on the operating system
if [ "$OS" = "Darwin" ]; then
    # shellcheck disable=SC1001
    FILE="Report_$(date +\%d-\%m-\%Y_\%H:\%M:\%S).html"
elif [ "$OS" = "MINGW64_NT-10.0" ]; then
    # shellcheck disable=SC1001
    FILE="Report_$(date +\%d-\%m-\%Y_\%H-\%M-\%S).html"
else
    echo "Unsupported operating system: $OS"
    exit 1
fi

# Determine the Python command based on the operating system
if [ "$OS" = "Darwin" ]; then
    PY_CMD="python3"
elif [ "$OS" = "MINGW64_NT-10.0" ]; then
    PY_CMD="python"
else
    echo "Unsupported operating system: $OS"
    exit 1
fi

# Print the file name
echo "$FILE"

# Run pytest for tests with the 'order' marker
$PY_CMD -m pytest --capture=sys --html="$FILE" --self-contained-html -v --show-progress

## Run pytest for tests with the 'order' marker
#$PY_CMD -m pytest -k "order" --capture=sys --html="$FILE" --self-contained-html -v --show-progress

## Run pytest for tests without the 'order' marker
#$PY_CMD -m pytest -k "not order" --capture=sys --html="$FILE" --self-contained-html -v --show-progress


## Mac
#echo "$FILE"
#python3 -m pytest --capture=sys --html="$FILE" --self-contained-html -v --show-progress

# # Windows
#echo "$FILE"
#python -m pytest --capture=sys --html="$FILE" --self-contained-html -v --show-progress
