# Marine Science Machine Learning Models

This directory contains machine learning models and tools specifically designed for marine science applications.

## Modules

### Species Detection
- Marine species identification
- Population counting
- Behavior analysis
- Uses YOLO and other object detection models

### Habitat Classification
- Coral reef mapping
- Seagrass detection
- Habitat type classification
- Uses TensorFlow and PyTorch models

### Population Tracking
- Marine mammal tracking
- Fish school movement analysis
- Migration pattern detection
- Uses computer vision and tracking algorithms

## Model Organization

Each subdirectory contains:
- Pre-trained models
- Training scripts
- Data preprocessing tools
- Evaluation metrics
- Example notebooks

## Usage

See individual module documentation for specific usage instructions. General workflow:

```python
from marine_science.ml.species_detection import SpeciesDetector
from marine_science.ml.habitat_classification import HabitatClassifier
from marine_science.ml.population_tracking import PopulationTracker

# Initialize models
detector = SpeciesDetector(model_type='yolo')
classifier = HabitatClassifier(model_type='tensorflow')
tracker = PopulationTracker(tracking_method='deep_sort')

# Use models
species = detector.detect(image)
habitat = classifier.classify(image)
tracks = tracker.track(video)
```

## Data Requirements

- Species Detection: Labeled images/videos of marine species
- Habitat Classification: Satellite/underwater imagery
- Population Tracking: Video sequences of marine populations

## Model Training

Each module includes training scripts and instructions. Basic steps:
1. Prepare and preprocess data
2. Configure model parameters
3. Train model
4. Evaluate performance
5. Export model for inference

## Dependencies

See root `requirements.txt` for complete list. Key dependencies:
- TensorFlow
- PyTorch
- OpenCV
- NumPy
- Pandas 