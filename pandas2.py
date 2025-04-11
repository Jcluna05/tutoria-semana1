# Importación de librerías necesarias para análisis de datos y visualización

import pandas as pd  # Librería principal para manipulación de datos tabulares
import sys           # Permite acceder a funciones del sistema (no se usa explícitamente en este código)
import datetime as dt  # Sirve para manejar fechas (no se utiliza en este ejemplo)
import numpy as np   # Útil para cálculos numéricos avanzados (no se utiliza en este ejemplo)
import matplotlib.pyplot as plt  # Usada para generar gráficos
import matplotlib     # Complementa funciones de configuración de gráficos

# NOTA: La siguiente línea solo se usa en notebooks para mostrar gráficos en línea:
# %matplotlib inline

# Instalación de la librería 'xlrd' para poder leer archivos Excel antiguos (.xls)
# Solo necesaria si no está instalada previamente
# Ejecutar esto en la terminal o en una celda mágica de Jupyter
# !pip install xlrd

# Leemos el archivo Excel ubicado en la carpeta 'data', llamado 'data-uno.xls'
# Usamos la primera fila como encabezado por defecto
mi_df = pd.read_excel('data/data-uno.xls')

# Mostramos el contenido del DataFrame leído
print("Contenido del archivo con encabezados por defecto:")
print(mi_df)

# Volvemos a leer el archivo Excel, esta vez indicando que no utilice encabezado del archivo original
# En su lugar, asignamos nombres personalizados a las columnas: 'v1', 'v2', 'v3'
mi_df = pd.read_excel('data/data-uno.xls', header=None, names=["v1", "v2", "v3"])

# Mostramos el nuevo DataFrame con nombres de columnas personalizados
print("\nContenido del archivo con encabezados personalizados:")
print(mi_df)
