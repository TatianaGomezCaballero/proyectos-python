'''
Crea una función llamada devolver_distintos() que reciba 3
integers como parámetros.
Si la suma de los 3 numeros es mayor a 15, va a devolver el
número mayor.
Si la suma de los 3 numeros es menor a 10, va a devolver el
número menor.
Si la suma de los 3 números es un valor entre 10 y 15
(incluidos) va a devolver el número de valorintermedio
'''

def devolver_distintos(*args):
    if sum(args) > 15:
        return max(args)
    elif sum(args) <10:
        return min(args)
    else:
        return args

resultado = devolver_distintos(2,1,6)
print(resultado)

'''
Escribe una función (puedes ponerle cualquier nombre que
quieras) que reciba cualquier palabra como parámetro, y que
devuelva todas sus letras únicas (sin repetir) pero en orden
alfabético.
Por ejemplo si al invocar esta función pasamos la palabra
"entretenido"
'''

palabra = 'tatiana'

def palabra_reservada(palabra):
    set_nuevo = set(palabra)
    lista = list(set_nuevo)
    lista.sort()
    return lista

resultado = palabra_reservada(palabra)
print(resultado)

'''
Escribe una función que requiera una cantidad indefinida de
argumentos. Lo que hará esta función es devolver True si en
algún momento se ha ingresado al numero cero repetido dos
veces consecutivas.
Por ejemplo:
(5,6,1,0,0,9,3,5) >>> True
(6,0,5,1,0,3,0,1) >>> False
'''

def argumentos(*args):
    indice = 0
    for numero in args:
        if args[indice] == 0 and args[indice + 1] == 0:
            return True
        else:
            indice = indice + 1
    return False

resultado = argumentos(1,2,3,4,0,0,3)
print(resultado)

'''
Escribe una función llamada contar_primos() que requiera un
solo argumento numérico.
Esta función va a mostrar en pantalla todos los números
primos existentes en el rango que va desde cero hasta ese
número incluido, y va a devolver la cantidad de números
primos que encontró.
Aclaración, por convención el 0 y el 1 no se consideran primos
'''
numero = 30
def contar_primos(numero):
    primos = [2]
    iteracion = 3

    if numero < 2:
        return 0
    while iteracion <= numero:
        for n in range(3,iteracion,2):
            if iteracion % n == 0:
                iteracion = iteracion + 2
                break
        else:
            primos.append(iteracion)
            iteracion = iteracion + 2
    print(primos)

contar_primos(numero)

'''
Crear una función que al recibir una lista de números, devuelva el que más 
se repite y cuántas veces lo hace. Si hay más de un "más repetido", 
que devuelva cualquiera
'''

lista = [1,2,3,4,5,5,6,6,7,8,8]
def repetido(lista):
    lista_repetidos = []
    lista_unicos = []
    for i in lista:
        if i in lista_unicos:
            i = lista_unicos.index(i)
            lista_repetidos[i] = lista_repetidos[i] + 1
        else:
            lista_unicos.append(i)
            lista_repetidos.append(1)
    print(lista_unicos)

repetido(lista)


'''
Crear una función que convierta entre grados Celsius, Farenheit y Kelvin<br>
# Fórmula 1	: (°C × 9/5) + 32 = °F<br>
# Fórmula 2	: °C + 273.15 = °K<br>
# Debe recibir 3 parámetros: el valor, la medida de orígen y la medida de destino
'''
def conversion(valor, origen, destino):
    if origen == 'celsius':
        if destino == 'celsius':
            valor_destino = valor
        elif destino == 'fah':
            valor_destino = (valor * 9/5) + 32
        elif destino == 'kelvin':
            valor_destino = valor + 273.5
        else:
            print('incorrecto')
    else:
        print('origen no correcto')

    return valor_destino

resultado = conversion(3,'celsius','kelvin')
print(resultado)

'''
Iterando una lista con los tres valores posibles de temperatura que 
recibe la función del punto 5, hacer un print para cada combinación de los mismos:
'''
valores = ['celsius','fah','kevin']

# devuelva el factorial de un numero

def factorial(num):
    if type(num) != 0:
        if num > 0:
            factorial = num
            while num > 2:
                num = num -1
                factorial = factorial * num
            print(factorial)
        else:
            print('Es menor a 0')
    else:
        print('No es entero')

factorial(5)







