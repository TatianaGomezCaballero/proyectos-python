# Ordenar ujna lista en orden sin usar librerias

lista = [3,5,1,4,2,6]

def ordenar_lista(lista):
    for i in range(len(lista)):
        numero_mas_pequeño = i
        for j in range(i + 1, len(lista)):
            if lista[j] < lista[numero_mas_pequeño]:
               numero_mas_pequeño = j
        lista[i], lista[numero_mas_pequeño] = lista[numero_mas_pequeño], lista[i]
    print(lista)


ordenar_lista(lista)

# ordenar de mayor a menor
lista = [3,5,1,4,2,6]
def ordenar_mayor_a_menor(lista):
    for i in range(len(lista)):
        numero_grande = i
        for j in range(i + 1, len(lista)):
            if lista[j] > lista[numero_grande]:
                numero_grande = j
        lista[i], lista[numero_grande] = lista[numero_grande], lista[i]
    print(lista)

ordenar_mayor_a_menor(lista)

# numero al revez

numero = str(123)



def revertir_cadena(numero):
    numero_al_reves = numero[::-1]
    return numero_al_reves

resultado = revertir_cadena(numero)
print(resultado)

# hacerlo con numero negativo pero sin mover el menos

numero2 = -123

def revetir_sin_signo(numero2):

    signo = -1 if numero2 < 0 else 1
    numero_sin_signo = abs(numero2)
    numero_cadena = str(numero_sin_signo)
    numero_final = int(numero_cadena[::-1])
    return numero_final * signo

resultado = revetir_sin_signo(numero2)
print(resultado)





