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
    FILE="Report_$(date +\%d-\%m-\%Y_\%H:\%M:\%S).html"
elif [ "$OS" = "MINGW64_NT-10.0" ]; then
    FILE="Report_$(date +\%d-\%m-\%Y_\%H-\%M-\%S).html"
else
    echo "Unsupported operating system: $OS"
    exit 1
fi

# Mac
echo "$FILE"
python3 -m pytest --capture=sys --html="$FILE" --self-contained-html -v

# # Windows
#echo "$FILE"
#python -m pytest --capture=sys --html="$FILE" --self-contained-html -v