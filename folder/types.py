#Tipo string   

strings= 'abcdef'

print(type(strings))

#Tipo int

integrer=20000

print(type(integrer))

#Tipo float

decimales=45.5

print(type(decimales))

#booleans

falso= False

verdadero=True

print(type(verdadero), type(falso))

#None: el tipo "None" funciona como en null en otros idiomas.

cero= None
print(type(cero))

#Conversion de tipos:
#si queremos operar un tipo string con un tipo "int" simplmente con el operador de suma(+) nos dara un type error, por ello es necesario
#que utilicemos las funciones para transformarlos, tomemos por ejemplo lo siguiente

ex1= 'Hola '
ex2= 'Mundo'
ex3=  20
ex4=  23  
#si juntamos por ejemplo "ex1 + ex2" se formara una frase, sin embargo si queremos agregar una de las otras variabales nos dara error

print('ejemplo 1: '+ex1+ex2)
#por ello para poder utilizarles deberemos usar las funciones integradas de python como por ejemplo str

print('ejemplo  2: '+ ex1+ex2 + ' '+ str(ex3)+str(ex4))

#algunas otras funciones son: int() para transformar un float a un entero, float() y bool()
#veamos un ejemplo

print(type(bool(ex1))) #nos devolvera que el tipo cambio a booleano

ex5=22.23

print(int(ex5), ', antes de la conversion ', type(ex5), 'despues de la conversion', type(int(ex5)))

#Formato de strings
#El metodo format() del objeto str ejecuta una operacion de formato en un string. El string
# en el cual este metodo es llamado puede contener texto literal o campos de sustitición delimitados por llaves {}
# ejemplo:

ejemplo= 'Hola, {}'
ejemplo2= 'Hola, {}. Esta es tu nota: {}'

arrayFormat= ['Rodrigo', 'Juan', 8, 7.25]

print(ejemplo.format('Rodrigo'))
print(ejemplo.format(arrayFormat[1]))

#o bien agregamos dos argumentos al format:
print(ejemplo2.format('Rodrigo', 8))
print(ejemplo2.format(arrayFormat[1], arrayFormat[3]))
#Este metodo esta devolviendo una copia del string con los cambios hechos por el metodo format

# f-Strings: es un string literal que tiene como prefijo la letra f o F. Tambien puede tener campos de
#sustitucion como en el anteior, es decir {}. Pero estos pueden ser llenados por cualquier variable del programa
#ejemplo:




