class Padre:
    def __init__(self, color_ojos):
        self.color_ojos = color_ojos
    def cabello(self):
        print('Su color de pelo es negro')


class Hija(Padre):
    pass

sofia = Hija('negros')
print(f'Sofia tiene los ojos {sofia.color_ojos} ')
sofia.cabello()










