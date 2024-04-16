import unittest
from suma import sumar
from resta import restar
from multiplicacion import multiplicar
from division import dividir

class testSumar(unittest.TestCase):
    def test_sumar(self):
        self.assertEqual(sumar(5, 3), 8)
        self.assertEqual(sumar(-2, 2), 0)
        self.assertEqual(sumar(-1, -3), -4)

class testRestar(unittest.TestCase):
    def test_restar(self):
        self.assertEqual(restar(5, 3), 2)
        self.assertEqual(restar(-2, 2), -4)
        self.assertEqual(restar(-1, -3), 2)

class testMultiplicar(unittest.TestCase):
    def test_multiplicar(self):
        self.assertEqual(multiplicar(5, 3), 15)
        self.assertEqual(multiplicar(-2, 2), -4)
        self.assertEqual(multiplicar(-1, -3), 3)
        self.assertEqual(multiplicar(5, 0), 0)

class testDividir(unittest.TestCase):
    def test_dividir(self):
        self.assertEqual(dividir(6, 3), 2)
        self.assertEqual(dividir(-2, 2), -1)
        self.assertEqual(dividir(-4, -2), 2)
        

if __name__ == "__main__":
    unittest.main()