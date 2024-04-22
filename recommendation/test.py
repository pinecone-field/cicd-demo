import unittest
from .query import recommendation_query

class TestApp(unittest.TestCase):
    def test_search_query(self):
        matches = recommendation_query(query_text="sector: Information Technology industry: Consulting", 
                                       rsi_filter=60, pe_filter=20, dividend_filter=1.5)

        print(matches)

        self.assertEqual(len(matches), 3)
        self.assertEqual(matches[0].metadata["ticker"], "ACN")
        self.assertEqual(matches[1].metadata["sector"], "Information Technology")
        self.assertIn("Consulting", matches[2].metadata["industry"])
        
    #self.assertEqual(answer, expected_answer)
    # def test_will_fail(self):
    #     self.assertEqual(1, 2)

if __name__ == '__main__':
    unittest.main()