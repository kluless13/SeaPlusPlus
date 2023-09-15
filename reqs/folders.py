# for kluless' eyes only

import os

def create_directory(path):
    """Create a directory if it doesn't exist."""
    if not os.path.exists(path):
        os.makedirs(path)

# Create Marine Science Subjects folders and subfolders
marine_science_base = "Marine Science Subjects 🐠"
marine_science_subjects = ["oceanography", "ecology", "conservation_science"]

create_directory(marine_science_base)
for subject in marine_science_subjects:
    create_directory(os.path.join(marine_science_base, subject))

# Create Code base folder, its subfolders, and further nested subfolders
code_base = "Code 🖥️"
code_folders = ["Python", "Julia", "TensorFlow Models", "PyTorch", "YOLO"]
python_subfolders = ["Basic Examples", "Statistical Tests", "Machine Learning Applications", "Image Detection in Marine Science"]

create_directory(code_base)
for folder in code_folders:
    create_directory(os.path.join(code_base, folder))

# Create Python nested subfolders
for subfolder in python_subfolders:
    create_directory(os.path.join(code_base, "Python", subfolder))

print("Directories and subdirectories created successfully!")
