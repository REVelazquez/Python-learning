# Los diccionarios son diferentes a las listas. Son estructuras de datos que representan
# un tipo de mapeo, que se pueden entender como colecciones de pares calores, es decir,
# una clave(key) y un valor(value). Por lo que son similares a un objeto en JavaScript

# Creando un diccionario:
# Hay varias formas:
# diccionario= {'clave_1:valor_1, ..., 'clave_n': valor_n}
# diccionario= dict(clave_1=valor_1, ..., clave_n=valor_n)
# diccionario= dict(zip(iterable_1, iterable_2))
# Vamos a comenzar con un diccionario simple para dar un ejemplo. Supongamos que 
# queremos crear un mapeo donde tenemos como clave los nombres de los vehiculos de
# nuestro dataset y como valores los precios de venta de cada vehiculo:

datos={'Jetta Variant':88078.64, 'Passat':106161.94, 'Crossfox':72832.16}

print(datos, 'Su tipo de dato es: ', type(datos))