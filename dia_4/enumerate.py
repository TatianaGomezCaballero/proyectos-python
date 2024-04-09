lista = ['a','b','c']

mis_tuples = list(enumerate(lista))

indice_1 = mis_tuples[1][0]
print(indice_1)

# mostrar el indice de la lista de personas
lista_nombres = ["Marcos", "Laura", "Mónica", "Javier", "Celina", "Marta", "Darío", "Emiliano", "Melisa"]


for indice, nombre in enumerate(lista_nombres):
    print(f'{nombre} esta en el indice {indice}')


# imprimir solo los indices de los que comienzan com la letra M

lista_nombres = ["Marcos", "Laura", "Mónica", "Javier", "Celina", "Marta", "Darío", "Emiliano", "Melisa"]
for indice, item in enumerate(lista_nombres):
    if item[0] == 'M':
        print(indice, item)