
# 05_pricing_recommendation_simulation.py

"""
Step 5: Recommend floor CPMs and simulate pre/post revenue uplift.
"""

df["Predicted_CPM"] = rf.predict(X)
recommended_floors = (
    df.groupby(["Taxonomy_Encoded", "Week"])["Predicted_CPM"]
    .quantile(0.25).reset_index()
    .rename(columns={"Predicted_CPM": "Recommended_Floor_CPM"})
)

df = df.merge(recommended_floors, on=["Taxonomy_Encoded", "Week"], how="left")
df["Simulated_CPM"] = np.maximum(df["Predicted_CPM"], df["Recommended_Floor_CPM"])
df["Actual_Revenue"] = df["Winning CPM"] * df["Impressions"] / 1000
df["Simulated_Revenue"] = df["Simulated_CPM"] * df["Impressions"] / 1000

uplift = df["Simulated_Revenue"].sum() - df["Actual_Revenue"].sum()
print("Revenue Uplift:", uplift)
