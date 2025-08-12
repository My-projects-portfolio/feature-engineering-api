# 🧠 Feature Engineering API + ML Models

## 📘 Project Overview: Customer Loan Feature Engineering API
## API Documentation

The API documentation can be accessed at:

[Feature Engineering API](https://feature-engineering-api.onrender.com/docs)
### 🧠 Project Objective

The aim of this project is to build a robust **Feature Engineering API** that transforms raw customer loan data into structured, machine-learning-ready features. These features are critical for downstream tasks such as default prediction, customer segmentation, and loan forecasting.

Using **FastAPI**, the project delivers an accessible interface for submitting customer data and retrieving engineered features in real-time — a practical step toward building **data-driven decision systems** in finance or retail.

---

### 🎯 Business Use Case

Businesses (such as lenders, fintechs, or retailers offering credit) often collect transactional loan data. This data, while rich, must be **pre-processed and transformed** before it can be used effectively in machine learning models.

This API helps automate that transformation by:
- Aggregating customer-level statistics
- Engineering new predictive features
- Returning clean, structured output ready for modeling

---

### 🔧 Technical Goals

- Build a **modular Python service** for automated feature engineering
- Expose it via **REST API endpoints** using the FastAPI framework
- Prepare the engineered dataset for ML tasks like classification, regression, and clustering

---

### ⚙️ Tech Stack

- **Python 3.8+**
- **FastAPI**
- **Pandas**
- **scikit-learn**
- **Docker** *(optional)*

---

### 📤 API Endpoints

1. **POST `/features`**  
   Accepts a JSON file containing customer loan records.  
   Returns: A JSON response with aggregated customer-level features.

2. **GET `/health`**  
   A simple health check endpoint.  
   Returns:  
   ```json
   { "status": "UP" }
   ```

---

### 📥 Input Data

- Format: JSON (`cvas_data.json`)
- Structure: Each record contains one or more loan entries per customer
- Fields include:
  - `customer_ID`
  - `loan_date`
  - `amount`
  - `fee`
  - `loan_status`
  - `term`
  - `annual_income`

---

### 📤 Output Data

- Format: JSON (or saved as CSV internally)
- Includes aggregated and transformed features per customer

---

## 🛠️ Features

- Upload raw JSON loan data via FastAPI
- Automatically runs feature engineering
- Returns structured customer-level features
- Trains 3 ML models:
  - Classification (loan default)
  - Clustering (customer segmentation)
  - Regression (loan size prediction)

---

## 📁 Project Structure

```
feature-engineering-api/
├── app/
│   ├── main.py
│   ├── ml-models.py
├── data/
│   ├── cvas_data.json
│   ├── customer_features.csv
│   └── customer_features_with_cluster.csv
├── requirements.txt
├── .gitignore
└── README.md
```

---

## 📥 How to Install and Run

### 1. Clone the Repository

```bash
git clone https://github.com/My-projects-portfolio/feature-engineering-api.git
cd feature-engineering-api
```

### 2. Create a Virtual Environment

```bash
python -m venv fe_api
source fe_api/bin/activate        # macOS/Linux
fe_api\Scripts\activate         # Windows
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🚀 Run the API

```bash
uvicorn app.main:app --reload
```

Open [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) to test the API.

---

## 🤖 Run ML Models

```bash
python app/ml-models.py
```

Outputs:
- 📈 Classification Report
- 🔍 Cluster assignments
- 📊 Regression RMSE
- 💾 CSV file with features and cluster labels

---

## 📦 Requirements

Python 3.8+
- fastapi
- uvicorn
- pandas
- scikit-learn

---

## 📊 Sample Output

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

**Nafiseh** – 
*Machine Learning & Data Science* 
[GitHub](https://github.com/My-projects-portfolio)

---

## 📃 License

MIT License — use freely for learning or real projects.
