#!/bin/bash

echo "🌊 Welcome to Sea++ setup! 🌊"

# Unzipping marine science subjects
echo "Unzipping marine science resources..."
for subject in oceanography ecology conservation_science; do
    unzip $subject.zip -d $subject/
done

# Unzipping code resources
echo "Unzipping code resources..."
for code in python julia tensorflow_models pytorch yolo; do
    unzip $code/documents.zip -d $code/
done

# Creating code templates directories
for code in python julia tensorflow_models pytorch yolo; do
    mkdir -p $code/code_templates
done

echo "✨ Setup complete! Dive into Sea++! 🐠"