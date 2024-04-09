# imprimir los numeros del 10 al 0

numero = 10

while numero >= 0:
    print(numero)
    numero = numero - 1


# restar de uno en uno los numeros, si son divisibles mostrarlo y si no ignorarlo

numero = 50
while numero >=0:
    if numero %5 ==0:
        print(numero)
        numero = numero -1
    else:
        numero = numero - 1

lista_numeros = [4,5,8,7,6,9,8,2,4,5,7,1,9,5,6,-1,-5,6,-6,-4,-3]

for numero in lista_numeros:
    if numero < 0:
        break
    print(numero)


numero = 30

while numero >=0:
   print(numero)
   numero = numero-1

