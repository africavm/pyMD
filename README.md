# This is a project that deals with MD for inelastic disks, in python
# 02/03/2018


## Resumen programa

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