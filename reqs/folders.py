# for kluless' eyes only

import os

def create_directory(path):
    """Create a directory if it doesn't exist."""
    if not os.path.exists(path):
        os.makedirs(path)

# Create main project structure
marine_science_dirs = {
    "marine_science": {
        "statistics": ["time_series", "spatial", "population"],
        "oceanography": ["currents", "waves", "tides"],
        "ecology": ["population_dynamics", "community_analysis"],
        "conservation": ["protected_areas", "species_monitoring"]
    }
}

# Create the directory structure
for main_dir, subdirs in marine_science_dirs.items():
    for category, components in subdirs.items():
        base_path = os.path.join(main_dir, category)
        create_directory(base_path)
        
        # Create component directories
        for component in components:
            component_path = os.path.join(base_path, component)
            create_directory(component_path)
            
            # Create standard subdirectories for each component
            create_directory(os.path.join(component_path, "data"))
            create_directory(os.path.join(component_path, "tests"))
            create_directory(os.path.join(component_path, "examples"))
            create_directory(os.path.join(component_path, "docs"))

# Create documentation directory
docs_dir = "docs"
create_directory(docs_dir)
for section in ["api", "examples", "tutorials", "contributing"]:
    create_directory(os.path.join(docs_dir, section))

print("✨ Directory structure created successfully! 🌊")
