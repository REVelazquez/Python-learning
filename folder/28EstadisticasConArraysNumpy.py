import numpy as np

#   Numpy ofrece herramientas de estadística básica para auxiliar en procesos de pruebas y análisis. Considera el código de abajo para nuestros ejemplos.

dataset= np.arange(1,16).reshape(5, 3)
print(dataset)
#   Esto nos retorna:
# [[ 1  2  3]
#  [ 4  5  6]
#  [ 7  8  9]
#  [10 11 12]
#  [13 14 15]]

# ------------- np.mean() ------------- 

#   Esta herramienta nos retorna la media de los elementos del array a lo largo del eje especificado. Para obtener la media de las líneas de un array
# bidimensional debemos configurar el argumento axis como 0

print(np.mean(dataset, axis = 0)) #[7. 8. 9.]

#   Y si quisiéramos obtener la media por las columnas el argumento axis debe tener valor 1

print(np.mean(dataset, axis = 1)) #[ 2.  5.  8. 11. 14.]

# ------------- np.std() ------------- 
#   Retorna la desviación estándar ed los elementos del array a lo largo del eje especificado. Para obtener la desviación estándar por las líneas de un
# array bidimensional debemos configurar el argumento axis como 0 y para obtener la desviación estándar por las columnas el argumento axis debe tener valor 1

# Lineas
print(np.std(dataset, axis=0)) #[4.24264069 4.24264069 4.24264069]
# Columnas
print(np.std(dataset, axis=1)) #[0.81649658 0.81649658 0.81649658 0.81649658 0.81649658]

# ------------- np.sum() ------------- 

#   Retorna la suma de los elementos del array a lo largo del eje especificado. Para obtener la sumatoria por las líneas con un array bidimensional, el argumento
# axis debe ser configurado como 0, si es configurado como 1 sera para las columnas

# Lineas
print(np.sum(dataset, axis = 0)) #[35 40 45]
# Columnas
print(np.sum(dataset, axis = 1)) #[ 6 15 24 33 42]
