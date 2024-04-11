def suma():
    n1 = 12
    n2 = '23'
    suma = n1 + n2
    print(suma)

try:
    suma()
except ValueError:
    print('Estas sumando diferentes tipos')
except TypeError:
    print('Algo salio mal')

else:
    print('Todo salio bien')
finally:
    print('Gracias')


def pedir_numero():
    while True:
        try:
            numero = int(input('Dame un numero: '))
        except:
            print('No es un numero')
        else:
            print(f'lograsta darme este numero{numero}')

        print('Gracias')




























































