import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("css/project/dataset/Amazon_Dataset.csv")

df.columns = df.columns.str.strip()


df["Order Date"] = pd.to_datetime(df["Order Date"], dayfirst=True, errors='coerce')


df_sorted = df.sort_values(by="Order Date")


plt.figure(figsize=(10, 5))
plt.scatter(df_sorted["Order Date"], df_sorted["Final Price"], color="blue")
plt.title("📦 Amazon Final Price Scatter Plot")
plt.xlabel("Order Date")
plt.ylabel("Final Price (₹)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.grid()
plt.show()
