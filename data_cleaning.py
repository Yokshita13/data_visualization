import pandas as pd

data = {
    'Name': ['Yokshita','Hasi','Prakhyat','Shuddhi','Pratishtha',None],
    'ID' : [1,2,None,4,5,6]
}

df = pd.DataFrame(data)

print("Adding Columns")
df['Age'] = [18,19,26,19,20,27] 
print(df)
print("\n")

print("Deleting a column/rows")
df.drop(columns=['Age'],inplace=False) 
print(df)
print("\n")

print("Filtering Data")
df[df['Age']>25]  
print(df)
print("\n")

print("Sorting Data")
df.sort_values(by='Age',ascending=False) 
print(df)
print("\n")

print("Handling Missing Values")
df.dropna(inplace=True) 
print(df)
print("\n")

print("Fill missing values")
df.fillna(0,inplace=True) 
print(df)
print("\n")

print("Renaming Columns")
df.rename(columns={'Name':'Unique ID'},inplace=True) 
print(df)
print("\n")

print("Removing Duplicates")
df.drop_duplicates(inplace=True) 
print(df)
print("\n")

print("Replacing Values")
df.replace('Hasi','Hasii',inplace=True)
print(df)