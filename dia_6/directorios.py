import os
# mostrar donde estamos parados
ruta = os.getcwd()
print(ruta)

from pathlib import Path
# abrir desde otra ruta
ruta = os.chdir('/Users/caica/Desktop/biologia')

archivo = open('prueba2.txt')
print(archivo.read())

# crear directorios
# ruta = os.mkdir('/Users/caica/Desktop/biology')

carpeta = Path('/Users/caica/Desktop/teoria curso python')/'otro_archivo.txt'
mi_archivo = open(carpeta)
print(mi_archivo.read())

