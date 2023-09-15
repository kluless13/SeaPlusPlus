#!/bin/bash

echo "🌊 Welcome to Sea++ setup! 🌊"

# Function to unzip files in a directory
unzip_files_in_directory() {
    local dir="$1"
    echo "Unzipping files in $dir..."
    cd "$dir"
    if ls *.zip 1> /dev/null 2>&1; then
        unzip "*.zip"
    else
        echo "Warning: No .zip files found in $dir"
    fi
    cd - > /dev/null
}

# Unzipping marine science resources
unzip_files_in_directory "oceanography"
unzip_files_in_directory "ecology"
unzip_files_in_directory "conservation_science"

# Unzipping code resources in Python/cheatsheets
unzip_files_in_directory "Code 🖥️/Python/cheatsheets"

echo "✨ Setup complete! Dive into Sea++! 🐠"
