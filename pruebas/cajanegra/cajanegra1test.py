import unittest
from cajanegra1 import Calculadora

class MyTestCase(unittest.TestCase) :
    def setUp(self) :
        self.calculadora = Calculadora()

    def test_sumar(self):
        self.assertEqual(self.calculadora.sumar(20), 20)
        self.assertEqual(self.calculadora.restar(10), 10)
        self.assertEqual(self.calculadora.getResultado(), 10)

    def test_resta(self):
        self.assertEqual(self.calculadora.restar(10), -10)
        self.assertEqual(self.calculadora.sumar(10), 0)
        self.assertEqual(self.calculadora.getResultado(), 0)

    def test_get_resultado(self):
        self.assertEqual(self.calculadora.getResultado(), 0)

    def tiarDown(self):
        del self.calculadora

if __name__ == '__main__' :
    unittest.main()
