from random import *
lista = ['panadero', 'letras', 'biologa']
palabras_correctas = []
palabras_incorrectas = []
intentos = 6
aciertos = 0

def elegir_palabra(lista_palabras):
    palabra_elegida = choice(lista_palabras)
    letras_unicas = len(palabra_elegida)

    return palabra_elegida, letras_unicas

def pedir_letra():
    letra_elegida = ''
    es_correcta = False
    abecedario = 'abcdefghijklmnñopqrstuvwxyz'

    while not es_correcta:
        letra_elegida = input('Escoge una letra: ')
        if letra_elegida in abecedario and len(letra_elegida) == 1:
            es_correcta = True

        else:
            print('Elegiste mal')
    return letra_elegida

def tablero_nuevo(palabra_elegida):
    lista_nueva = []
    for l in palabra_elegida:
        if l in palabras_correctas:
            lista_nueva.append(l)
        else:
            lista_nueva.append('-')
    print(' '.join(lista_nueva))










