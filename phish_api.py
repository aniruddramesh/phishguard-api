from flask import Flask, request, jsonify
import re
import pandas as pd
import joblib
from flask_cors import CORS

# Load the trained model
model = joblib.load("phishing_url_model.pkl")

# Initialize Flask app
app = Flask(__name__)
CORS(app)  # Allow requests from browser extension

# Feature extraction function
def extract_features(url):
    features = {
        'url_length': len(url),
        'num_dots': url.count('.'),
        'num_hyphens': url.count('-'),
        'num_at': url.count('@'),
        'num_equals': url.count('='),
        'has_https': 1 if url.startswith('https') else 0,
        'has_ip': 1 if re.match(r'http[s]?://\d+\.\d+\.\d+\.\d+', url) else 0,
        'has_login': 1 if 'login' in url.lower() else 0,
        'has_verify': 1 if 'verify' in url.lower() else 0,
        'has_secure': 1 if 'secure' in url.lower() else 0,
        'has_bank': 1 if 'bank' in url.lower() else 0
    }
    return pd.DataFrame([features])

# Predict route
@app.route('/predict', methods=['GET'])
def predict():
    url = request.args.get('url', '')
    if not url:
        return jsonify({'error': 'URL parameter is missing'}), 400

    features = extract_features(url)
    prediction = model.predict(features)[0]
    result = 'phishing' if prediction == 1 else 'safe'
    return jsonify({'result': result})

# Run app
if __name__ == '__main__':
    app.run(debug=True)
