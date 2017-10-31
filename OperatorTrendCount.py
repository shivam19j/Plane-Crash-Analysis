import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns
from collections import Counter 
df = pd.read_csv("Airplane_Crashes_and_Fatalities_Since_1908.csv")

df['Date'] = pd.to_datetime(df['Date'])
df['Year'] = df['Date'].map(lambda x:x.year)

operator_count = Counter(df['Operator'].dropna().tolist()).most_common(5)
operator_list = [operator[0] for operator in operator_count] 
operator_trend = df[['Operator','Year','Fatalities']].groupby(['Operator','Year']).agg(['sum','count'])
operator_trend = operator_trend['Fatalities'].reset_index()

fig,ax = plt.subplots(figsize=(8,6))
plt.title('Operator trend')
plt.ylabel('Total Fatalities')
plt.xlabel('Year')
for operator in operator_list:
    operator_trend[operator_trend['Operator'] == operator].plot(x = 'Year',
                                                                y = 'count',
                                                                linewidth=2,
                                                                ax=ax,
                                                                label=operator)
plt.show()