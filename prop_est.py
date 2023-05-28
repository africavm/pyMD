import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm
from scipy.spatial import Delaunay,Voronoi, voronoi_plot_2d
from matplotlib.animation import FuncAnimation


##################################################################################################################
# ESTUDIO DE LAS PROPIEDADES ESTRUCTURALES DEL SISTEMA


# ¡CUIDADO! Para que el programa funcione correctamente el número de partículas tiene que ser el mismo que en MD_numpy
particulas=50

# Leemos el fichero que contiene las posiciones de las partículas
posiciones = np.loadtxt('xy.dat', usecols=(0, 1), unpack=True)

# Almacenamos los datos de las posiciones en dos vectores diferentes
x = posiciones[0]
y = posiciones[1]

num_estados=int(len(x)/particulas)

# Construimos matrices para que cada columna de la matriz represente las posiciones de las n particulas en un estado
x_matrix = np.zeros((particulas, num_estados))
y_matrix = np.zeros((particulas, num_estados))

for i in range(num_estados):
    columnax = x[i * particulas: (i + 1) * particulas]
    columnay = y[i * particulas: (i + 1) * particulas]
    x_matrix[:, i] = columnax
    y_matrix[:, i] = columnay

# Calculamos la función de distribución radial de cada partícula con el resto en cada paso temporal
distancias = np.zeros((particulas * (particulas - 1) // 2, num_estados))

# Cálculo de las distancias
k = 0
for i in range(particulas):
    for j in range(i+1,particulas):
        distancias[k] = np.sqrt((x_matrix[i] - x_matrix[j])**2 + (y_matrix[i] - y_matrix[j])**2)
        k += 1
dist=distancias.flatten()
plt.hist(dist,bins=20,density=True)
plt.title("Distribución radial")
plt.xlabel("Distancia")
plt.ylabel("Frecuencia")
plt.show()
print((dist))
# Vamos a calcular la triangulación de Delaunay de nuestro sistema en el primer instante de tiempo
# Guardamos en vectores las coordenades x e y de las particulas en el primer estado del sistema
xd=x_matrix[:,1]
yd=y_matrix[:,1]

# Combinamos la coordenadas en un único vector
puntos = np.column_stack((xd, yd))

# Calcular la triangulación de Delaunay
triangulacion = Delaunay(puntos)

# Obtenemos los triángulos
triangulos = triangulacion.simplices

# Representamos gráficamente
plt.triplot(xd, yd, triangulos)
plt.plot(xd, yd, 'o')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Triangulación de Delaunay')
plt.show()

#Creamos una animación que represente la triangulación de Delauney para cada estado
fig, ax = plt.subplots()

# Función para actualizar la visualización en cada frame
def update(estado):
    ax.clear()

    # Calculamos la triangulación para cada estado
    triangulacion = Delaunay(np.column_stack((x_matrix[:, estado], y_matrix[:, estado])))

    triangulos = triangulacion.simplices

    # Representamos
    ax.triplot(x_matrix[:, estado], y_matrix[:, estado], triangulos)
    ax.plot(x_matrix[:, estado], y_matrix[:, estado], 'o')
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_title(f'Estado {estado + 1}')

# Creamos la animación
anim = FuncAnimation(fig, update, frames=num_estados, interval=1000, repeat=False)
plt.show()

# Calculamos la teselación de Voronoi para el estado incial
vor = Voronoi(puntos)

# Representamos gráficamente
voronoi_plot_2d(vor)
plt.plot(xd, yd, 'o')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Teselación de Voronoi')
plt.show()

# Creamos una animación que represente la teselación de Voronoi en cada estado
# Crear figura y ejes
fig, ax = plt.subplots()

# Función para actualizar la visualización en cada frame
def update(estado):
    ax.clear()

    # Calcular la teselación de Voronoi para el estado actual
    vor = Voronoi(np.column_stack((x_matrix[:, estado], y_matrix[:, estado])))

    # Visualizar la teselación de Voronoi
    voronoi_plot_2d(vor, ax=ax)
    ax.plot(x_matrix[:, estado], y_matrix[:, estado], 'o')
    ax.set_xlabel('x')
    ax.set_ylabel(' y')
    ax.set_title(f'Estado {estado + 1}')

# Crear la animación
anim = FuncAnimation(fig, update, frames=num_estados, interval=1000, repeat=True)

# Mostrar la animación
plt.show()