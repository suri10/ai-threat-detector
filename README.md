
# AI Threat Detector

A simple FastAPI-based threat detection API that uses a trained model to predict if network traffic is malicious based on the number of bytes transferred.

## 👨‍💻 Author
**Suresh**

---

## 🚀 How It Works
This project is a minimal implementation of a machine learning model served using FastAPI. It accepts a value for `bytes_transferred` and returns a prediction with a confidence score on whether the network traffic is malicious.

## 🛠️ Tech Stack
- **FastAPI**: for building the API
- **Joblib**: for model loading
- **Scikit-learn**: for the ML model (RandomForest)
- **Uvicorn**: ASGI server to run FastAPI

## 📦 Files & Structure
```
.
├── app
│   ├── main.py         # Main FastAPI app
│   └── model.pkl       # Trained model file
├── requirements.txt    # Python dependencies
├── README.md
└── .gitignore
```

## 📈 Endpoint
### `/predict`
- **Method**: POST
- **Request Body**:
```json
{
  "bytes_transferred": 4500
}
```
- **Response**:
```json
{
  "verdict": "benign",
  "confidence": 0.87
}
```

## 🧪 Run Locally
1. Clone the repo:
```bash
git clone https://github.com/suri10/ai-threat-detector.git
cd ai-threat-detector
```
2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # or .\venv\Scripts\activate on Windows
```
3. Install dependencies:
```bash
pip install -r requirements.txt
```
4. Run the app:
```bash
uvicorn app.main:app --reload
```

## ✅ To Do
- [x] Build and test prediction model
- [x] Create FastAPI app
- [x] Connect `/predict` endpoint
- [x] Set up for GitHub upload
- [ ] Deploy to cloud (Future)

## 🤝 Contributions
Pull requests are welcome!

## 📄 License
This project is open source and available under the [MIT License](LICENSE).

---

Let's catch threats with AI! 💻⚡

