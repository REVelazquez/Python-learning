# Porque usar numpy para data science?

#   NumPy, abreviación de Numerical Python, es una de las bibliotecas mas importantes para procesamiento numérico
# en Python, ofreciendo la base para la mayoría de otras bibliotecas de aplicaciones científicas que utilzian datos
# numéricos en el lenguaje. Podemos destacar los siguientes recursos:

# - Un poderoso objeto array multidimensional;
# - Funciones matemáticas sofisticadas para operaciones con arrays sin la necesidad de utilización de bucles "for"
# - Recursos de álgebra lineal y generación de números aleatorios

#   Fuera de los recursos numéricos y de procesamiento eficiente de arrays, esta biblioteca tambien actua como contenedor
# para transporte de datos multidimensionales entre algoritmos y diversas bibliotecas del lenguaje. En la manipulacón y 
# almacenamiento de datos numéricos, los arrays NumPy son significativamente más eficientes que las estructuras básicas 
# de datos de Python

#   Si bien no ofrece funcionalidades específicas del área de análisis de datos como herramientas de modelaje estadístico,
# es importante saber como trabaja con arrays NumPy y el procesamiento orientado a arrays ya que nos permitira entender más
# fácilmente las herramientas con semántica orientada a arrays, como seria Pandas.

# --------- Importanto toda la biblioteca ------------

#   Python posee una biblioteca patrón que viene con un conjunto de herramientas importantes para atender una amplia variedad
# de tareas. Algunas de ellas serian las built- in functions.

#   Ademas nos permite tener acceso a un amplio ecosistema de herramientas y bibliotecas de terceros que amplían las 
# funcionalidades del lenguaje para áreas y tareas más específicas, como es el caso de la biblioteca NumPy.

#   Para cargar módulos de la biblioteca patrón o de terceros en nuestro proyecto  basa utilizar la declaración "import" seguida 
# del nombre que identifica la biblioteca de interés. En el caso del paquete NumPy seria de la siguiente forma:

# import numpy---> comentado para que no genere errores

# Con esta declaración estamos importando todo el contenido de la biblioteca NumPy en nuestro proyecto y para acceder a cualquier 
# recurso del paquete necesitamos utilizar el nombre del módulo seguido del carácter "." y después el nombre del recurso:

# print(numpy.arange(10)) --->comentado para que no genere errores

# ----------- Importando parte de la biblioteca -----------

#   Es posible también importar alfunos recursos específicos de una biblioteca en vez de importar todo su contenido. Para eso basta 
# utilizar la declaración "from" en conjunto con la declaración "import", de la siguiente forma:

# from numpy import arange --> comentado para evitar errores

# Hacer esto nos permite lo siguiente:

# print(arange(10)) ----> comentado para evitar errores

#   Este método debe ser utilizado con cautela pues puede sobrescribir nombres de funciones no namespace de nuestro proyecto. Un namespace
# es, básicamente, un sistema para garantizar que todos los nombres en un programa sean exclusivos y puedan ser usados sin ningún comflicto

# ------------ Importando toda la biblioteca y atribuyendo un nuevo nombre --------

#   Una práctica bastante común a la hora de realizar el "import" de un paquete es atribuir un alias al mismo. Por convención la comunidad
# acostumbra utilizar el seudónimo np para el namespace numpy, de la siguiente forma:

import numpy as np

#   Una vez  hecho esto, basta digitar el alias (np) seguido del carácter '.' y después el nombre del recurso.

print(np.arange(10))
