import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns
from collections import Counter 
df = pd.read_csv("Airplane_Crashes_and_Fatalities_Since_1908.csv")

df['Date'] = pd.to_datetime(df['Date'])
df['Year'] = df['Date'].map(lambda x:x.year)

type_count = Counter(df['Type'].dropna().tolist()).most_common(10)
type_index = [type_[0] for type_ in type_count]
type_val = [type_[1] for type_ in type_count]

fig,ax = plt.subplots(figsize=(8,6))
sns.barplot(x = type_index , y = type_val)
plt.title('Top 10 type')
plt.xlabel('Type')
plt.ylabel('Count')
ticks = plt.setp(ax.get_xticklabels(),rotation=90)
plt.show()