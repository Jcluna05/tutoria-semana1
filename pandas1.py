# Importamos la librería pandas, que se usa para manipular y analizar datos
import pandas as pd

# Creamos un diccionario con los datos de los estudiantes
# Cada clave representa una columna del DataFrame
datos = {
    'Nombre': ['Ana', 'Luis', 'María', 'Carlos', 'Sofía'],
    'Nota1': [80, 55, 78, 90, 60],
    'Nota2': [75, 60, 85, 88, 65],
    'Nota3': [90, 50, 82, 92, 70]
}

# Convertimos el diccionario en un DataFrame de pandas
df = pd.DataFrame(datos)

# Mostramos el DataFrame original
print("Datos originales de los estudiantes:")
print(df)

# Calculamos el promedio de las tres notas para cada estudiante
# Se crea una nueva columna llamada 'Promedio'
df['Promedio'] = df[['Nota1', 'Nota2', 'Nota3']].mean(axis=1)

# Mostramos el DataFrame con el promedio calculado
print("\nDatos con promedio de notas:")
print(df)

# Filtramos los estudiantes que tienen un promedio mayor o igual a 60 (es decir, aprobaron)
estudiantes_aprobados = df[df['Promedio'] >= 60]

# Mostramos únicamente a los estudiantes que aprobaron
print("\nEstudiantes que aprobaron:")
print(estudiantes_aprobados)
