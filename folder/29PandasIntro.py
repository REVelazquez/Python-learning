# ----------- Porque usar la biblioteca Pandas para data science? ----------- 

#   Los proyectos de DS siempre envuelven algún tipo de conjuntos de datos, y
# por ende, debemos que explorar y tratar estos conjuntos de datos. Es alli
# donde Pandas entra en acción.
#   Pandas es un paquete Python que tiene estructuras de manipulación de alto 
# nivel, teniendo como base la biblioteca de NumPy. El paquete puede ser visto
# como una combinación de los recursos de manipulación de datos encontrados en
# planillas y bancos de datos relacionales con el alto desempeño de arrays del
# paquete NumPy.
#   Otro punto fuerte de Pandas es que sus estructuras de datos son fácilmente
# utilizadas por las principales bibliotecas de análisis del lenguaje Python.
#   Con estos puntos y teniendo en mente que preparación y tratamiento de datos
# son parte fundamental en un proceso de análisis de datos la biblioteca Pandas 
# se convierte en herramienta indispensable para un profesional de DS.

# ----------- Importando la biblioteca ----------- 

#   Se hara de la misma forma que se hace con  Numpy, por convención se acostumbra
# utilizar el pseudónimo pd para el namespace pandas, de la siguiente forma:

import pandas as pd

#   Para acceder a un recurso del paquete basta escribir el alias (pd) seguido del 
# carácter "." y después el nombre del recurso. El código de abajo imprime la versión
# del paquete pandas que estamos utilizando:
print(pd.__version__)

# ----------- Conociendo las estructuras de datos de Pandas ----------- 
# ------ Series ------ 
#   Son arrays unidimensionales etiquetados capaces de almacenar cualquier tipo de dato.
# Las etiquetas de las líneas son llamadas de "index". La forma básica de creación de una
# Series es la siguiente:

"s = pd.Series(datos, index=index)"

#   El argumento datos puede ser un diccionario, una lista, un array NumPy o una constante.

print(pd.Series(['Jetta Variant', 'Passat', 'Crossfox']))

#   Output:
# 0    Jetta Variant
# 1           Passat
# 2         Crossfox
# dtype: object

#   Cuando omitimos el parámetro "index" la Series queda apenas con el índice patrón que está
# compuesto por números enteros iniciados en cero. Adicionando el argumento "index" quedaría:

serie1=pd.Series(['Jetta Variant', 'Passat', 'Crossfox'], index=['Carro A', 'Carro B', 'Carro C'])
print(serie1)
#   Output:
# Carro A    Jetta Variant
# Carro B           Passat
# Carro C         Crossfox
# dtype: object

# ------ DataFrame ------ 
#   Es una estructura de datos tabular bidimensional con etiquetas en las líneas y columnas. Como las
# Series, son capaces de almacenar cualquier tipo de datos. La forma básica de creación de un DataFrame
# es la siguiente:

"df= pd.DataFrame(datos, index=index, columns = columns)"

# ------ Creación de un DataFrame a partir de una lista de diccionarios ------

#   Considere lo siguiente:

datos=[
    {'Nombre':'Jetta Variant', 'Motor':'Motor 4.0 Turbo', 'Año':2003, 'Kilometraje':44410.0, 'Cero_km':False, 'Valor':17615.73},
    {'Nombre':'Passat', 'Motor':'Motor Diesel', 'Año':1991, 'Kilometraje':5712.0, 'Cero_km':False, 'Valor':21232.39},
    {'Nombre':'Crossfox', 'Motor':'Motor Diesel V8', 'Año':1990, 'Kilometraje':37123.0, 'Cero_km':False, 'Valor':14566.43}
]

#   Con esta estructura de datos podemos crear un DataFrame de forma bastante simple, donde los valores
# de cada diccionario serán los registros del DataFrame(líneas) y las claves serán los labels de las columnas.

dataset=pd.DataFrame(datos)

print(dataset)

# El output será:

