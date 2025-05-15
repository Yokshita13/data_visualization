import pandas as pd

import pandas as pd

# Series: 1D labeled data

s = pd.DataFrame([10,20,30,40], index=['a','b','c','d'])

print(s)

# DataFrame: 2D labeled data (rows & columns)

data = {
    'Name' : ['Yokshita','Lakshya','Vivaan','Meera','Kabir','Ishita'],
    'ID' : [1,2,3,4,5,6]
}

df = pd.DataFrame(data)
print(df)