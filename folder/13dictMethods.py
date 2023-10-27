# Métodos de diccionarios

# En la siguiente tabla muestra algunos métodos soportados por diccionarios Python. En la tabla
# la letra d representa un diccionario cualquiera, 'key' es la clave de un ítem especifíco del
# diccionario y puede ser cualquier tipo de inmutable y 'value' es un valor de ítem especifico
# del diccionario.

#   Operaciones             |   Resultado
#   d.clear()               |   Elimina todos los ítems del diccionario.
#   d.copy()                |   Crea una copia del diccionario.
#   d.pop(key[, default])   |   Si la clave(key) es encontrada en el diccionario, el ítem es 
#                           |   eliminado y su valor es retornado. Caso contrario, el valor 
#                           |   especifícado como default es retornado. Si el valor "default" no es
#                           |   pasado y la clave no fue encontrada un error será generado.
#   d.get(key[, default])   |   Retorna el valor correspondiente a la clave "key". Caso contrario, el
#                           |   valor especificado como 'default' es retornado. Si el valor 'default'
#                           |   no fuera pasado y la clave no fuera encontrada, el método retorna
#                           |   None, o sea, este método nunca retorna error.
#   d.update()              |   Actualiza el diccionario.

# Pongamos algunos ejemplos a continuacion

# d.clear()

# Para eliminar todos los items de un diccionario utilizamos el método clear (). ej:
datos={'Jetta Variant':88078.64, 'Passat':106161.94, 'Crossfox':72832.16}

print(datos.clear())

# d.copy()

# Funciona de la misma forma que el "copy()" de secuencias solo que con diccionarios
datos2= {'Jetta Variant':88078.64, 'Passat':106161.94, 'Crossfox':72832.16, 'DS5':124549.07}

datos3=datos2.copy()
print(datos2, datos3)

# d.pop(key[, default])

# El metodo pop() elimina del diccionario el ítem especificado por la clave (key). Si la clave fuera encontrada,
# el ítem es eliminado y su valor es retornado. Caso contrario es retornado el valor especificado como default.

print (datos3.pop( 'DS5'))

# si el valor default no es pasado y la clave no es encontrada en el diccionario, se generara un error:
# en este caso debemos usar el valor de retorno para cuando la misma no es encontrada
print( datos3.pop('Fiat', 'Clave no encontrada'))
# se puede probar sin el valor de retorno, pero solamente lanzara un error en consola

# d.get(key[, default])
# Este metodo nos retorna el valor correspondiente a la clave "key". Caso contrario se retorna default
# si bien no retorna un error siempre podemos agregar el valor de retorno
print(datos.get('Ds5x', 'clave no encontrada'))

# d.update()
# este metodo nos permite actualizar total y parcialmente un diccionario
# podemos agregar un nuevo ítem, actualizar uno existente y agregar uno nuevo, como veremos en el ejemplo:

datos2.update({'Passat':96161.95, 'Volkswagen':50000})
# A su vez podemos utilizar asignacion en vez de puntos como se hizo previamente.
# Recordando claro las reglas de formación de nombre de variables de Python.

print(datos2)
