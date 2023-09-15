#!/bin/bash

echo "🌊 Welcome to Sea++ setup! 🌊"

# Check if pandoc is installed
if ! command -v pandoc &> /dev/null; then
    echo "pandoc is not installed."
    # Detect the OS
    if [[ "$OSTYPE" == "linux-gnu"* ]]; then
        echo "You are using Linux. You can install pandoc using:"
        echo "sudo apt-get install pandoc"
    elif [[ "$OSTYPE" == "darwin"* ]]; then
        echo "You are using macOS. You can install pandoc using:"
        echo "brew install pandoc"
    else
        echo "Please install pandoc manually from https://pandoc.org/installing.html"
    fi
    exit 1
fi

# Function to unzip files in a directory
unzip_files_in_directory() {
    local dir="$1"
    echo "Unzipping files in $dir..."
    cd "$dir"
    if ls *.zip 1> /dev/null 2>&1; then
        unzip "*.zip"
        # Delete all zip files after unzipping
        rm *.zip
    else
        echo "Warning: No .zip files found in $dir"
    fi
    cd - > /dev/null
}

# Function to convert README.md to PDF
convert_md_to_pdf() {
    local dir="$1"
    echo "Converting README.md to PDF in $dir..."
    cd "$dir"
    if [ -f "README.md" ]; then
        pandoc README.md -o README.pdf --pdf-engine=xelatex
    else
        echo "Warning: README.md not found in $dir"
    fi
    cd - > /dev/null
}

# Unzipping marine science resources
unzip_files_in_directory "Marine Science Subjects 🐠/oceanography"
unzip_files_in_directory "Marine Science Subjects 🐠/ecology"
unzip_files_in_directory "Marine Science Subjects 🐠/conservation_science"

# Unzipping code resources in Python/cheatsheets
unzip_files_in_directory "Code 🖥️/Python/cheatsheets"

# Convert README.md to PDF
convert_md_to_pdf "Marine Science Subjects 🐠/oceanography"
convert_md_to_pdf "Marine Science Subjects 🐠/ecology"
convert_md_to_pdf "Marine Science Subjects 🐠/conservation_science"
convert_md_to_pdf "Code 🖥️/Python/cheatsheets"
convert_md_to_pdf "Code 🖥️/Python/Basic Examples"
convert_md_to_pdf "Code 🖥️/Python/Image Detection in Marine Science"
convert_md_to_pdf "Code 🖥️/Python/Machine Learning Applications"
convert_md_to_pdf "Code 🖥️/Python/Statistical Tests"
convert_md_to_pdf "Code 🖥️/PyTorch"
convert_md_to_pdf "Code 🖥️/TensorFlow Models"
convert_md_to_pdf "Code 🖥️/YOLO"
convert_md_to_pdf "Code 🖥️/Julia"

echo "✨ Setup complete! Dive into Sea++! 🐠"