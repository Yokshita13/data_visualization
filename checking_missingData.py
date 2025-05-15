import pandas as pd

data = {
    'Name' : ['Yokshita','Lakshya',None,'Meera','Kabir','Ishita'],
    'ID' : [1,2,3,None,5,6]
}

df = pd.DataFrame(data)

print(df.isnull()) # Used to detect NAN values

print(df.isnull().sum()) # Total missing values per column

print(df.isnull().any()) # Checks if any column has missing values
