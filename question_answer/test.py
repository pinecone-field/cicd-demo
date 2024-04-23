import unittest
from .query import query

class TestApp(unittest.TestCase):
    def test_question_answer_query(self):
        answer = query("How does Shopify make money as a digital native business?")
        expected_answer = (
            "Shopify makes money by charging subscription fees for "
            "its e-commerce platform and taking a percentage of sales "
            "from merchants using its payment gateway, Shopify Payments."
        )
        
        self.assertEqual(answer, expected_answer)
    def test_query_with_similarity_min(self):
        answer = query("What does Waste Management do?")
        expected_answer = "Sorry, I do not have an answer to that question."
        self.assertEqual(answer, expected_answer)
        

if __name__ == '__main__':
    unittest.main()