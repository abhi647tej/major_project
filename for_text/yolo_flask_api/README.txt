YOLOv8 ONNX Flask API
=====================

1. Place your exported model.onnx file in this folder (same as app.py)
2. Install requirements:
   pip install flask onnxruntime pillow numpy
3. Run the API:
   python app.py
4. Send POST requests to:
   http://localhost:5000/predict
   With an image file (key = "image")

Example using curl:
   curl -X POST http://127.0.0.1:5000/predict -F image=@test.jpg
