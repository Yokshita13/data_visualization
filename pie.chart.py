import pandas as pd
import matplotlib.pyplot as plt

data = {
    'flavors': ['Vanilla', 'Chocolate', 'Strawberry', 'Mint', 'Mango'],
    'votes': [35, 30, 15, 10, 10]
}


df = pd.DataFrame(data)


# colors = ['#fcebb7', '#8b4513', '#fc5a8d', '#98ff98', '#ffcc5c']

colors = ['white','brown','pink','green','yellow']

plt.figure(figsize=(6,6))

plt.pie(df['votes'], labels=df['flavors'], autopct='%1.1f%%', startangle=140)
plt.title("Favorite Ice Cream Flavors")
plt.axis('equal')
plt.show()