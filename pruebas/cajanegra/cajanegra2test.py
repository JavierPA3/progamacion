import unittest

from cajanegra2 import Cuenta

class MyTestCase(unittest.TestCase):
    def setUp(self) :
        self.cuenta = Cuenta(1000)

if __name__ == '__main__' :
    unittest.main()
