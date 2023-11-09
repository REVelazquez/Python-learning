# Las list comprehensions, son un recurso de Python que permite la creacion de una nueva lista de forma más concisa.

# Formato patrón:

# [ <expresión> for <item> in <iterable> if <condición> ]

# Este formato es equivalente al siguiente bucle:

# lista= []
# for <item> in <iterable>:
#     if <condición>:
#         lista.append(<expresión>)

# Podemos tener algunas variaciones en este formato, pero la idea básica continúa siendo la de permitir la creación de listas
# de manera concisa(apenas una línea de código) con la aplicación de filtros y transformaciones en los elementos.
# Por ejemplo, el siguiente bucle for crea la lista "cuadrado" conteniendo los elementos del iterable range(10) elevados al cuadrado.

cuadrado=[]
for i in range(10):
    cuadrado.append(i**2)

print(cuadrado)

# a esto lo podemos hacer de la siguiente forma:

cuadrados= [i**2 for i in range(10)]
print(cuadrados, ' Esto fue hecho con List comprehension')

# Un segundo ejemplo seria el siguiente, donde vamos a crear la misma linea del código anterior apenas para los números pares del iterable range(10).
# Para esto necesitamos incluir una cláusula if para probar si el número es par o no.

cuadrado_pares = []
for i in range(10):
    if(i % 2 == 0 ):
        cuadrado_pares.append(i **2)

print(cuadrado_pares)

# Ahora veamos con list comprehension:

cuadrados_pares= [ i**2 for i in range(10) if (i % 2 == 0)]

print(cuadrados_pares, 'Esto fue hecho con List Comprehension')

# If, elif y else en un List Comprehension:
# En algunos casos necesitamos verificar y tratar mas de una condicion durante la construcción de una lista. Para ello usamos las instrucciones
# if-elif-else. Con list comprehension es posible utilizar este tipo de estructura condicional. Veamos un ejemplo.

datos= [
    ['Jetta	Variant',	2003,	False],
	['Passat',	1991,	False],
	['Crossfox',	1990,	False],
	['DS5',	2019,	True],
	['Aston	Martin	DB4',	2006,	False],
	['Palio	Weekend',	2017,	False],
	['A5',	2019,	True],
	['Série	3	Cabrio',	2009,	False],
	['Dodge	Jorney',	2018,	False],
	['Carens',	2011,	False]
]

# Ahora utilizando estructuras condicionales creamos un clasificador simple con el siguiente código:

estado1=[]
for item in datos:
    if(item[1] >= 2019):
        estado1.append('Vehiculo nuevo')
    else:
        estado1.append('Vehiculo usado')

print(estado1)

# ahora para hacerlo con list Comprehension:

tipo = ['Vehiculo nuevo' if (item[1] >= 2019) else 'Vehiculo usado' for item in datos]

print ('Lista creada con list comprehension: ', tipo)

# En el caso de usar un elif, en el primer codigo habria que agregar dos lineas, las mismas contendrian lo siguiente:

# elif(item[1] > 2016 and item[1] <= 2018):
#       estado1.append('Vehiculo seminuevo')

# esto no se aplica nuevamente para no enseñar mayor cantidad de datos en la terminal.

# en la list comprehension seria de la siguiente forma:

# tipo = ['Vehiculo nuevo' if (item[1] >= 2019) else 'Vehiculo seminuevo' if (item[1] > 2016 and item[1] <2018) else 'Vehiculo usado' for item in datos]

# en este caso ambos codigos darian el mismo resultado: la lista anterior con el agregado de tener una variacion 
# en aquellos objetos donde el año del modelo sea entre 2016 y 2019

# Tambien es posible utilizarle en bucles anidados, como por ejemplo:

# Estructura patrón
# Bucle aninado:

# for lista in datos:
#     for item in lista:
#         accesorios.append(item)

# List Comprehension:

# [item for lista in datos for item in lista]

# Lo cual, como podemos ver, reduce mucho la cantidad de lineas a utilizar.

# De esta forma podemos usar el recurso de "list comprehension" para hacer un codigo simple en uno que sea
# conciso y de fácil lectura, también impactando en el perfonmance cuando es comparado con los bucles
# for equivalentes.