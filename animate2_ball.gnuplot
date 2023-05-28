# ANIMATE BALLS for MD codes (disks)

# Usage example: "gnuplot -e 'nt=2000; LX=10; LY=10' --persist animate2_ball.gnuplot"

# Para Linux:
# set t x11

# Para Windows:
set terminal wxt

# Seleccionamos los rangos de los ejes
set xrange[-LX*0.5:LX*0.5]
set yrange[-LY*0.5:LY*0.5]
set size ratio LY/LX

# Cambiamos el directorio
cd 'C:/Users/Africa/Desktop/fec/pyMD'

archivo = 'xy.dat'
n_particulas = 10

do for [i=0:(int(total_lineas/n_particulas)-1)] {
    inicio = i * n_particulas
    fin = inicio + n_particulas-1
    plot archivo every ::inicio::fin u 1:2:(1) w circles title archivo
    pause 0.1
}