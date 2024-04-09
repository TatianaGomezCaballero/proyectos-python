class Casa:
    def __init__(self, color, cantidad_pisos):
        self.color = color
        self.cantidad_pisos = cantidad_pisos

casa_blanca = Casa('blanca', 4)

print(f'Mi casa es de color {casa_blanca.color} y tiene {casa_blanca.cantidad_pisos} pisos')


class Cubo:
    caras = 6
    def __init__(self, color):
        self.color = color

cubo_rojo = Cubo('rojo')

print(f'mi cubo es de color {cubo_rojo.color} y tiene {cubo_rojo.caras} caras')

class Personaje:
    real = False
    def __init__(self, especie, magico, edad):
        self.especie = especie
        self.magico = magico
        self.edad = edad

harry_potter = Personaje('Humano', True, 17)
print(f'Harry es {harry_potter.especie} su magia es {harry_potter.magico} y tiene {harry_potter.edad} años')
















