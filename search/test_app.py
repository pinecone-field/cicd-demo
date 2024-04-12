import unittest
from query import search_query

class TestApp(unittest.TestCase):
    def test_search_query(self):
        answer = search_query("What are the main challenges in machine learning?")
        expected_answer = (
            "The main challenges in machine learning include dealing with insufficient "
            "quantities of training data, handling unstructured data, avoiding bias in "
            "models, overfitting, and underfitting."
        )
        
        self.assertEqual(answer, expected_answer)
        
if __name__ == '__main__':
    unittest.main()