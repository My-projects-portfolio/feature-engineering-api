#!/usr/bin/env python
# coding: utf-8

# In[ ]:
from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd
import json
import io

# Create the FastAPI app
app = FastAPI()

# Add CORS middleware to allow requests from all origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allow all methods
    allow_headers=["*"],  # Allow all headers
)

# Feature engineering logic
def process_json_file(content):
    raw_json = json.load(io.BytesIO(content))
    all_loans = []
    for customer in raw_json["data"]:
        for loan in customer["loans"]:
            all_loans.append(loan)
    df = pd.DataFrame(all_loans)

    # Convert types
    df["amount"] = pd.to_numeric(df["amount"])
    df["fee"] = pd.to_numeric(df["fee"])
    df["loan_status"] = pd.to_numeric(df["loan_status"])
    df["annual_income"] = pd.to_numeric(df["annual_income"])

    # Group and aggregate
    features = df.groupby("customer_ID").agg({
        "amount": ["sum", "mean", "count"],
        "fee": "mean",
        "loan_status": "mean",
        "term": lambda x: x.mode()[0] if not x.mode().empty else "unknown",
        "annual_income": "first"
    })

    features.columns = ['_'.join(col).strip('_') for col in features.columns]
    features.reset_index(inplace=True)

    return features.to_dict(orient="records")

# ---------- ROUTES ----------

# Health check route
@app.get("/health")
def health_check():
    return {"status": "UP"}

# Root route to test if the app is running
@app.get("/")
def read_root():
    return {"message": "Hello, World!"}

# Route to process the uploaded file and generate features
@app.post("/features")
async def generate_features(file: UploadFile = File(...)):
    content = await file.read()
    result = process_json_file(content)
    return {"features": result}



