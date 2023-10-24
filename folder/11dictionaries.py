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

# Ahora crearemos un diccionario usando la funcion dict(), que nos premite proceder
# de diferentes formas por ejemplo, para crear un diccionario similar al anterior:

datos2 = dict(JettaVariant= 88078.64, Passat=106161.94, Crossfox=72832.16)

print('Esta es la segunda forma de hacer un diccionario: ', datos2)

# Aqui usaremos los pares clave-valor como si fuesen asignación de variable. En
# este caso debemos tener en cuenta las restricciones de nombres de variable del lenguaje python
# Otra forma de crear diccionarios en Python es con la combinacion de las fuciones
# zip() y dict(). Este metodo nos permite transformar pares de listas en diccionarios
# de forma bastante simple, para dar un ejemplo:

carros = ['Jetta Variant', 'Passat', 'Crossfox']
valores = [88078.64, 106161.94, 72832.16]

# Si utilizamos zip con estas dos listas tenemos como resultado un iterador que
# agrega los elementos de cada una de las listas en tuplas, de la siguiente forma:

datos3 = list(zip(carros, valores))
# Si pasamos este iterador como argumento de la funcion dict() tenemos como respuesta
# un diccionario que utiliza como claves el primer elemento de cada tupla y como
# valor el segundo de las mismas. Esto terminaria asi:

datosFinales = dict(datos3)

print('Este es el tipo de dato en el paso intermedio para crear un diccionario con zip y dict: ', type(datos3), 'y este es el tipo del ultimo paso con su construcción: ', type(datosFinales), datosFinales)