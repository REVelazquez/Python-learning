# Creando funciones:

# Este recurso es bastante útil en programación pues nos permite nombrar unidades de
# código haciendo nuestro programa más facil de leer y depurar. Usar funciones también
# permite eliminar el código repetitivo, posibilitando la reutilización de código de forma
# limpia y simple en otras partes de nuestro programa.

# Funciones sin argumentos:
# Para definir una función, en su forma más simple, necesitamos apenas espedificar un nombre
# y una secuencia de instrucciones que serán ejecutadas cuando la función es llamada

# Formato patrón:

# def <nombre>():
#     <instrucciones>

# En Python, las funciones son definidas con la instrucción "def" seguida del nombre escodigo para 
# la función. Debemos evitar tener una función y una variabe con el mismo nombre en el códifo.

# Despues del nombre de la función utilizamos los paréntesis (), que cuando están vacíos indican que 
# se trata de una funcion sin argumentos. La primera linea de la definición de una función termina con el
# uso del carácter ":" y luego en la siguiente línea tenemos las instrucciones que necesitan ser indentadas,
# asi como en los bucles for. Veamos un ejemplo a continuación:

def media():
    valor = (1+2+3)/3
    print (valor)

# Note que no hay nungun retorno de la ejecución de dicha función. Este código apenas crea un objeto de
# función del tipo function. Para llamar la función media() utilizamos la misma sintaxis de las build.in functions

media()