
# 01_data_cleaning_transformation.py

"""
Step 1: Data Cleaning and Feature Engineering Script
This script loads the raw Excel file, removes nulls, performs feature engineering,
and prepares the dataset for modeling.
"""

import pandas as pd
from sklearn.preprocessing import LabelEncoder

# Load Excel data
df = pd.read_excel("Auction Banner Case Study - vF.xlsx", sheet_name="Data")

# Clean column names
df.columns = df.columns.str.strip()

# Drop rows missing critical fields
df = df.dropna(subset=["Winning CPM", "Sales", "Ad Spend", "Impressions"]).copy()

# Parse dates and create new features
df["Date"] = pd.to_datetime(df["Date"])
df["Revenue_Per_Impression"] = df["Sales"] / df["Impressions"]
df["CPM_Delta"] = df["Winning CPM"] - df["Floor CPM"]
df["CTR_Proxy"] = df["Impressions"] / df["Traffic"]
df["Week"] = df["Date"].dt.isocalendar().week
df["Month"] = df["Date"].dt.month
df["Year"] = df["Date"].dt.year

# Encode categorical column
le = LabelEncoder()
df["Taxonomy Name"] = df["Taxonomy Name"].astype(str)
df["Taxonomy_Encoded"] = le.fit_transform(df["Taxonomy Name"])
