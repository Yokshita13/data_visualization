import pandas as pd

data = {
    'Name' : ['Yokshita','Lakshya','Vivaan','Meera','Kabir','Ishita'],
    'ID' : [1,2,3,4,5,6]
}

df = pd.DataFrame(data)

print(df.info())

print(df.describe()) # Statistical summary (mean, std, min, etc.)