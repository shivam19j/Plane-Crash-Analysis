import numpy as np
import pandas as pd 
from matplotlib import pyplot as plt

df = pd.read_csv('Airplane_Crashes_and_Fatalities_Since_1908.csv', sep=',')

plt.scatter(df['Aboard'], df['Fatalities'], alpha=0.7, s = 50)
plt.xlabel('Aboard')
plt.ylabel('Fatalities')
plt.show()

df['survivors'] = 100*(df.Aboard - df.Fatalities)/df.Aboard
df['survivors'].dropna().plot(kind='hist')
plt.xlabel('% survivors')
plt.show()

df['Date'] = pd.to_datetime(df['Date'])
survivors_series = df.groupby(df['Date'].dt.year)['survivors'].mean()
survivors_series = pd.Series(survivors_series, index=survivors_series.index)
survivors_series.dropna().plot()
plt.ylabel('% survivors')
plt.show()

from pandas.tools.plotting import autocorrelation_plot
autocorrelation_plot(survivors_series.diff().dropna())
plt.show()

