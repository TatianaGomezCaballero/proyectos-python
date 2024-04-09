# Ordenar una lista en orden sin usar librerias
# coding: utf-8
lista = [3,5,1,4,2,6]

def ordenar_lista(lista):
    for numero in range(len(lista)):
        numero_mas_pequeño = numero
        for numero_chiqui in range(numero + 1, len(lista)):
            if lista[numero_chiqui] < lista[numero_mas_pequeño]:
                numero_mas_pequeño = numero_chiqui

        lista[numero], lista[numero_mas_pequeño] = lista[numero_mas_pequeño], lista[numero]

    print(lista)

ordenar_lista(lista)

# ordenar una lista de mayor a menor

def mayor_a_menor(lista):
    for i in range(len(lista)):
        numero_mas_grande = i
        for j in range(i + 1, len(lista)):
            if lista[j] > lista[numero_mas_grande]:
                numero_mas_grande = j

        lista[numero_mas_grande], lista[i] =  lista[i], lista[numero_mas_grande]

    print(lista)

mayor_a_menor(lista)

# numero al revez
numero = str(123)



def revertir_cadena(numero):
    numero_al_reves = numero[::-1]
    return numero_al_reves

resultado = revertir_cadena(numero)
print(resultado)


# revertir el numero pero sin que el signo afecte en algo

numero = -123


def revertir_cadena2(numero):
    signo = -1 if numero < 0 else 1
    numero_sin_signo = abs(numero)
    numero_en_cadena = str(numero_sin_signo)
    numero_final = int(numero_en_cadena[::-1])
    return numero_final * signo


resultado = revertir_cadena2(numero)
print(resultado)

'''
Utilizar un ciclo while para realizar el factorial de un número guardado 
en una variable, sólo si la variable contiene un número entero mayor a 0
'''



n = 5
if type(n) == int:
    if n > 1:
        factorial = n
        while n > 2:
            n = n - 1
            factorial = factorial * n
        print(factorial)
    else:
        print('Es menor a 0')
else:
    print('No se puede')

# factorial dentro de una funcion

numero = 4

def factorial(numero):
    if type(numero) == int:
        if numero > 1:
            factorial = numero
            while numero > 2:
                numero = numero - 1
                factorial = factorial * numero
            print(factorial)
        else:
            print('No es entero')
    else:
        print('No es entero')

factorial(numero)

# Crear un ciclo for dentro de un ciclo while

n = 0
while n < 4:
    n = n + 1
    for i in range(1,n):
        print(i)

# crear ciclo while dentro de for

n = 6

for i in range(1,n):
    while n > 0:
        n = n - 1
        print(n)


# imprima numeros primos del 0 al 30



for i in range(0, 30):
    es_primo = True
    divisor = 2
    if i >= 2:
        while divisor <= i // 2:
            if i % divisor == 0:
                es_primo = False
            divisor = divisor + 1
        if es_primo:
            print(i)
    else:
        pass













