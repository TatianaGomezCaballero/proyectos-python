class Vehiculo:
    def __init__(self, color, tipo, cilindraje):
        self.color = color
        self.tipo = tipo
        self.cilindraje = cilindraje

'''
2) A la clase Vehiculo creada en el punto 1, agregar los siguientes métodos:<br>
# Acelerar<br>
# Frenar<br>
# Doblar<br>
'''

class Vehiculo:
    def __init__(self, color, tipo, cilindraje):
        self.color = color
        self.tipo = tipo
        self.cilindraje = cilindraje
        self.velocidad = 0
        self.direccion = 0

    def acelerar(self, velocidad):
        self.velocidad = self.velocidad + velocidad

    def frenar(self, velocidad):
        self.velocidad = self.velocidad + velocidad

    def frenar(self, grados):
        self.direccion = self.direccion + grados

    def estado(self):
        print(f'T enecuentras a una velocidad de {self.velocidad} y {self.direccion}')

'''
Esta función devuelve un objeto instanciado de la clase Animal, 
    la cual debe tener los siguientes atributos:
        Edad    (Un valor de tipo de dato entero, que debe inicializarse en cero)
        Especie (Un valor de tipo de dato string)
        Color   (Un valor de tipo de dato string)
    y debe tener el siguiente método:
        CumplirAnios  (este método debe sumar uno al atributo Edad y debe devolver 
        ese valor)
    Recibe dos argumento:
        especie: Dato que se asignará al atributo Especie del objeto de la clase 
        Animal
        color: Dato que se asignará al atributo Color del objeto de la clase 
        Animal
    Ej:
        a = ClaseAnimal('perro','blanco')
        a.CumpliAnios() -> debe devolver 1
        a.CumpliAnios() -> debe devolver 2
        a.CumpliAnios() -> debe devolver 3
'''

class Animal:
    def __init__(self, especie, color):
        self.edad = 0
        self.especie = especie
        self.color = color

    def cumplirAnios(self):
        self.edad = self.edad + 1
        return self.edad

a = Animal('gato', 'amarillo')
print(a.cumplirAnios())
print(a.cumplirAnios())


