from tensorflow import keras
from PIL import Image
import numpy as np

# Load the model
model_path = 'static/model/model10.h5'
model = keras.models.load_model(model_path, compile=False)

# Load and preprocess the test image
img = Image.open('path_to_test_image.jpg')  # Replace with a valid image path
img = img.resize((224, 224))
img_array = np.array(img) / 255.0
img_array = np.expand_dims(img_array, axis=0)

# Get prediction
prediction = model.predict(img_array)
print("Prediction:", prediction)
