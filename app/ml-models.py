#!/usr/bin/env python
# coding: utf-8

# In[7]:





# In[ ]:


import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.cluster import KMeans
from sklearn.linear_model import LinearRegression
from sklearn.metrics import classification_report, mean_squared_error

print("📊 Loading dataset...")
df = pd.read_csv("data/customer_features.csv")

# ----------------------- Classification ------------------------
print("\n🔍 Classification: Predicting Default Flag")

df["default_flag"] = (df["default_rate"] > 0.5).astype(int)

X_cls = df[["total_loan", "avg_loan", "loan_count", "avg_fee", "annual_income_first"]]
y_cls = df["default_flag"]

X_train, X_test, y_train, y_test = train_test_split(X_cls, y_cls, test_size=0.2)

clf = RandomForestClassifier()
clf.fit(X_train, y_train)
y_pred_cls = clf.predict(X_test)

print("📌 Classification Report:")
print(classification_report(y_test, y_pred_cls))

# ----------------------- Clustering ------------------------
print("\n🔍 Clustering: Segmenting Customers")

X_clu = X_cls  # same features

kmeans = KMeans(n_clusters=3, random_state=42)
df["cluster"] = kmeans.fit_predict(X_clu)

print("📌 Cluster Sizes:")
print(df["cluster"].value_counts())

# ----------------------- Regression ------------------------
print("\n🔍 Regression: Predicting Total Loan")

X_reg = df[["avg_loan", "loan_count", "avg_fee", "annual_income_first"]]
y_reg = df["total_loan"]

X_train, X_test, y_train, y_test = train_test_split(X_reg, y_reg, test_size=0.2)

reg = LinearRegression()
reg.fit(X_train, y_train)
y_pred_reg = reg.predict(X_test)

rmse = mean_squared_error(y_test, y_pred_reg, squared=False)
print(f"📌 Regression RMSE: {rmse:.2f}")

# ----------------------- Save Results ------------------------
df.to_csv("data/customer_features_with_cluster.csv", index=False)
print("\n✅ All models completed. Results saved to 'data/customer_features_with_cluster.csv'")