#           Nombre            Motor  ...  Cero_km     Valor
# 1         Passat     Motor Diesel  ...    False  21232.39
# 2       Crossfox  Motor Diesel V8  ...    False  14566.43

# [3 rows x 6 columns]

# ------ Creación de un DataFrame a partir de un diccionario ------

#   Otra forma es, pasando un diccionario, donde sus claves séran los labels de las columnas y los valores, en formato
# de listas, serán los registros de cada columna. El resultado sera idéntico al anterior

datos2={
    	'Nombre':	['Jetta	Variant',	'Passat',	'Crossfox'],	
		'Motor':	['Motor	4.0	Turbo',	'Motor	Diesel',	'Motor	Diesel	V8'],
		'Año':	[2003,	1991,	1990],
        'Kilometraje':	[44410.0,	5712.0,	37123.0],
		'Cero_km':	[False,	False,	False],
		'Valor':	[17615.73,	21232.39,	14566.43]
}

dataset2=pd.DataFrame(datos2)

print(dataset2)
# Output:
# Nombre              Motor  ...  Cero_km     Valor      
# 0  Jetta\tVariant  Motor\t4.0\tTurbo  ...    False  17615.73      
# 1          Passat      Motor\tDiesel  ...    False  21232.39      
# 2        Crossfox  Motor\tDiesel\tV8  ...    False  14566.43      

# [3 rows x 6 columns] las \t es para indicar a un programa de procesamiento de datos, como postgreSQl que hay un espacio

#   Creando un DataFrame a partir de un archivo externo

#   Una de la formas más utilizadas para creación de DataFrames es a partir de la importación de datos de archivos externos.
#   Nosotros nos enfocaremos en datasets almacenados en el formato csv, pero pandas ofrece soporte para importación de datos
# en diversos formatos.

#   La etapa inicial de todo proyecto en Data Science esta formada por algunos pasos: colecta e importación de los datos,
# identificación y entendimiento, transformación, tratamiento y resumen.

#   Para ello vamos a utilizar el conjunto de datos "db.csv" que contiene un conjunto de información sobre vehiculos anunciados
# para la venta. El mismo se encuentra en esta carpeta. Recordar que el material dentro de esta parte del repositorio 
# pertenece a un libro enunciado en el readme del repositorio

#   Para cargar el contenido de un archivo CSV en un DataFrame Pandas pone a disposición el método read_csv(). la forma más simple
# de utilización  de este método puede ser vista en el código de más abajo.

#   Donde pasaremos como primer parámetro el nobmre y localización del archivo CSV. Como nuestro archivo CSV está en la misma carpeta
#  del "notebook" que estamos utilizando, basta informar el nombre del archivo, suponiendo que esté dentro de una carpeta "data" y esta
# carpeta esté localizada en la misma carpeta de nuestro "notebook", la dirección deberá ser informada de la siguiente forma: './data/db.csv
# o 'data/db.csv'.

#   El parámetro sep informa que tipo de separador de columnas el archivo CSV está utilzando. El "default" de este parámetro es el carácter ","
# Cuando el archivo utilice otro tipo de carácter como separador de columnas, el parámetro sep debe ser configurado. En este caso utilzia el
# carácter ";" como separador.

dataset3=pd.read_csv('db.csv', sep=';') # Este nombre es  para no causar conflicto con el nombre que aparece antes que es dataset
dataset3.head()
print(dataset3) # Si bien el output es mas extenso pondre el resultado que da al hacer el print: [258 rows x 7 columns]

#   Este codigo lee el archivo y carga su contenido en un DataFrame de Pandas que recibe el nombre de dataset3. La última linea del código se
# utiliza la función head(), la cual  retorna las primeras "n" líneas de un DataFrame o Series. Esta funcionalidad es útil para verificar de 
# forma rápida si tu dataset posee el tipo ciertos de datos o si fue importado de forma correcta. Cuando esta función se utiliza sin parámetro
# genera una visualización de las cinco primeras líneas.