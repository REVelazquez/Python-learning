# Ahora conoceremos uno de las principales construcciones de loops de Python. 

# For
# Este bucle comienza con el encabezado que define una variable de destino para cada ítem de la iteración (),
# juntamente con el objeto que será recorrido (). Después del encabezado sigue el bloque de instrucciones
# identado. Veamos un ejemplo

for i in range(1, 11):
    print (i ** 2)

# Este es un loop simple.


# Loops con secuencias:
# En las secuencias se puede iterar por los ítems con el uso de los bucles for. Tengamos en cuenta la
# siguiente lista para nuestro ejemplo:

accesorios=['Llantas de aleación', 
            'Cerraduras eléctricas',
            'Piloto automático',
            'Bancos de cuero', 
            'Aire acondicionado', 
            'Sensor de estacionamiento', 
            'Sensor crepuscular', 
            'Sensor de lluvia']

# En la siguiente sentencia el nombre "item" es asignado a cada elemento de la lista accesorios y la instrucción
# print es ejecutada para cada uno:

for item in accesorios:
    print (item)

# Ahora, supongamos que tenemos un conjunto de datos sobre vehiculos organizadas en listas. La variable "datos"
# que tenemos a continuacion es una lista con datos sobre los vehículos. Tengamos en cuenta que la estructura sera:
# item de la lista: nombre del vehiculo, año de fabricación, vehículo cero km o no.

datos=[
    ['Jetta Variant', 2003, False],
    ['Passat', 1991, False],
    ['Crossfox', 1990, False],
    ['DS5', 2019, True],
    ['Aston Martin DB4', 2006, False],
    ['Palio Weekend', 2017, False],
    ['A5', 2019, True],
    ['Série 3 Cabrio', 2009, False],
    ['Dodge Jorney', 2018, False],
    ['Carens', 2011, False],
]

# En este caso siendo que cada item de datos es una lista, podemos especificar si queremos acceder a un elemento 
# mediante el operador de indexación []. En el siguiente ejemplo veremos que ocurre cuando hacemos esto con la lista anterior.
# Ej:
for item in datos:
    print(item[0])

# De esta forma podemos definir, por ejemplo, si un auto es nuevo o no agregando solamente un condicional dentro del loop:

for item in datos:
    if(item[1] >= 2019):
        print('Vehiculo nuevo')
    elif(item[1] > 2016 and item[1]<= 2018):
        print('Vehiculo seminuevo')
    else:
        print('Vehiculo usado')

# Loops con diccionarios

# Estas iteraciones pueden ser hechas a partir de métodos específicos. Abajo hay algunos metodos soportados por diccionarios Python
# que nos ayudan en la hora de hacer iteraciones. En la tabla la letra "d" representa un diccionario cualquiera:

#       Operaciones     |       Resultado
#       d.keys()        |       Retorna una nueva visualización de las claves del diccionario.
#       d.values()      |       Retorna una nuva visualización de los valores del diccionario.
#       d. items()      |       Retorna una nueva visualizacion de los pares (clave, valor) del diccionario

# En el siguiente codigo se construye un nuevo diccionario que tiene como claves los nombres de los vehículos y como valores el valor
# de venta de cada uno

data={
    'Crossfox':72832.16,
    'DS5': 124549.07,
    'Volkswagen': 150000,
    'Jetta Variant': 88078.64,
    'Passat': 106161.95
}

# El método keys() retorna una nueva visualizaci'on de las claves de un diccionario. Observe el código de abajo:

# print(data.keys()) <-- esto fue comentado para que no cree repeticiones en la consola

# de esta forna podemos acceder a las claves de un diccionario y tambien acceder a sus valores:

for clave in data.keys():
    print( 'El precio de ', clave, ' es ', data[clave])

# values funciona de forma similar solo que con los valores de los vehículos, veamos que ocurre en el siguiente caso:
