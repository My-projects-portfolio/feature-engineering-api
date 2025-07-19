# 🧠 Feature Engineering API + ML Models

This project builds a real-world, end-to-end system that:
- 🧰 Processes customer loan records through feature engineering
- 🚀 Exposes the logic via a FastAPI web service
- 🤖 Trains three types of machine learning models:
  - Classification: Predict loan default
  - Clustering: Segment customers
  - Regression: Predict ideal loan size

It’s designed to simulate how modern businesses (like fintech or retailers) can become **more data-driven** using predictive modeling and behavior profiling.

---

## 📌 Project Purpose

Many companies want to:
- Predict customer **churn**, **risk**, or **default**
- Optimize **loan offerings** or **pricing**
- Segment customers based on financial behavior

This project offers a framework for doing all of the above using Python, FastAPI, and scikit-learn — with clean code, data handling, and model training.

---

## 🛠️ Features

- Upload customer loan data via a FastAPI endpoint (`/features`)
- Automatically run feature engineering (aggregate stats per customer)
- Save cleaned output to CSV
- Train 3 ML models on the features:
  - **Classifier** to predict loan default
  - **KMeans** for customer segmentation
  - **Linear Regression** for loan forecasting

---

## 📁 Project Structure

```
feature-engineering-api/
├── app/
│   ├── main.py              # FastAPI app for feature engineering
│   ├── ml-models.py         # Runs all 3 ML models
├── data/
│   ├── cvas_data.json       # Raw customer + loan input data
│   ├── customer_features.csv        # Output of feature engineering
│   └── customer_features_with_cluster.csv # Final output w/ clusters
├── requirements.txt
├── .gitignore
└── README.md
```

---

## 📥 How to Install and Run

### 🔧 1. Clone the Repository

```bash
git clone https://github.com/My-projects-portfolio/feature-engineering-api.git
cd feature-engineering-api
```

### 🐍 2. Create a Virtual Environment

```bash
python -m venv fe_api
source fe_api/bin/activate   # on macOS/Linux
# or
fe_api\Scripts\activate      # on Windows
```

### 📦 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🚀 How to Run the FastAPI App

```bash
uvicorn app.main:app --reload
```

Then open: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)  
Use the interactive Swagger UI to upload `cvas_data.json` and view the engineered features.

---

## 🤖 How to Run ML Models

This script trains all 3 ML models and saves results to CSV:

```bash
python app/ml-models.py
```

### You’ll Get:
- 📈 Classification report (default prediction)
- 🔍 Cluster labels for each customer
- 📊 Regression RMSE (loan size prediction)
- 💾 Final output in: `data/customer_features_with_cluster.csv`

---

## 📦 Requirements

Python 3.8+
```txt
fastapi
uvicorn
pandas
scikit-learn
```

---

## 📊 Sample ML Output

```
📌 Classification Report:
              precision    recall  f1-score   support
           0       0.89      0.92      0.91        26
           1       0.78      0.70      0.74        10

📌 Cluster Sizes:
0    22
1    8
2    6

📌 Regression RMSE: 1032.56
```

---

## 🧑‍💻 Author

**Nafiseh Imanian**  
PhD in Computer Science | Machine Learning Engineer  
[GitHub](https://github.com/My-projects-portfolio)

---

## 📃 License

MIT License — use freely for learning or real projects.
