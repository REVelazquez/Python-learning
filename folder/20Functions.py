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

# Ahora, una vez que llamamos a la función, esta nos devolvera el valor calculado previamente.

# Funciones con argumentos:

# Algunas funciones exigen uno o más argumentos para pdoer ejecutar sus instrucciones. Esos pueden ser obligatorios u
# opcionales.

# Formato patrón:
# def <nombre>(<arg_1>, <arg_2>, ..., <arg_n>):
#     <instrucciones>

# Estos argumentos obligatorios no vienen previmante configurados, o sea, con un valor default, por eso
# necesitan ser especificados cuando la función es llamada. Veamos un ejemplo de función que recibe argumentos.

def media2(valor_1, valor_2, valor_3):
    valor= (valor_1 + valor_2 + valor_3)/3
    print("La media es", valor)

# La funcion media2() tiene tres argumentos y necesitan ser informados siempre que la funcion es llamada, o sea,
# son obligatorios.

media2(2, 5, 8)

# Esta función es ahora una que necesita tener tres argumentos obligatorios si llamamos esa función y pasamos menos de
# tres argumentos o más de tres ocurrirá un error. Para tener un argumento "default" deberiamos defifnirlos a la hora de 
# definir la función, por ejemplo, reemplazando 'valor_3' por 'valor_3=3'. En este caso el tercer valor siempre estaria definico 
# como "3".

# Pero a la vez podriamos llamar la misma funcion con tres argumentos y asignar un nuevo valor para el ultimo argumento,
# lo que cambiaria el valor default por este otro nuevo que nosotros definimos.

