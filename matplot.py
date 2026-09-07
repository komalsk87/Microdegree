import matplotlib.pyplot as plt

# x = [1, 2, 3, 4, 5]
# y = [2, 3, 5, 7, 11]

# plt.plot(x,y)
# plt.show()

# x = ['mon', 'tue', 'wed', 'thu', 'fri']
# y = ['12' , '15', '20', '25', '30']

# plt.bar(x,y)
# plt.title('Bar Graph')
# plt.xlabel('Days')
# plt.ylabel('Attendance')
# plt.show()

import pandas as pd

df = pd.read_csv('employees.csv')
plt.bar(df['Salary'], df['Bonus %'])
plt.title('Salary vs Bonus')
plt.xlabel('Salary')
plt.ylabel('Bonus %')
plt.show()