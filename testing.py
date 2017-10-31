import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
import seaborn as sns 

df = pd.DataFrame.from_csv("Airplane_Crashes_and_Fatalities_Since_1908.csv", index_col=None)

def investigate(s):
    data = {
        'weather': [
            'fog', ' rain', 'unlighted', 'thunder', 'turbulence', 'air pocket', 'adverse weather', 
            'mist', 'weather conditions', 'storm', 'typhoon', 'icing', 'bad weather', 'poor weather',
            'meteorological conditions', 'head wind', 'lightning', 'weather was poor', 'snow',
            'weather related', ' ice'
        ],
        'lost_control': ['disorientation', 'low altitude', 'loss of control'],
        'crash_landing': ['short of the runway', 'attempting to land', 'on approach', 'final approach'],
        'crash_takingoff': ['taking off', 'takeoff', 'take off'],
        'air_collision': ['mid-air', 'in-flight collision', 'midair', 'planes collided'],
        'shot_down': ['shot down', 'missile', 'rebel', 'fighter'],
        'mechanical_fail': [
            'engine', 'propeller', 'mechanical failure', 'rotor', 'out of fuel', 'system failure', 'component failure',
            'fatigue'
        ],
        'navigation error': [
            'navigational error', 'disoriented', 'altimiter', 'poor visibility', 'altimeter',
            'compass', 'gyros', 'navigational equipment', 'erroneous navigation'
        ],
        'human_error': [
            'failure of the crew', 'pilot error', 'did not follow', 'crew ignored', 'failure to', 
            'delayed landing', 'overloaded', 'misinterpretation', 'misjudge', 'failed to', 'lost control', 
            'inadequate risk', 'improper use', 'midjudge', 'poor crew'
        ],
        'terract': ['bomb', 'hijacker']
    }

    res = []
    for el, words in data.items():
        res += [el for word in words if word in s]
        
    return list(set(res))

df['Summary'].fillna('', inplace=True)
all_values = []
for s in df['Summary']:
    all_values += investigate(s.lower())

plt.figure(figsize=(20, 6))
pd.DataFrame(all_values)[0].value_counts().plot('bar')
plt.show()