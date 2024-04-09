serie = 'N-02'

match serie:
    case 'N-01':
        print('samsung')
    case 'N-02':
        print('apple')
    case 'N-03':
        print('nokia')
    case _:
        print('no se cual es')


cliente = {'nombre': 'tatiana',
           'edad':26,
           'profesion':'biologa'
          }

pelicula = {'titulo':'barbie',
            'ficha': {'creador': 'lala', 'fecha': 2023}
            }

elementos = [cliente, pelicula, 'libros']

for e in elementos:
    match e:
        case {'nombre': nombre,
              'edad':edad,
              'profesion': profesion
        }:
            print('es un cliente')

        case {'titulo':titulo,
              'ficha': {'creador': creador, 'fecha': fecha}
              }:
            print('es una peli')

        case _:
            print('no se que es')
