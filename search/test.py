import unittest
from .query import search_query

class TestApp(unittest.TestCase):
    def test_search_query(self):
        answer = search_query("How does Shopify make money as a digital native business?")
        expected_answer = (
            "Shopify makes money by charging subscription fees for "
            "its e-commerce platform and taking a percentage of sales "
            "from merchants using its payment gateway, Shopify Payments."
        )
        
        self.assertEqual(answer, expected_answer)
    # def test_will_fail(self):
    #     self.assertEqual(1, 2)

if __name__ == '__main__':
    unittest.main()