# Definiendo funciones que retornan valores.

# Considerando la ultima definición de la función media() que utilizamos en la sección anterior. Como podemos ver en el
# código de abajo esta funcion recibe una lista de valores, calcula la media aritmética de estos valores y despues imprime
# el resultado de esta media para el usuario.

def media(lista):
    valor = sum(lista)/len(lista)
    print(valor)

media([1, 2, 3, 4, 5, 6, 7, 8, 9])

# Ahora supongamos que estamos interesados en utilizar el resultado de la media en otro lugar del codigo. Se podria pensar que
# para ello bastaria asignar el valor de la función media() a una variable y luego utilizar esta variabel en otar parte del código.

# Sin embargo cuando accedemos al a variable esta no retorna el resultado de la operación. Funciones como esta son conocidas como
#  funciones nulas, pues pueden exhibir algún resultado en la pantalla, pero no tienen un valor de retorno.

# Funciones que retornan un valor.

# para definir una función con retorno utilizamos la instrucción return y pasamos el resultado que deseamos que la función retorne.
# Ejemplo de formato:

# def <nombre> (<arg_1>, <arg_2>, ..., <arg_n>):
#     <instrucciones>
#     return <resultado>

# Vamos entonces a definir nuevamente nustra función para el cálculo de las medias, solo que ahora retornando el resultado y no apenas
# imprimiendo:

def media2(lista):
    valor = sum(lista) / len(lista)
    return valor

# La función continua funcionando como antes, solo que ahroa podemos asignar su resultado a una variable o hasta mismo llamarla dentro 
# de una expresión u otra función

# Metodos de string:

# lower() y upper()
# Estos dos modifican las cadenas de texto, o strings, para que todos los caracteres se encuentren en minusculas o
# mayúsculas, respectivamente, esto es debido a que unicode tiene un codigo diferente para la "A" y "a", por ello es
# que str.lower() transforma todos los strings en minúscula y el medoto str.upper() los transforma a mayúsculas.

