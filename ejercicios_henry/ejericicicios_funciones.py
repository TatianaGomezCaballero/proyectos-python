'''
Crear una función que reciba un número como parámetro y devuelva si True si es primo y
False si no lo es
'''

numero = 8

def revision(numero):
    for i in range(2,numero):
        if numero % i == 0:
            return False
        else:
            return True
    if numero < 2:
        return False

resultado = revision(numero)
print(resultado)

'''
Utilizando la función del punto 1, realizar otra función que reciba de 
parámetro una lista de números y devuelva sólo aquellos que son primos 
en otra lista
'''
lista = list(range(0, 30))

def numeros_primos(lista):
    lista_primos = []
    for i in lista:
        if revision(i):
            lista_primos.append(i)
    print(lista_primos)

numeros_primos(lista)
