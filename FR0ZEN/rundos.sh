#!/bin/bash

# Use the Unix-style file path
FILE_PATH="/mnt/c/Users/desny/OneDrive/Desktop/FR0ZEN/udpflood.py"

# Check if the file exists
if [ -f "$FILE_PATH" ]; then
    echo "Opening $FILE_PATH with Python..."
    clear
    python3 "$FILE_PATH"  # or use 'python' if Python 3 is the default on your system
else
    echo "File not found: $FILE_PATH"
fi
