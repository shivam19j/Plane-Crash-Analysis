import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns
from collections import Counter 
#%matplotlib inline

from subprocess import check_output
#print(check_output(["ls", "../input"]).decode("utf8"))

df = pd.read_csv("Airplane_Crashes_and_Fatalities_Since_1908.csv")
#print(df.head())

#test = pd.read_csv("Airplane_Crashes_and_Fatalities_Since_1908.csv")
test_shape = df.shape
#print(test_shape)

