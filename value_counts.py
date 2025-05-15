import pandas as pd

data = {
    'Name' : ['Yokshita','Lakshya','Vivaan','Meera','Kabir','Ishita'],
    'ID' : [1,2,3,4,5,6]
}

df = pd.DataFrame(data)

print(df['Name'].value_counts()) #Frequency of unique values in a column