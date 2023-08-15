#!/bin/bash

echo "🌊 Welcome to Sea++ setup! 🌊"

# Unzipping marine science subjects
echo "Unzipping marine science resources..."
marine_subjects=("oceanography" "ecology" "conservation_science")
for subject in "${marine_subjects[@]}"; do
    unzip "./$subject/$subject.zip" -d "./$subject/"
done

# Unzipping code resources
echo "Unzipping code resources..."
code_folders=("python/Basic Examples" "python/Statistical Tests" "python/cheatsheets" "python/Machine Learning Applications" "python/Image Detection in Marine Science" "julia" "tensorflow_models" "pytorch" "yolo")
for folder in "${code_folders[@]}"; do
    unzip "./Code 🖥️/$folder/$folder.zip" -d "./Code 🖥️/$folder/"
done

# Convert .md files to .pdf
echo "Converting .md files to .pdf..."

# Determine OS
OS="$(uname)"

# Install and use pandoc based on OS
if [ "$OS" == "Darwin" ]; then  # Mac OS
    # Check if pandoc is installed
    if ! command -v pandoc &> /dev/null
    then
        # Check if brew is installed
        if ! command -v brew &> /dev/null
        then
            echo "Brew is not installed. Installing brew..."
            /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
        fi
        echo "Pandoc is not installed. Installing pandoc using brew..."
        brew install pandoc
    fi
elif [ "$OS" == "Windows_NT" ]; then  # Windows OS
    # Check if pandoc is installed
    if ! command -v pandoc &> /dev/null
    then
        # Check if choco is installed
        if ! command -v choco &> /dev/null
        then
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

# Convert all .md files in the repository to .pdf
find . -name "*.md" -exec sh -c 'pandoc "${0}" -o "${0%.md}.pdf"' {} \;

echo "Conversion complete!"


echo "✨ Setup complete! Dive into Sea++! 🐠"
