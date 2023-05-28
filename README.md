# This is a project that deals with MD for inelastic disks, in python
# 02/03/2018


## Práctica 1
## Resumen del programa

En primer lugar, se importan las librerías necesarias. A continuación se declaran los parámetros que describen el sistema a estudiar y se inicializan los vectores de las posiciones y las velocidades de las partículas y las listas que contendrán la información sobre las colisiones.

La segunda parte del programa consiste en las definiciones de las funciones que se van a utilizar para modelar el sistema. Las funciones que se definen son las siguientes:
1. propaga: avanza el estado de las partículas en un tiempo dt.
2. midedist: mide las distancias entre las partículas.
3. tcol: mide el tiempo de colisión entre cada par de partículas.
4. tpcol: mide el tiempo de colisión entre las partículas y las paredes del sistema.
5. pcolisiona: actualiza las velocidades de una partícula que colisiona con la pared.
6. colisiona: actualiza las velocidades de dos partículas que colisionan entre sí.
7. write_micr_state: escribe las posiciones y las velocidades de las partículas en cada estado en un fichero.
8. initialize_random: inicializa las partículas con velocidades y posiciones aleatorias.
9. calculate_average: mide la temperatura media del sistema.
10. write_averages_evol: escribe en un fichero los resultados de calcular la temperatura media en cada estado.

Por último, se hace uso de las funciones para simular la evolución del sistema. Para ello, se imprimen por pantalla los parámetros elegidos para el sistema y después se inicializa este de forma aleatoria haciendo uso de la función initialize_random. Posteriormente se usan bucles anidados que, haciendo uso de las funciones definidas van calculando la evolución del sistema y escribiéndolas en un fichero en cada paso. 
 
## Cambios introducidos (18/05/2023)

1. Modificación del método de inicialización de los vectores utilizando la función np.zeros que crea directamente un vector de ceros de la dimensión deseada.

2. Modificación del algoritmo de escritura para que los microestados se escriban en un único fichero. Para saber que datos corresponden a cada estado se añade una tercera columna en el fichero que indica el número del estado. Puesto que ahora en los ficheros se escribe mediante el argumento "append" en lugar de write, al principio del programa se han añadido unas líneas de código que a través de la librería "os" hace que cuando se ejecute el programa de nuevo se borren de los ficheros los datos de las ejecuciones anteriores.

3. Modificación del código de gnuplot para que represente los datos contenidos en un único fichero. Se utiliza un bucle que en cada iteración representa las partículas en cada uno de los estados.

## Práctica 2: Análisis de propiedades dinámicas del sistema (28/05/2023)

En esta práctica vamos a realizar un estudio de las propiedades dinámicas de nuestro sistema. En primer lugar, para poder estudiar adecuadamente las propiedades, aumentamos el número de partículas y el tamaño del sistema del programa original. Creamos un nuevo script en el que se calcularán, a partir de los ficheros generados con la información del sistema, las diferentes propiedades dinámicas.

Al comienzo del script almacenamos los datos obtenidos mediante la simulación realizada con MD_numpy, contenidos en los ficheros ".dat", en matrices. Inicialmente tenemos 4 vectores, dos para las componentes de la velocidad y dos para las componentes de la posición. Dividimos estos vectores en matrices para poder ver mejor los datos. Cada una de las columnas de las matrices representa la componente de cada partícula en un estado. Por ejemplo, la primera columna de la matriz "x_matrix" representa la coordenada x de todas las partículas del sistema en el primer estado. También almacenamos las temperaturas contenidas en el fichero temp.dat en la variable "T".

Una vez que hemos importado los datos correctamente, pasamos a realizar el estudio de las propiedades dinámicas del sistema. En primer lugar, estudiamos cuál es la velociad media de las partículas. Para ello, puesto que queremos las componentes de la velocidad y no el módulo de esta, hacemos uso de la librería numpy para calcular la media de los vectores vx y vy e imprimimos el resultado por pantalla. Podemos ver que el resultado obtenido es el esperado ya que obtenemos valores muy próximos a cero para cada coordenada.

A contirnuación calculamos el módulo de la velocidad al cuadrado y, obteniendo que el módulo de la velocidad al cuadrado es 2,1. Esto también está de acuerdo con lo esperado, ya que este valor debe ser distinto de cero. Calculamos también el valor medio del módulo de la cuarta potencia de la velocidad con el fin de calcular el coeficiente de kurtosis de la distribución de velocidades. Obtenemos que nuestro coeficiente de kurtosis es positivo, lo que significa, como queda reflejado en el gráfico, que nuestra distribución tiene carácter leptocúrtico.

Vamos ahora a comparar la distribución de velocidades de las partículas de nuestro sistema con la función de Maxwell. Definimos entonces la función de maxwell y la representamos frente al histograma que obtenemos a partir de los datos del modulo de las velocidades de nuestras partículas. Para hacer la representación utilizamos las funciones "hist" y "plot" de la librería matplotlib. La figura que obtenemos es la siguiente:

<image src="Figura 1.png" alt="Figura 1: Distribución de velocidades">

Vemos que la distribución de velocidades que hemos obtenido a partir de la simulación coincide bastante bien con los valores teóricos esperados.

Por último, calculamos la función de autocorrelación para varios intervalos. Para ello, en cada paso vamos aumentantando el número de saltos temporales y calculamos los coeficientes de autocorrelación de cada partícula. Después obtenemos la media de todas las partículas para cada paso y guardamos este valor en un vector. Si representamos gráficamente obtenemos la siguiente figura:

<image src="Figura_2.png" alt="Figura 1: Coeficiente de autocorrelación de velocidades">

Vemos que el coeficiente parte de 1 y decae hasta valores muy próximos a 0 en 200 desplazamientos. Podemos concluir entonces que a los 200 desplazamientos temporales prácticamente todas las partículas del sistema han modificado su velocidad.