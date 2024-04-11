from datetime import datetime
''' 1. Imagine que está desarrollando un sistema para ayudar a
los agricultores a gestionar la información sobre sus cultivos.
Implementar un programa Python que permita a los agricultores
realizar las siguientes operaciones:

a. Agregue un nuevo cultivo con su nombre, tipo, área plantada
y fecha de siembra.
b. Calcular la edad de un cultivo en días desde la fecha de siembra.
C. Muestra todos los cultivos y su información almacenada. '''

agricultura = []

def agregar_cultivo(nombre, tipo,area,fecha):
    cultivo = {'nombre': nombre,
               'tipo': tipo,
               'area': area,
               'fecha': datetime.strptime(fecha, '%Y-%m-%d')
               }
    agricultura.append(cultivo)

def edad_cultivo(fecha):
    fecha_actual = datetime.now()
    fecha = datetime.strptime(fecha, '%Y-%m-%d')
    edad = fecha - fecha_actual
    return edad.days


def todos_los_cultivos(agricultura):
    for n in agricultura:
        print(f'Mi cultivo se llama {n['nombre']}, es de tipo  {n['tipo']},y tiene un area de {n['area']} mts')


agregar_cultivo('papa', 'hortaliza', 1200,'1998-02-12')
agregar_cultivo('fresa', 'hortaliza', 1200,'1998-02-12')
agregar_cultivo('habichuela', 'hortaliza', 1200,'1998-02-12')
print(agricultura)
todos_los_cultivos(agricultura)

resultado = edad_cultivo('1998-02-12')
print(f'Los dias que tiene mi cultivo son {resultado} dias')


'''
Instrucciones: Defina una función llamada add_crop que tome parámetros para el
nombre del cultivo, tipo, área plantada y fecha de siembra. Esta función debería 
agregar una nueva crop al diccionario de cultivos. La clave del diccionario será el 
nombre del cultivo, y el valor será otro diccionario que contenga la información 
correspondiente.
a. Defina una función llamada calcular_crop_age que tome el nombre de un cultivo
y la fecha actual. Esta función debe calcular y devolver el valor del cultivo.
Edad en días desde la fecha de siembra.
b. Defina una función llamada show_crops que imprima todos los cultivos almacenados en el
diccionario junto con su información.
'''

def add_crop(cultivos, nombre_cultivo, tipo, area, fecha):
    fecha = datetime.strptime(fecha, '%Y-%m-%d')
    cultivos[nombre_cultivo] = {'tipo':tipo, 'area':area, 'fecha':fecha}

def calcular_crop_age(cultivos, nombre_cultivo, fecha_actual):
    fecha_actual = datetime.now()
    fecha = cultivos[nombre_cultivo]['fecha']
    edad = fecha_actual - fecha
    return edad.days

def show_crops(cultivos):
    for nombre_cultivo, caracterisiticas in cultivos.items():
        print(f'el nombre de mi cultivo es: {nombre_cultivo}, es de tipo {caracterisiticas['tipo']},con un area de {caracterisiticas['area']}')

cultivos  = {}

add_crop(cultivos, 'maiz','cereal', 1200, '2005-12-21')
add_crop(cultivos, 'fresa','fruta', 900, '2007-02-12')

show_crops(cultivos)








