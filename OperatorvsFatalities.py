import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns
from collections import Counter 
df = pd.read_csv("Airplane_Crashes_and_Fatalities_Since_1908.csv")

operator_fatal = df[['Operator','Fatalities']].groupby(['Operator']).sum()
operator_fatal = operator_fatal['Fatalities'].sort_values(ascending=False)[:10]
operator_fatal_keys = operator_fatal.index
operator_fatal_val = operator_fatal.values
fig,ax = plt.subplots(figsize=(8,6))
sns.barplot(x = operator_fatal_keys,y =operator_fatal_val)
plt.title('Operator vs Fatalities')
plt.xlabel('Operator')
plt.ylabel('Total Fatalities')
ticks = plt.setp(ax.get_xticklabels(),rotation=90)

plt.show()