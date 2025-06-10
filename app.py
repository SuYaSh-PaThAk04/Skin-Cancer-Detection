from flask import Flask, request, jsonify, render_template, url_for
from tensorflow import keras
from PIL import Image
import numpy as np
import os

app = Flask(__name__)

model_path = os.path.join('static', 'model', 'model10.h5')
model = keras.models.load_model(model_path, compile=False)


disease_classes = {
    0: {'name': 'Actinic keratoses and intraepithelial carcinoma (Bowen’s disease)', 'image_folder': 'AKIEC'},
    1: {'name': 'Basal cell carcinoma', 'image_folder': 'BCC'},
    2: {'name': 'Benign keratosis-like lesions', 'image_folder': 'BKL'},
    3: {'name': 'Dermatofibroma', 'image_folder': 'DF'},
    4: {'name': 'Melanoma', 'image_folder': 'Melanoma'},
    5: {'name': 'Melanocytic nevi', 'image_folder': 'Nevus'},
    6: {'name': 'Vascular lesions (angiomas, angiokeratoma6s, etc.)', 'image_folder': 'Vascular'}
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        if 'image' not in request.files:
            return jsonify({"error": "No image uploaded"}), 400

        image_file = request.files['image']

        try:
            img = Image.open(image_file)
        except Exception as e:
            return jsonify({"error": f"Invalid image format: {str(e)}"}), 400

        img = img.convert('L')  

        img = img.resize((28, 28))

        img_array = np.array(img) / 255.0 

        img_array = np.expand_dims(img_array, axis=0) 
        img_array = np.expand_dims(img_array, axis=-1) 
        prediction = model.predict(img_array)

        predicted_class = np.argmax(prediction, axis=1)[0]
        predicted_probabilities = prediction[0]

        predicted_disease_info = disease_classes.get(predicted_class, {"name": "Unknown Disease", "image_folder": ""})
        predicted_disease = predicted_disease_info['name']
        image_folder = predicted_disease_info['image_folder']

        disease_names = [disease_classes[i]['name'] for i in range(len(disease_classes))]

        image_urls = []
        if image_folder:
            image_path = os.path.join('static', 'disease_images', image_folder)
            if os.path.exists(image_path):
                for image_name in os.listdir(image_path):
                    image_urls.append(url_for('static', filename=f'disease_images/{image_folder}/{image_name}'))

        return jsonify({
            "predicted_disease": predicted_disease,
            "predicted_probabilities": predicted_probabilities.tolist(),
            "disease_names": disease_names,
            "similar_disease_images": image_urls
        })

    except Exception as e:
        print(f"Error occurred: {e}")
        return jsonify({"error": "An internal error occurred"}), 500

if __name__ == '__main__':
    app.run(debug=True)
