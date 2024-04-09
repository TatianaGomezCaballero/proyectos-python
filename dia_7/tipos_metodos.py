class Pajaro:
    alas = True
    ''' Metodos de instnacia'''
    def __init__(self, color, especie):
        self.color = color
        self.especie = especie

    def piar(self):
        print('PIO')

    def volar(self, metros):
        print(f'el pajaro volo {metros} mts')
        self.piar() # se puede acceder a otro metodo

    def cambiar_color(self):
        self.color = 'negro'
        print(f'mi color ahora es {self.color}') # cambiar atributos

    ''' Metodos de clase'''
    @classmethod
    def poner_huevos(cls, cantidad):
        print(f'esta semana puso {cantidad} huevos')
        cls.alas = False # modifica atributos de clase
        print(Pajaro.alas)

    ''' Mertodos estaticos'''
    @staticmethod
    def mirar():
        print('El pajaro miro')


piolin = Pajaro('amarillo', 'canario')
piolin.cambiar_color()
piolin.volar(66)

Pajaro.poner_huevos(4)
Pajaro.mirar()


class Personaje:
    def __init__(self, cantidad_flechas):
        self.cantidad_flechas = cantidad_flechas

    def lanzar_flechas(self):
        self.cantidad_flechas = self.cantidad_flechas - 1
        print(self.cantidad_flechas)


personajito = Personaje(30)
personajito.lanzar_flechas()
print(personajito.cantidad_flechas)



