# Importamos las librerías necesarias
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm

# ¡CUIDADO! Para que el programa funcione correctamente el número de partículas tiene que ser el mismo que en MD_numpy
particulas=50

# Leemos el fichero que contiene las velocidades de las partículas
velocidades = np.loadtxt('vxvy.dat', usecols=(0, 1), unpack=True)

# Almacenamos los datos de las velocidades en dos vectores diferentes
vx = velocidades[0]
vy = velocidades[1]

# Constrimos matrices para que cada columna de la matriz represente las velocidades de las n particulas en un estado
num_columnas=int(len(vx)/particulas)
vx_matrix = np.zeros((particulas, num_columnas))
vy_matrix = np.zeros((particulas, num_columnas))

for i in range(num_columnas):
    columnax = vx[i * particulas: (i + 1) * particulas]
    columnay = vy[i * particulas: (i + 1) * particulas]
    vx_matrix[:, i] = columnax
    vy_matrix[:, i] = columnay

# Repetimos el proceso para las posiciones de las partículas

# Leemos el fichero que contiene las posiciones de las partículas
posiciones = np.loadtxt('xy.dat', usecols=(0, 1), unpack=True)

# Almacenamos los datos de las posiciones en dos vectores diferentes
x = posiciones[0]
y = posiciones[1]

# Construimos matrices para que cada columna de la matriz represente las posiciones de las n particulas en un estado
x_matrix = np.zeros((particulas, num_columnas))
y_matrix = np.zeros((particulas, num_columnas))

for i in range(num_columnas):
    columnax = x[i * particulas: (i + 1) * particulas]
    columnay = y[i * particulas: (i + 1) * particulas]
    x_matrix[:, i] = columnax
    y_matrix[:, i] = columnay

# Importamos los datos de la temperatura
datosT= np.loadtxt('temp.dat', usecols=(0, 1), unpack=True)
t=datosT[0]
T=np.mean(t)

# Definimos las x para representar nuestra función de Maxwell
x = np.linspace(0,7,100)

# Calculamos el módulo de la velocidad media
v=np.zeros(len(vx))
for i in range(len(vx)):
    v[i]=np.sqrt(vx[i]**2+vy[i]**2)

# Calculamos la media de cada componente para obtener la velocidad media vectorial
vx_media=np.mean(vx)
vy_media=np.mean(vy)
print('Velocidad media de las partículas: ({0:1.3f}, {0:1.3f})'.format(vx_media, vy_media))

# Calculamos el módulo de la velocidad al cuadrado
v2=np.zeros(len(vx))
for i in range(len(vx)):
    v2[i]=vx[i]**2+vy[i]**2

v2_mean=np.mean(v2)
print('Módulo de la velocidad media al cuadrado',v2_mean)

# Calculamos el módulo de la velocidad elevado a 4 para calcular el coeficiente de kurtosis
v4=np.zeros(len(vx))
for i in range(len(vx)):
    v4[i]=(vx[i]**2+vy[i]**2)**2
v4_mean=np.mean(v4)

# Cálculo del coeficiente de kurtosis
k=v4_mean/v2_mean**2
print("Coeficiente de Kurtosis",k)

# Definimos la función de Maxwell para comparar con los datos experimentales
def fmaxwell(x,T):
    return (x/(0.5*T))*np.exp(-x**2/(2*0.5*T))
f=fmaxwell(x,T)

# Dibujamos el histograma frente a la función de Maxwell
plt.plot(x,f, label="Maxwell")
plt.hist(v, density=True, label="Simulación") 
plt.xlabel('Velocidades')
plt.ylabel('Frecuencia')
plt.legend(loc = "upper right")
plt.title('Distribución de velocidades')
plt.show()

# Calculamos los coeficientes de autocorrelación para cada una de las particulas en cada estado y los guardamos en un vector
desplazamientos=100
acorr = sm.tsa.acf(v,nlags=desplazamientos)

# Calculamos la media de los coeficientes de autocorrelación
media_acorr=np.mean(acorr)
print("Coeficiente de autocorrelación medio para",desplazamientos,"desplazamientos:",media_acorr)





