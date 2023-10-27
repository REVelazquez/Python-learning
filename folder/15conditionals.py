# Estructuras condicionales y de Repetición.

# Instruccion "if"
# Como en otros idiomas, el "if" se utiliza para verificar una condicion y luego pasos a seguir si esta es True o False.

# los siguientes son los operadores que existen:

# Operadores de comparación:

#       Operador        |       Descriptión
#       ==              |       Igualdad
#       !=              |       Diferencia
#       >               |       Mayor que
#       <               |       Menor que
#       >=              |       Mayor o igual
#       <=              |       Menor o igual

# Operadores lógicos:

#       Operador        |       Descriptión
#       and             |       Y
#       or              |       O
#       not             |       Negación

# Comencemos utilizando algunos de los operadores de comparacion, veamos el siguiente ejemplo que
# representara el año de fabricación de un vehículo:

anho= 2018

# ahora buscaremos responder la pregunta: "Anho es mayor o igual a 2019?" Evidentemente la respuesta sera
# que no es verdadera por lo tanto la respuesta sera un False. Ahora llevmos esto a la logica de programación:

if(anho >= 2019):
    print('Vehiculo nuevo')

# A la hora de revisar en la consola, dicho mensaje no aparecera al no cumplir con la sentencia.

# if-else y if-elif-else

# En algunas situaciones puede ser necesaria alguna acción específica para el caso contrario en una instrucción
# 'if, es decir cuando la condicion no retorna True, como en el anterior caso. Para ello utilizamos 'else' que 
# nos dara ejecutarlas cuando dicha condicion retorna False.

if(anho >= 2019):
    print ('Vehiculo nuevo')
else:
    print ('Vehiculo seminuevo')

# Hay que tener en cuenta que si cambiamos la variable anho a, por ejemplo, 2020 la consola nos repetira 2 veces
# el mensaje para cuando la sentencia es "True"

# En el caso de que haya una segunda condición se deberia utilizar "elif" antes de un else, esta estructura es una
# union de "else" y "if" que puede ser utilizada una o mas veces dentro de una estructura condicional. Antes de poder 
# dar un ejemplo de esto debemos revisar los valores de los operadores logicos

# Tabla verdad - operador lógico AND

#       A       |       B       |       A and B
#       True    |       True    |       True
#       True    |       False   |       False
#       False   |       True    |       False
#       False   |       False   |       False

# En el caso de "AND" si no tiene un doble "true" la respuesta siempre sera false

# Tabla verdad - operador lógico OR

#       A       |       B       |       A or B
#       True    |       True    |       True
#       True    |       False   |       True
#       False   |       True    |       True
#       False   |       False   |       False

# En este caso el unico que sera falso es cuando las dos condiciones sean falsas.

# Ahora tomemos por ejemplo la siguiente construcción para esta construcción:

anho2= 2017
#aqui puedes cambiar los valores de anho2 para ver diferentes respuestas
if(anho2 >= 2019):
    print('Vehiculo nuevo')
elif(anho2 > 2016 and anho2 <= 2018):
    print('Vehiculo seminuevo')
else:
    print('Vehiculo usado')
