import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns
from collections import Counter 
df = pd.read_csv("Airplane_Crashes_and_Fatalities_Since_1908.csv")

df['Date'] = pd.to_datetime(df['Date'])
df['Year'] = df['Date'].map(lambda x:x.year)

table_count = df.groupby([df['Year']])['Fatalities'].size()

year = table_count.index
table_count_val = table_count.values
fig,ax = plt.subplots(figsize=(15,6))
sns.barplot(x = year , y = table_count_val)
plt.title('Fatalities per year')
plt.xlabel('Year')
plt.ylabel('Count')
ticks = plt.setp(ax.get_xticklabels(),rotation=90)
plt.show()