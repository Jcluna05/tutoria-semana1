import pandas as pd
import sys
import datetime as dt
import numpy as np
import matplotlib.pyplot as plt
import matplotlib

#%matplotlib inline
df = pd.DataFrame({'date':['17 MAY2018']})
df
df['date2'] = pd.to_datetime(df['date'])

df
mi_df = pd.read_json('data/data-demo-3.json')
mi_df
mi_df.dtypes
mi_df['edad'] = mi_df['edad'].astype(float)
mi_df
mi_df = pd.read_json('data/data-demo-4.json')
mi_df
mi_df['edad2'] = mi_df['edad'].str.replace("edad", "").astype("int")
print(mi_df)
