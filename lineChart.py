import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("css/project/dataset/Amazon_Dataset.csv")


df["Order Date"] = pd.to_datetime(df["Order Date"], dayfirst=True)

df_sorted = df.sort_values(by="Order Date")

plt.figure(figsize=(10, 5))
plt.plot(df_sorted["Order Date"], df_sorted["Final Price"], color="blue", marker="o")
plt.title("📈 Final Price Over Time")
plt.xlabel("Order Date")
plt.ylabel("Final Price (₹)")
plt.xticks(rotation=45)
plt.grid()
plt.tight_layout()
plt.show()
