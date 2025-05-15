import pandas as pd

data = {
    'Student': ['Yokshita', 'Prakhyat', 'Hasi', 'Shuddhi', 'Pratishtha', 'Lakshya', 'Arnav', 'Khushi'],
    'Department': ['AI', 'DS', 'AI', 'DS', 'AI', 'DS', 'AI', 'DS'],
    'Score': [85, 78, 92, 88, 75, 82, 90, 79],
    'Semester': [1, 1, 2, 2, 1, 1, 2, 2]
}

df = pd.DataFrame(data)

grouped = df.groupby('Department')['Score'].mean()
print("Average score by Department:\n", grouped)

print("\n")

grouped_multi = df.groupby(['Student', 'Department'])['Score'].mean()
print("Average score by Student and Department:\n", grouped_multi)