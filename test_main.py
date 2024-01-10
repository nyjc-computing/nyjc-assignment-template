import unittest

class TestAssignment(unittest.TestCase):

    def test_part1(self):
        pass

    def test_part2(self):
        pass

    def test_part3(self):
        pass

    def test_part4(self):
        pass

    def test_docstrings(self):
    for func in []:
        self.assertIs(hasattr(func, "__doc__"), True)
        self.assertTrue(func.__doc__, f"{func.__name__}() does not have a docstring")


if __name__ == '__main__':
    unittest.main()
