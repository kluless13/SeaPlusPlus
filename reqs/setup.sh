#!/bin/bash

echo "🌊 Welcome to Sea++ setup! 🌊"

# Unzipping marine science subjects
echo "Unzipping marine science resources..."
marine_subjects=("oceanography" "ecology" "conservation_science")
for subject in "${marine_subjects[@]}"; do
    if ls "./$subject/"*.zip 1> /dev/null 2>&1; then
        unzip "./$subject/*.zip" -d "./$subject/"
    else
        echo "Warning: No .zip files found in ./$subject/"
    fi
done


# Unzipping code resources in Python/cheatsheets
echo "Unzipping Python cheatsheets..."
if [ -f "./Code 🖥️/Python/cheatsheets/cheatsheets.zip" ]; then
    unzip "./Code 🖥️/Python/cheatsheets/cheatsheets.zip" -d "./Code 🖥️/Python/cheatsheets/"
else
    echo "Warning: cheatsheets.zip not found in ./Code 🖥️/Python/cheatsheets/"
fi

# Convert .md files to .pdf
echo "Converting .md files to .pdf..."

# Determine OS
OS="$(uname)"

# Install and use pandoc based on OS
if [ "$OS" == "Darwin" ]; then  # Mac OS
    # Check if pandoc is installed
    if ! command -v pandoc &> /dev/null; then
        # Check if brew is installed
        if ! command -v brew &> /dev/null; then
            echo "Brew is not installed. Installing brew..."
            /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
        fi
        echo "Pandoc is not installed. Installing pandoc using brew..."
        brew install pandoc
    fi
elif [ "$OS" == "Windows_NT" ]; then  # Windows OS
    # Check if pandoc is installed
    if ! command -v pandoc &> /dev/null; then
        # Check if choco is installed
        if ! command -v choco &> /dev/null; then
            echo "Chocolatey is not installed. Please install Chocolatey from https://chocolatey.org/install"
            exit 1
        fi
        echo "Pandoc is not installed. Installing pandoc using choco..."
        choco install pandoc
    fi
else
    echo "Unsupported OS. Please manually install pandoc."
    exit 1
fi

# Convert all .md files in the repository to .pdf using xelatex for better Unicode support
find . -name "*.md" -exec sh -c 'pandoc "${0}" --pdf-engine=xelatex -o "${0%.md}.pdf"' {} \;

echo "Conversion complete!"
echo "✨ Setup complete! Dive into Sea++! 🐠"

