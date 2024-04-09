class Padre:
    def cabello(self, color):
        self.color = color
        print(f'El cabello es de color {color}')

class Madre:
    def ojos(self):
        print('Tiene los ojos verdes')

class Hijo(Padre, Madre):
    pass

arturo = Padre()
arturo.cabello('negro')

tatiana = Hijo()
tatiana.cabello('negro')
tatiana.ojos()


