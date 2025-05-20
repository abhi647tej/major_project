from flask import Flask, request, jsonify
import onnxruntime as ort
import numpy as np
from PIL import Image

app = Flask(__name__)

# Load class labels
with open("classes.txt", "r") as f:
    class_names = [line.strip() for line in f.readlines()]

# Load ONNX model
session = ort.InferenceSession("best.onnx")
input_name = session.get_inputs()[0].name

# Image preprocessing
def preprocess(image, size=224):
    img = image.convert("RGB").resize((size, size))
    img = np.array(img).astype(np.float32) / 255.0
    img = np.transpose(img, (2, 0, 1))  # CHW
    img = np.expand_dims(img, axis=0)  # Add batch dimension
    return img

# API endpoint
@app.route("/predict", methods=["POST"])
def predict():
    if "image" not in request.files:
        return jsonify({"error": "No image uploaded"}), 400

    file = request.files["image"]
    image = Image.open(file.stream)
    img_array = preprocess(image)

    output = session.run(None, {input_name: img_array})
    pred_idx = int(np.argmax(output[0]))
    confidence = float(np.max(output[0]))
    
    if(confidence<=0.7):
        return jsonify({
            "class": "Not a Drug",
            "confidence": round(confidence, 3)
        })

    return jsonify({
        "class": class_names[pred_idx],
        "confidence": round(confidence, 3)
    })

if __name__ == "__main__":
    app.run(debug=True)



