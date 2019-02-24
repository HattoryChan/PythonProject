
import pandas as pd
import matplotlib.pyplot as plt


df = pd.DataFrame({
    'Sex': ['female', 'male', 'gender'],
    'Smoke': [1, 8, 1]})

sums = df.Smoke.groupby(df.Sex).sum()
ax1 = plt.subplot(111, aspect = 'equal')

explode = (12, 0.2, 0.6)
df.plot(kind = 'pie', y ='Smoke', ax=ax1, autopct='%1.1f%%',
        startangle=90, shadow=False, labels= sums.index, fontsize=10,
        explode = [i/10 for i in range(0, len(df.Smoke))])
plt.legend(labels=sums.index, loc="best")
plt.axis('equal')



plt.show()

'''
ax1 = plt.subplot(121, aspect = 'equal')
df.plot(kind = 'pie', y ='Smoke',ax=ax1, autopct='%1.1f%%',
 startangle=90, shadow=False, labels= sums.index, legend = False, fontsize=14)
'''
