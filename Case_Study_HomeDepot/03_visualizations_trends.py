
# 03_visualizations_trends.py

"""
Step 3: Generate time series visualizations for Winning CPM and Impressions over time.
"""

import seaborn as sns
import matplotlib.pyplot as plt

# Line plot of Winning CPM over time
sns.lineplot(data=df, x="Date", y="Winning CPM")
plt.title("Winning CPM Over Time")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("trend_winning_cpm.png")

# Line plot of Impressions over time
sns.lineplot(data=df, x="Date", y="Impressions")
plt.title("Impressions Over Time")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("trend_impressions.png")
