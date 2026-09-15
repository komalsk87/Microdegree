import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# 1. Load raw dataset
df = pd.read_csv("customer_support_tickets.csv")

# 2. Fill missing values based on data type
for col in df.columns:
    if pd.api.types.is_numeric_dtype(df[col]):
        df[col] = df[col].fillna(0)
    else:
        df[col] = df[col].fillna("No data available")

# 3. Save the cleaned DataFrame to a new CSV file
df.to_csv("customer_support_tickets_cleaned.csv", index=False)
print(
    "Cleaned dataset successfully saved to 'customer_support_tickets_cleaned.csv'!"
)

# 4. Plot category distribution
plt.figure(figsize=(10, 5))
ax = sns.countplot(
    data=df,
    x="Ticket Type",
    palette="viridis",
    order=df["Ticket Type"].value_counts().index,
)

plt.title("Distribution of Customer Support Tickets by Category", fontsize=14)
plt.xlabel("Ticket Type", fontsize=12)
plt.ylabel("Total Count", fontsize=12)
plt.xticks(rotation=15)

# Add counts above bars
for p in ax.patches:
    ax.annotate(
        f"{int(p.get_height())}",
        (p.get_x() + p.get_width() / 2.0, p.get_height()),
        ha="center",
        va="center",
        xytext=(0, 6),
        textcoords="offset points",
    )

plt.tight_layout()
plt.show()