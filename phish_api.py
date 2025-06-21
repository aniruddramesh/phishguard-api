from flask import Flask, request, jsonify
import pickle
import re

# Load your trained phishing detection model
model = pickle.load(open("phishing_url_model.pkl", "rb"))

# Initialize Flask app
app = Flask(__name__)

# Root endpoint to fix 404 error
@app.route('/')
def home():
    return "✅ PhishGuard API is Live! Use /predict?url=... to test a URL."

# Feature extraction function
def extract_features(url):
    features = []
    features.append(len(url))
    features.append(url.count('@'))
    features.append(url.count('http'))
    features.append(url.count('https'))
    features.append(url.count('.'))
    features.append(url.count('/'))
    features.append(bool(re.search(r'//', url)))
    features.append(bool(re.search(r'-', url)))
    features.append(bool(re.search(r'\d', url)))
    return [features]

# Prediction route
@app.route('/predict')
def predict():
    url = request.args.get('url')
    
    if not url:
        return jsonify({"error": "Please provide a URL using ?url=..."})

    features = extract_features(url)
    prediction = model.predict(features)[0]
    
    label = "phishing" if prediction in [1, 'bad'] else "safe"
    return jsonify({"result": label})

# Local testing only (ignored in production)
if __name__ == '__main__':
    app.run(debug=True)
