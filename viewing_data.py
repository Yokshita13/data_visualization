import pandas as pd
import matplotlib.pyplot as plt

df= pd.read_csv("css/project/DV/Student_performance_dataset.csv")

print(df.head(48)) #display first n rows
print(df.tail(25)) #display last n rows
