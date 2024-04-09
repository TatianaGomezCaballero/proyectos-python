# Erika Tatiana Gomez Caballero

'''
Escriba una función de Python llamada promedio que tome tres números como argumentos y
devuelve su promedio. Almacene el resultado en una variable e imprímalo. Prueba tu función
con algunas entradas de muestra.
'''


def promedio(x,y,z):
    suma = x + y + z
    cantidad = 3
    ponderado = suma/cantidad
    return ponderado


resultado = promedio(4,5,6)
print(f'El promedio de estos numeros es {resultado}')


# Escribe funcion de su preferencia, en mi caso una funcion que me busque el cuadrado de un numero

num = 2
def cuadrado(num):
    print(num ** 2)


cuadrado(num)


# mira el error en el codigo, si lo hay informar

x = 5
y = 3
z = x + y
print("The sum of x and y is: ", z)

print('No hay error')

'''
Operadores: escriba una función de Python que calcule el área de un rectángulo, tome el
longitud y ancho del rectángulo como argumentos y luego calcular el área usando
operadores adecuados.
'''


def area_rectangulo(longitud, ancho):
    area = longitud * ancho
    return area


resultado = area_rectangulo(4, 6)
print(f'El area de mi rectangulo es {resultado}')

# muestre longitud de la siguiente cadena

cadena = 'universidad del cauca'
largo_cadena = len(cadena)
print(f'El largo de mi cadena es {largo_cadena}')

# Muestre las iniciales fdca
cadena2 = 'Facultad de Ciencias Agrarias'

letras_iniciales = cadena2[0] + cadena2[12] + cadena2[21]
print(f'Mis letras iniciales son {letras_iniciales}')

# 2 forma de hacerla
cadena3 = 'Facultad de Ciencias Agrarias'
letras = ''
for letra in cadena3:
    if letra in 'FCA':
        letras = letras + letra

print(letras)


cadena = 'Facultad de Ciencias Agrarias'
letras_separadas = cadena.split()

letrass = ' '
for letra in letras_separadas:
    letrass += letra[0].upper()

print(f'Las iniciales de esta cadena son {letrass}')



