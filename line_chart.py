import pandas as pd
import matplotlib.pyplot as plt

data = {
    'Months' : ['January'	,'February'	,'March','April','May','June','July','August','September','October','November','December'],
    'Sales' : [1200,1500,1700,1600,1800,2000,2200,2100,2300,2400,2500,2700]
}

df = pd.DataFrame(data)

df.plot(x='Months',y='Sales',kind='line',marker='o',color='b',linestyle='-')
plt.title("Sales Over Time")
plt.xlabel('Months')
plt.ylabel('Sales')
plt.grid()
plt.show()