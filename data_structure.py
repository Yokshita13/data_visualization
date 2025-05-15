import pandas as pd

data = {
    'Name' : ['Yokshita','Lakshya','Vivaan','Meera','Kabir','Ishita'],
    'ID' : [1,2,3,4,5,6]
}

df = pd.DataFrame(data)

print(df.shape) # Counts rows and columns

print(df.columns) # List of column names

print(df.dtypes) # Data types of each column

print(df.info) # Returns range index
