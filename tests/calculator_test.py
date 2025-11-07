from unittest import TestCase, main
from MatImit1 import calculator

class Calculator_test(TestCase):
    def test_plus(self):
        self.assertEqual(calculator("2+2"), 4)

    def test_divisionByZero(self):
        with self.assertRaises(ValueError) as e:
            calculator("2/0")
        self.assertEqual("Деление на нолsь", e.exception.args[0])
if __name__ == '__main__':
    main()