import unittest
from palindromos import palindromo

class Testpalindromo(unittest.TestCase):
    def test_1(self):
        resultado = palindromo("ana")
        self.assertEqual(resultado, True)

    def test_2(self):
        resultado = palindromo("Radar")
        self.assertEqual(resultado, True)
    
    def test_3(self):
        resultado = palindromo("Sale El As")
        self.assertEqual(resultado, True)

    def test_4(self):
        resultado = palindromo("No es palindromo")
        self.assertEqual(resultado, False)
        

if __name__ == '__main__':
    unittest.main()
