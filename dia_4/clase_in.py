x = 5
y = 6

def suma(x,y):
    sumar = x + y
    print(sumar)

suma(x,y)


nombre = 'tatiana'


def nombres(nombre):
    print(f'holii soy {nombre}')


nombres(nombre)


def nombrar():
    nombre = 'tatiana'
    print(f'holi soy {nombre}')


nombrar()


lista = [3,4,5,7]


def suma(lista):
    suma = 0
    for numero in lista:
        suma = suma + numero
    return suma

resultado = suma(lista)
print(resultado)

# saludar con nombre

nombre = input('dime tu nombre: ')


def saludar_nombre(nombre):
    print(f'holi {nombre}')


saludar_nombre(nombre)


def dolar_a_euro(dolar):
    conversion = dolar * 5000
    print(conversion)

dolar_a_euro(1000)



listado = ['yei','tati','sofi']


def nombres(listado):
    for nombre in listado:
        print(f'holi {nombre}')


nombres(listado)

def convertir_dolar_peso(dolares):
    coversion = dolares * 4300
    return coversion

resultado = convertir_dolar_peso(1000)
print(resultado)


peso_seco = 34
peso_humedo = 21

def conversion(peso_seco, peso_humedo):
    conver = peso_seco - peso_humedo
    division = conver/peso_seco
    return division

resultado = conversion(peso_seco,peso_humedo)
print(resultado)
