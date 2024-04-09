lista = [1,2,3,4,5,6,7,8,9,10]

def agrupar_por_numeros(lista,numero_agrupa):
    return [lista[n:n + numero_agrupa] for n in range(0,len(lista), numero_agrupa)]


resultado = agrupar_por_numeros(lista, 4)
print(resultado)

lista = [1,2,3,4]
valor = [numero ** 2 for numero in lista]
print(valor)

lista2 = [2,3,4,5]
def potencia(lista2):
    return [numero ** 2 for numero in lista2]

resultado = potencia(lista2)
print(resultado)