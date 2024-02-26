import pandas as pd

#   Objetos Index

#   Pandas posee un conjunto de objetos Index que son responsables por el almacenamiento de las etiquetas
# de los ejes de Series y DataFrames.  Estos pueden guardar otros metadatos, como serian los nombres de los ejes.

#   RangeIndex
#   Es el tipo de índice patrón utilizado por el DataFrame y Series cuando ningún índice explícito es dado por el 
# usuario

datos = {
    'Nombre':	['Jetta	Variant',	'Passat',	'Crossfox'],	
    'Motor':	['Motor	4.0	Turbo',	'Motor	Diesel',	'Motor	Diesel	V8'],
    'Año':	[2003,	1991,	1990],
    'Kilometraje':	[44410.0,	5712.0,	37123.0],
    'Cero_km':	[False,	False,	False],
    'Valor':	[17615.73,	21232.39,	14566.43]
}

df=pd.DataFrame(datos)

print(df) # Output [3 rows x 6 columns] <-- aqui hay mas código antes
print(df.index) #Output RangeIndex(start=0, stop=3, step=1)

#   Index
#   Al crear una Series o un DataFrame la secuencia de etiquetas que fue utilizada en la construcción de estos objetos
# será internamente convertida en un Index

#   Pandas soporta valores de índice no exclusivos, pero caso una operacón que no soporta valores duplicados de índice sea
# ejecutada, una excepción será generada.

df = pd.DataFrame(datos, index=['A', 'B', 'C'])
print(df)

#   Objetos index no pueden ser modificados por el usuario, o sea, son inmutables.
# df.index[1]= 'H'  #   Si esta línea se descomenta dara un error el codigo

#   Definiendo como índice una de las columnas existentes.

#   Utilizando el método set_index() es posible definir un índice para un DataFrame utilizando como etiquetas los valores de
# una o más columnas del propio DataFrame. Considere el DataFrame anterior para el siguiente ejemplo:

df.set_index('Nombre')

#   En este ejemplo fueron utilizados los valores de la columna 'Nombre' como etiquetas para las lineas de nuestro DataFrame. El
# método set_index() posee un parámetro llamado "drop" que viene configurado como True por default. Este parámetro indica si la 
# columna utilizada como nuevo índice debe permanecer( drop=False) o ser retirada del DataFrame(default)

#   Cuando utilizamos métodos de Series y Dataframes se hace sobre el parámetro inplace. Este aparece en buenaparte de los métodos
# que utilizaremos y viene configurado como False por default. El mismo informa si el objeto debe ser modificado in-place(True) o no
# (default). Cuando "inplace" es False apenas una visualización del objeto es creada, permaneciendo inalterado. Cuando accedemos al
# índice del DataFrame df no encontramos las modificaciones que fueron hechas, porque el parametro "inplace" se mantuvo con su 
# configuración default(False)

print(df.index)

#   Para poder modificar el DataFrame basta configurar "inplace" como True en el m'etodo set_index().

df.set_index('Nombre', inplace=True)

print(df.index)