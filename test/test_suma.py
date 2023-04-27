import unittest

from src.suma import suma

class pruebaSuma(unittest.TestCase):
    def testSuma(self):
        unaSuma = suma(2,3)
        total = unaSuma.getSuma()
        self.assertEqual(total,5,"test de suma correcta")
        self.assertEqual(total,4,"test suma incorrecta pero valido")

class simplisticTest(unittest.TestCase):
    def test(self):
        self.assertTrue(True)


if __name__ = '__main__'
    if __name__ == '__main__':
        unittest.main(verbosity=10)
