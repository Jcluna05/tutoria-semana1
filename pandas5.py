import pandas as pd
import sys
import datetime as dt
import numpy as np
import matplotlib.pyplot as plt
import matplotlib

#%matplotlib inline
mi_df = pd.read_json('data/data-demo-5.json')
mi_df
mi_df = mi_df.dropna()
mi_df.fillna(0)