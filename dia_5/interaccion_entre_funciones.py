# juego de escoger el palito mas corto

from random import *

# lista de palitos

palitos = ['-', '--','---','----']

# mezclar palitos al azar

def mezclar_palitos(lista):
    shuffle(lista)
    return lista

# pedir intento al usuario

def pedir_intento():
    intento = ' '

    while intento not in ['1', '2','3','4']:
        intento = input('Esoge un numero del 1 al 4: ')
    return int(intento)


# comprobar intento

def chequear(lista, intento):
    if lista[intento - 1] == '-':
        print('Te toco pagar el almuerzo')
    else:
        print('Te salvate')

    print(f'Te toco {lista[intento - 1]}')


mezclar_palitos = mezclar_palitos(palitos)
probar = pedir_intento()
chequear(mezclar_palitos, probar)

'''
Crea una función (lanzar_dados) que arroje dos dados al azar y devuelva sus resultados:

La función debe retornar dos valores resultado, que se encuentren entre 1 y 6).

Dicha función no debe requerir argumentos para funcionar, sino que debe generar internamente 
los valores aleatorios.

Proporciona el resultado de estos dos dados a una función que se llame evaluar_jugada 
(es decir, esta segunda función debe recibir dos argumentos) y que retorne 
-sin imprimirlo- un mensaje según la suma de estos valores:

Si la suma es menor o igual a 6:

"La suma de tus dados es {suma_dados}. Lamentable"

Si la suma es mayor a 6 y menor a 10:

"La suma de tus dados es {suma_dados}. Tienes buenas chances"

Si la suma es mayor o igual a 10:

"La suma de tus dados es {suma_dados}. Parece una jugada ganadora"
'''
def lanzar_dados():
    numero1 = randint(1,6)
    numero2 = randint (1,6)
    return (numero1, numero2)

def evaluar_jugada(numero1, numero2):
    suma = numero1 + numero2
    if suma <= 6:
        return f'La suma de tus dados es {suma}. Lamentable'

    elif suma < 6 and suma < 10:
        return f'La suma de tus dados es {suma}. Tienes buenas chances'
    else:
        return f'La suma de tus dados es {suma}. Parece una jugada ganadora'

resultado1, resultado2 = lanzar_dados()

resultado = evaluar_jugada(resultado1, resultado2)
print(resultado)

'''
Crea una función llamada reducir_lista() que tome una lista como argumento 
(crea también la variable lista_numeros), y devuelva la misma lista, pero 
eliminando duplicados (dejando uno solo de los números si hay repetidos) 
y eliminando el valor más alto. El orden de los elementos puede modificarse.

Por ejemplo, si se le proporciona la lista [1,2,15,7,2] debe devolver [1,2,7].

Crea una función llamada promedio() que pueda recibir como argumento la lista 
devuelta por la anterior función, y que calcule el promedio de los valores de 
la misma. Debe devolver el resultado, sin imprimirlo.
'''
lista = [1,1,2,3,4,4,5]
def reducir_lista(lista):
    sets = set(lista)
    lista_sin_repetidos = list(sets)
    lista_sin_repetidos.sort()
    lista_sin_repetidos.pop(-1)
    return lista_sin_repetidos

lista_ajustada = reducir_lista(lista)

def promedio(lista_ajustada):
    promedio = sum(lista_ajustada)/len(lista_ajustada)
    return promedio

resultado_promedio = promedio(lista_ajustada)
print(resultado_promedio)

'''
Crea una función (llamada lanzar_moneda) que devuelva el resultado de 
lanzar una moneda (al azar). Dicha función debe poder devolver los resultados 
"Cara" o "Cruz", y no debe recibir argumentos para funcionar.

Crea una segunda función (llamada probar_suerte), que tome dos argumentos: 
el primero, debe ser el resultado del lanzamiento de la moneda. El segundo argumento, 
será una lista de números cualquiera (debes crear una lista con valores y 
llamarla lista_numeros).

Si se le proporciona una "Cara", debe mostrar el mensaje al usuario: 
"La lista se autodestruirá", y eliminarla (devolverla como lista vacía []).

Si se le proporciona una "Cruz", debe imprimir en pantalla: 
"La lista fue salvada" y devolver la lista intacta.
'''

def lanzar_monedas():
    moneda = ['cara', 'sello']
    lanzamiento = choice(moneda)
    return lanzamiento

lanzamiento_moneda = lanzar_monedas()
lista = [1,2,3,4,5,6]


def probar_suerte(lanzamiento_moneda, lista):
    if lanzamiento_moneda == 'cara':
        return lista.remove()
    else:
        return f'La lista se salvo {lista}'

resultado_moneda = probar_suerte(lanzamiento_moneda, lista)
print(resultado_moneda)

