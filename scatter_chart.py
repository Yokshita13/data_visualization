import pandas as pd
import matplotlib.pyplot as plt

data = {
'study_hours' : [1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0, 5.5, 6.0],
'scores' : [52, 58, 65, 70, 75, 78, 82, 85, 88, 90]
}

df = pd.DataFrame(data)

df.plot(x='study_hours',y='scores',kind='scatter',color='blue')

plt.title("Study Hours VS Scores")
plt.xlabel('study_hours')
plt.ylabel('scores')
plt.grid()
plt.show()