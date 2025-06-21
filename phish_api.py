from flask import Flask, request, jsonify
import pickle
import re

# Load your trained model
model = pickle.load(open("phishing_url_model.pkl", "rb"))

app = Flask(__name__)

# Route for root URL (to fix 404 issue)
@app.route('/')
def home():
    return "✅ PhishGuard API is Live! Use /predict?url=... to test a URL."

# Function to extract features from a URL
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

# Prediction endpoint
@app.route('/predict')
def predict():
    url = request.args.get('url')

    if not url:
        return jsonify({"error": "Please provide a URL using ?url=..."})

    features = extract_features(url)
    prediction = model.predict(features)[0]

    label = "phishing" if prediction == 1 or prediction == 'bad' else "safe"
    return jsonify({"result": label})

if __name__ == '__main__':
    app.run(debug=True)
