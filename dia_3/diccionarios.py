cliente = {'nombre': 'tati',
           'edad': 26,
           'talla':165
           }

consulta = cliente['nombre']
print(consulta)

dic = {'c1': 300,
       'c2': [1,3,4],
       'c3': {'s1':23, 's2': 23}
       }

resultado = dic['c3']['s1']
print(resultado)

dic2 = {'c1': ['a','b','c'],
        'c2': ['d','e','f']
        }

resultado = dic2['c2'][1].upper()
print(resultado)

diccionario = {'euro': 'E',
               'dolar':'$'
               }

pregunta = input('Dime que consigna de pesos estas buscando: ')
print(pregunta)

if pregunta == 'euro':
    print(f'esta consigna si la tenemos y es {diccionario['euro']}')

elif pregunta == 'dolar':
    print(f'esta consigna si la tenemos y es {diccionario['dolar']}')

else:
    print('lo siento no tenemos esa consigna')

# frutas y mumero de pesos por kilo

dict = {'banano': 1.32,
        'fresa':1.54
        }

