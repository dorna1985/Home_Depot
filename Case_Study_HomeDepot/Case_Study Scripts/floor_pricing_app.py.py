import streamlit as st
import pandas as pd
import numpy as np
import io

# --- Load or simulate sample data (replace this with actual df loading) ---
@st.cache_data
def load_data():
    np.random.seed(42)
    n = 500
    df = pd.DataFrame({
        "Taxonomy_Encoded": np.random.choice(["A", "B", "C", "D"], size=n),
        "Week": np.random.randint(1, 12, size=n),
        "Predicted_CPM": np.random.uniform(1.0, 5.0, size=n),
        "Impressions": np.random.randint(1000, 10000, size=n)
    })
    return df

df = load_data()

# --- UI ---
st.title("📊 Floor Pricing Simulator")
q = st.slider("Select Quantile for Floor Pricing", 0.1, 0.5, 0.25, step=0.05)

# --- Floor Pricing Logic ---
recommended = df.groupby(["Taxonomy_Encoded", "Week"])["Predicted_CPM"].quantile(q).reset_index()
recommended.columns = ["Taxonomy_Encoded", "Week", "Recommended_Floor"]
merged = df.merge(recommended, on=["Taxonomy_Encoded", "Week"])
merged["Simulated"] = np.maximum(merged["Predicted_CPM"], merged["Recommended_Floor"])
merged["Revenue"] = merged["Simulated"] * merged["Impressions"] / 1000

# --- Output ---
total_revenue = merged["Revenue"].sum()
st.metric("💰 Total Simulated Revenue", f"${total_revenue:,.2f}")
st.dataframe(merged.head(10))

# --- Save & Offer Download ---
csv = merged.to_csv(index=False)
st.download_button(
    label="📥 Download Results as CSV",
    data=csv,
    file_name="simulated_floor_pricing_results.csv",
    mime="text/csv"
)
