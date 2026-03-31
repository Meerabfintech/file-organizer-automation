#!/bin/bash
# Bash wrapper for file organizer script
# Google IT Automation Course Project

echo "==================================="
echo "📂 FILE ORGANIZER - Bash Launcher"
echo "==================================="

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo " Python 3 is not installed. Please install Python 3 first."
    exit 1
fi

# Run the Python script
python3 file_organizer.py

echo ""
echo "Done!"
