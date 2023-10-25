# Operaciones con diccionarios.

# Asi como las listas, los diccionarios tambien soportan un conjunto de operaciones
# estas estaran listadas debajos, siendo "d" un diccionario cualquiera, "key" es la
# clave de un ítem especifico del diccionario y puede ser de cualquier tipo inmutable
# y "valor" es el valor de un ítem especifico del diccionario

#   Operaciones     |       Resultado
#   d[key]          |   Retorna el ítem del diccionario "d" correspondiente a la clave "key"
#   key in d        |   Retorna "True" si el diccionario "d" tiene un ítem con la clave "key"
#   len (d)         |   Asigna el valor "value" a la clave "key" del diccionario "d"
#   D[ley]=value    |   Asigna el valor "value" a la clave "key" del diccionario "d"
#   del d[key]      |   Elimina el ítem con la clave "key" del diccionario "d"

# Para estos ejemplo utilizaremos el siguiente diccionario:

datos={'Jetta Variant':88078.64, 'Passat':106161.94, 'Crossfox':72832.16}

# D[KEY]
# Para acceder a un valor específico de un diccionario "d" basta informar para el
# operador [] la clave (key) del ítem. En el siguiente codigo vamos a acceder al
# valor de venta del vehículo "Passat"

print ('Este es el valor de la key Passat: ', datos['Passat'])

# key() in d
# El operador "in" también funciona con diccionarios cuando queremos verificar la existencia
# de una determinada clave(key). La línea del código "key in d" retorna True si la 
# clave(key) se encuentra en el diccionario "d". Ejemplo:

print('Se encuentra Passat en datos?: ', 'Passat' in datos)
# Si se usa "not" tambien se puede utilizar para hacer la verificacion contraria

print('No se encuentra Crossfox en datos?: ', 'Crossfox' not in datos)

# len(d)
# esta funcion retorna el numero de ítems del diccionario, es decir la cantidad de 
# pares clave-valor

print('El diccionario tiene ', len(datos), ' ítems')

# D[KEY]=VALUE
# Esta es una forma de incluir un nuevo clave-valor en el diccionario:
datos['DS5']=124549.07

print('', datos)

# del d[key]
# Para exluir un ítem de un diccionario podemos utilizar el comando "del" y luego
# especificar el diccionario y la clave que queremos eliminar

del datos['Passat']

print('Este es el diccionario luego de borrar un valor: ', datos)