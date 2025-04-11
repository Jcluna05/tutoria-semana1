import pandas as pd
import sys
import datetime as dt
import numpy as np
import matplotlib.pyplot as plt
import matplotlib

#%matplotlib inline
mi_df = pd.read_json('data/data-demo-2.json')
mi_df
mi_df['nombres']
mi_funcion = lambda x: x.upper()
mi_df['nombres-mayuscula'] = mi_df['nombres'].apply(mi_funcion)
mi_df['apellidos'] = mi_df['apellidos'].apply(lambda x: x.upper())
mi_df
def count_nombres(x):
    valor = len(x)
    return valor


def count_apellidos(x):
    valor = len(x)
    if valor > 5:
        valor = 5

    return valor
mi_df['longitud-nombres'] = mi_df['nombres'].apply(count_nombres)
mi_df['longitud-apellidos'] = mi_df['apellidos'].apply(count_apellidos)
print(mi_df)