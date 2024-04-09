from random import *

numero_azar = randint(1,101)

nombre = input ('Dime tu nombre: ')

consigna = f'Bueno {nombre} he pensado un numero entre 1 y 100, solo tienes 8 intentos para adivinar cual es el numero'
print(consigna)
numero_intentos = 0

while numero_intentos < 8:
    consulta = input('Dime un numero del 1 al 100: ')
    numero = int(consulta)
    numero_intentos = numero_intentos + 1

    if numero < 1 or numero > 100:
        print('Numero o permitido')

    elif numero < numero_azar:
        print('numero incorrecto, es menor al que pense')

    elif numero > numero_azar:
        print('numero incorrecto, es mayor al numero')

    else:
        print('Adivinate el numero')
        break


if numero != numero_azar:
    print('Lo siento')


