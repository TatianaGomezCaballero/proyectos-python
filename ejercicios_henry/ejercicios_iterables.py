# iterables
'''
A partir de una lista vacia, utiliza un ciclo while para cargar alli
numeros negativos de -15 a -1
'''

lista = []

n = -15

while n < 0:
    lista.append(n)
    n = n + 1
print(lista)

'''
¿Con un ciclo while sería posible recorrer la lista para imprimir sólo 
los números pares?'''

n = 0

while n < len(lista):
    if lista[n] % 2 == 0:
        print(lista[n])
    n = n + 1

# Resolver el punto anterior sin utilizar un ciclo while

for i in lista :
    if i % 2 == 0:
        print(i)


# Utilizar el iterable para recorrer sólo los primeros 3 elementos

for i in lista[:3]:
    print(i)

'''
Utilizar la función **enumerate** para obtener dentro del iterable, 
tambien el índice al que corresponde el elemento
'''

for indice, item in enumerate(lista):
    print(indice, item)

'''
Dada la siguiente lista de números enteros entre 1 y 20, 
crear un ciclo donde se completen los valores faltantes:
'''
lista = [1,2,5,7,8,10,13,14,15,17,20]

n = 1

while n <= 20:
    if not n in lista:
        lista.insert((n-1), n)
    n = n + 1
print(lista)

# sucesion fibonacci
# 30 numeros

fibo = [0,1]
n = 2

while n <= 30:
    fibo.append(fibo[n - 1] + fibo[n - 2])
    n = n + 1
print(fibo)

# relaizar la suma de todos los anteriores

suma = 0

for i in fibo:
    suma = suma + i
print(suma)

'''
9) La proporción aurea se expresa con una proporción matemática 
que nace el número irracional Phi= 1,618… que los griegos llamaron número áureo. 
El cuál se puede aproximar con la sucesión de Fibonacci. Con la lista del ejercicio anterior, 
imprimir el cociente de los últimos 5 pares de dos números contiguos
'''
inicio = 15
n = inicio - 5

while n < inicio:
    print(fibo[n] / fibo[n - 1])
    n = n + 1


# decir en que posicion se encientra la palabra n

palabra = 'Hola mundo soy tatiana'

for indice, item in enumerate(palabra):
    if item == 'n':
        print(indice)

# crear un diccionario e iterar u mostrar las claves

dicc = {'ciudad': ['bogota', 'cali', 'medellin'],
        'nombred':['tati', 'yei','sofi']
        }

for clave in dicc:
    print(clave)

# crear una nueva lista si el numero es divisible por 7

lista = [18,21,29,32,35,42,56,60,63,71,84,90,91,100]
lista2 = []

for i in lista:
    if i % 7 == 0:
        lista2.append(i)
print(lista2)

# contar el numero de elementos de elementos de la siguiente lista

lis = [[1,2,3,4],'rojo','verde',[True,False,False],['uno','dos','tres']]

cantidad = 0

for i in lis:
    if type(i) == list:
        cantidad = cantidad + len(i)
    else:
        cantidad = cantidad + 1
print(cantidad)