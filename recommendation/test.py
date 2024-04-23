import unittest
from .query import query

class TestApp(unittest.TestCase):
    def test_recommendation_query(self):
        recommendations = query(query_text="sector: Information Technology industry: Consulting", 
                                       rsi_filter=60, pe_filter=20, dividend_filter=1.5) 

        self.assertEqual(3, len(recommendations))
        self.assertEqual("ACN", recommendations[0]["ticker"])
        self.assertEqual("Information Technology", recommendations[0]["sector"])
        self.assertIn("Consulting", recommendations[2]["industry"])

    # def test_query_with_similarity_min(self):
    #     matches = query(query_text="sector: A sector that does not exist industry: Some random industry", 
    #                                    rsi_filter=99, pe_filter=99, dividend_filter=0)
    #     print(matches)
    #     self.assertEqual(matches, "Sorry, I do not have a recommendation for you.")

if __name__ == '__main__':
    unittest.main()