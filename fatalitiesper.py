import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns
from collections import Counter 
df = pd.read_csv("Airplane_Crashes_and_Fatalities_Since_1908.csv")

df['Date'] = pd.to_datetime(df['Date'])
df['Year'] = df['Date'].map(lambda x:x.year)


table_count = df[['Year','Fatalities']].dropna().groupby(['Year'])['Fatalities'].agg(['sum'])

table_count = table_count.dropna().reset_index()
table_count.columns = ['Year','Total Fatalities']
fig,ax = plt.subplots(figsize=(8,6))
table_count.plot(x = 'Year' , y = 'Total Fatalities',ax=ax)
plt.title('Fatalities per year')
plt.xlabel('Year')
plt.ylabel('Total Fatalities')
ticks = plt.setp(ax.get_xticklabels(),rotation=90)
plt.show()