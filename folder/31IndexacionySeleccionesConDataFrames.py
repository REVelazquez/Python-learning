import pandas as pd


#   El operador de indexación de Python y NumPy [] ofrece acceso rápido y fácil a las estructuras de datos de Pandas. Eso
# facilita el aprendizaje visto que ya sabemos lidiar con consecuencias y diccionarios de Python y arrays NumPy. Pandas 
# también ofrece algunos métodos optimizados de acceso a datos.

#   Consideremos en nuestros ejemplos el DataFrame dataset que cargamso con el contenido del archivo "db.csv"
dataset=pd.read_csv('db.csv', sep=';')
print(dataset.head())