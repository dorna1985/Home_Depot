
# 04_iv_calculation.py

"""
Step 4: Calculate Information Value (IV) using mutual information as a proxy.
"""

from sklearn.metrics import mutual_info_score

iv_scores = {
    col: mutual_info_score(X[col], pd.qcut(y, q=10, duplicates="drop"))
    for col in X.columns
}
iv_df = pd.DataFrame(list(iv_scores.items()), columns=["Feature", "IV_Score"])
iv_df.sort_values(by="IV_Score", ascending=False).to_excel("information_value_report.xlsx", index=False)
