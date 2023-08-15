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
code_folders=("python/Basic Examples" "python/Statistical Tests" "python/Machine Learning Applications" "python/Image Detection in Marine Science" "julia" "tensorflow_models" "pytorch" "yolo")
for folder in "${code_folders[@]}"; do
    unzip "./Code 🖥️/$folder/$folder.zip" -d "./Code 🖥️/$folder/"
done

echo "✨ Setup complete! Dive into Sea++! 🐠"
