# Project Overview: Customer Loan Feature Engineering API
🧠 Project Objective
The aim of this project is to build a robust Feature Engineering API that transforms raw customer loan data into structured, machine-learning-ready features. These features are critical for downstream tasks such as default prediction, customer segmentation, and loan forecasting.

Using FastAPI, the project delivers an accessible interface for submitting customer data and retrieving engineered features in real-time — a practical step toward building data-driven decision systems in finance or retail.

🎯 Business Use Case
Businesses (such as lenders, fintechs, or retailers offering credit) often collect transactional loan data. This data, while rich, must be pre-processed and transformed before it can be used effectively in machine learning models.

This API helps automate that transformation by:

Aggregating customer-level statistics

Engineering new predictive features

Returning clean, structured output ready for modeling

🔧 Technical Goals
Build a modular Python service for automated feature engineering

Expose it via REST API endpoints using the FastAPI framework

Prepare the engineered dataset for ML tasks like classification, regression, and clustering



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
