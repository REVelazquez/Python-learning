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

print(df) # Output [3 rows x 6 columns]
print(df.index) #Output RangeIndex(start=0, stop=3, step=1)

#   Index
#   Al crear una Series o un DataFrame la secuencia de etiquetas que fue utilizada en la construcción de estos objetos
# será internamente convertida en un Index

#   Pandas soporta valores de índice no exclusivos, pero caso una operacón que no soporta valores duplicados de índice sea
# ejecutada, una excepción será generada.

df = pd.DataFrame(datos, index=['A', 'B', 'C'])
print(df)