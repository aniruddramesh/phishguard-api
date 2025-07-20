**PhishGuard API** is a smart browser extension project that detects phishing websites in real-time using a machine learning model trained on real phishing and legitimate URLs. It's built as a **data analytics hobby project** and integrates a **Random Forest classifier** with a Flask backend and a browser extension frontend.


Key Features

- **ML-powered Phishing Detection**  
  Trained using a curated dataset of phishing and safe URLs.

- **Browser Extension**  
  Chrome-compatible extension that actively monitors URLs being visited.

- **Fast, Lightweight API**  
  Flask backend receives URLs and responds with predictions from the trained model.


Tech Stack
| Layer        | Tech Used                    |
|--------------|-------------------------------|
| ML Model     | Python, scikit-learn (Random Forest) |
| Backend      | Flask REST API                |
| Frontend     | JavaScript (Chrome/Brave Extension) |
| Data Source  | Phishing & Legitimate URL datasets (open source) |
