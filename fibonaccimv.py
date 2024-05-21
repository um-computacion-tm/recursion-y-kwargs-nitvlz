import unittest

def fibonacci(n):

    if n in (0,1):
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)


class TestFibonacci(unittest.TestCase):

    def test_0(self):
        result = fibonacci(0)
        self.assertEqual(result, 0)

    def test_1(self):
        result = fibonacci(1)
        self.assertEqual(result, 1)

    def test_2(self):
        result = fibonacci(2)
        self.assertEqual(result, 1)

    def test_3(self):
        result = fibonacci(3)
        self.assertEqual(result, 2)

    def test_4(self):
        result = fibonacci(4)
        self.assertEqual(result, 3)

    def test_5(self):
        result = fibonacci(5)
        self.assertEqual(result, 5)

    def test_6(self):
        result = fibonacci(6)
        self.assertEqual(result, 8)

    def test_7(self):
        result = fibonacci(7)
        self.assertEqual(result, 13)

    def test_8(self):
        result = fibonacci(8)
        self.assertEqual(result, 21)

    def test_9(self):
        result = fibonacci(9)
        self.assertEqual(result, 34)

    def test_9(self):
        result = fibonacci(10)
        self.assertEqual(result, 55)

    def test_9(self):
        result = fibonacci(11)
        self.assertEqual(result, 89)

    def test_9(self):
        result = fibonacci(12)
        self.assertEqual(result, 144)

    def test_9(self):
        result = fibonacci(13)
        self.assertEqual(result, 233)

    def test_9(self):
        result = fibonacci(14)
        self.assertEqual(result, 377)

    def test_9(self):
        result = fibonacci(15)
        self.assertEqual(result, 610)

    def test_9(self):
        result = fibonacci(9)
        self.assertEqual(result, 987)

    unittest.main()