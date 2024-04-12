import unittest

class TestApp(unittest.TestCase):
    def test_method1(self):
        # Add your test logic for method1 here
        self.assertEqual(1, 1)

    def test_method2(self):
        # Add your test logic for method2 here
        self.assertEqual(2, 2)

    def test_method3(self):
        # Add your test logic for method3 here
        self.assertEqual(3, 3)

if __name__ == '__main__':
    unittest.main()