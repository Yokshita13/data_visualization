import pandas as pd

data1 = {
    'Student': ['Yokshita', 'Prakhyat', 'Hasi', 'Shuddhi', 'Pratishtha', 'Lakshya', 'Arnav', 'Khushi'],
    'Department': ['AI', 'DS', 'AI', 'DS', 'AI', 'DS', 'AI', 'DS'],
    'ID' : [1,2,3,4,5,6,7,8]
}

data2 = {
    'ID' : [9,10,11,14,15,16,17,18],
    'Score': [85, 78, 92, 88, 75, 82, 90, 79],
    'Semester': [1, 1, 2, 2, 1, 1, 2, 2]
}

df1 = pd.DataFrame(data1)
df2 = pd.DataFrame(data2)

print("By using Merge function")
merge = pd.merge(df1,df2,on='ID', how='inner')
print(merge)
print("\n")

print("By using Join function")
join = df1.join(df2, how='left')
print(join)
print("\n")

print("By using concatenate function")
concate = pd.concat([df1,df2])