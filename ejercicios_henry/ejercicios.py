# Crear una variable con un numero y luego imprimir si es mayor o menor a  0

numero = 10

if numero > 0:
    print('Es mayor a 0')
else:
    print('Es menor a 0')

# crear dos variables y comparar si son del mismo tipo

entero = 12
flotante = 13.5

if type(entero) == type(flotante):
    print('La variables son del mismo tipo')
else:
    print('Las variables no son del mismo tipo')

# imprima los valores del 1 al 20 y diga si son pares o impares

for i in range(1, 20):
    if i % 2 == 0:
        print(f'{i} es par')
    else:
        print(f'{i} es impar')

'''En un ciclo for muestre los valores de 0 a 5 y el resultado elevarlo a 
la potencia igual a 3 '''

for i in range(0, 6):
    print(f'El valor de {i} elevado a la potencia de 3 es {i ** 3}')

''' Crear una variable que contenga un numero entero y realizar un ciclo for 
la misma cantidad de veces'''

entero = 5

for i in range(0, entero):
    print(i)

''' 6) Utilizar un ciclo while para realizar el factorial de un número guardado 
en una variable, sólo si la variable contiene un número entero mayor a 0'''

numero = 4

if type(numero) == int:
    if numero > 0:
        factorial = numero
        while numero > 2:
            numero = numero - 1
            factorial = factorial * numero
        print(f'El factorial del numero es: {factorial}')
    else:
        print('El numero es negativo')
else:
    print('No es entero')

n = 5

if type(n) == int:
    if n > 0:
        fact = n
        while n > 2:
            n = n - 1
            fact = fact * n
        print(f'El factorial del numero  es: {fact}')
    else:
        print('Es menor a 0')
else:
    print('No es entero')



# 7) Crear un ciclo for dentro de un ciclo while
n = 0

while n < 4:
    n = n + 1
    for i in range(1, n):
        print(i)

'''numero = 6

while numero > 0:
    numero = numero -1
    for i in range(1,numero):
        print(i)'''

# crea un ciclo while dentro de un for
n = 4
for i in range(1, n):
    while n < 4:
        n = n - 1
        print(i)

# imprima numeros primos de 0 y 30

for n in range(2, 30):
    primo = True
    divisor = 2

    while divisor <= n // 2:
        if n % divisor == 0:
            primo = False
        divisor = divisor + 1
    if primo:
        print(n)

'''
12) Aplicando continue, armar un ciclo while que solo imprima los valores 
divisibles por 12, dentro del rango de números de 100 a 300
'''
n = 100

while n <= 300:
    n = n + 1
    if n % 12 != 0:
        print(f'{n}, No es divisible por 12')
        continue
    else:
        print(f'{n}, es divisible por 12')

'''
Utilizar la función **input()** que permite hacer ingresos por teclado, 
para encontrar números primos y dar la opción al usario de buscar el 
siguiente'''








