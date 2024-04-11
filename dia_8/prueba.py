import unittests
import unittest

class ProbarFuncion(unittest.TestCase):
    def test_mayuscula(self):
        palabra = 'buen dia'
        resultado = unittests.cambiar_mayuscula(palabra)
        self.assertEqual(resultado, 'BUEN DIA')

if __name__ == '__main':
    unittest.main()