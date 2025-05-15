import pandas as pd
import matplotlib.pyplot as plt

data = {
    'marks': [45, 50, 55, 60, 62, 65, 66, 67, 68, 70,
              72, 74, 75, 76, 78, 80, 82, 85, 87, 90]
}

df = pd.DataFrame(data)

df.plot(kind='hist',bins=5,color='pink',edgecolor='yellow')
plt.title('Distribution of Student Marks')
plt.xlabel('Marks')
plt.ylabel('Number of Students')
plt.show()