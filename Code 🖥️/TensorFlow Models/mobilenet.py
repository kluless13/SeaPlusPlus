# MobileNetV2 Model in TensorFlow
# pip install tensorflow

# Import necessary libraries
import tensorflow as tf
from tensorflow import keras
import numpy as np
import matplotlib.pyplot as plt

# Ensure TensorFlow version is 2.x
print(tf.__version__)

# Load the MobileNetV2 model with ImageNet weights
mobilenet_model = keras.applications.MobileNetV2(weights='imagenet', input_shape=(224, 224, 3))

# Load a sample image for prediction
sample_image = keras.preprocessing.image.load_img('path_to_your_image.jpg', target_size=(224, 224))
sample_image_array = keras.preprocessing.image.img_to_array(sample_image)
sample_image_array = np.expand_dims(sample_image_array, axis=0)
sample_image_array = keras.applications.mobilenet_v2.preprocess_input(sample_image_array)

# Predict using MobileNetV2
predictions = mobilenet_model.predict(sample_image_array)
decoded_predictions = keras.applications.mobilenet_v2.decode_predictions(predictions)

# Display the image and top 5 predictions
plt.imshow(sample_image)
plt.title(f"Top Prediction: {decoded_predictions[0][0][1]}")
plt.show()

print("Top 5 Predictions:")
for i, (imagenet_id, label, score) in enumerate(decoded_predictions[0]):
    print(f"{i + 1}: {label} ({score:.2f})")
