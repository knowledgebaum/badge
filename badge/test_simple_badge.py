import unittest
from badge.simple_badge_module import *
from pathlib import Path

class Test_Badge(unittest.TestCase):

    def test_get_rank_badge(self):
        result = get_rank_badge(1)
        self.assertEqual(result, 5)

    def test_get_complex_diet_badge(self):
        result = get_complex_diet_badge(1)
        self.assertTrue(result)

    def test_get_archivist_badge(self):
        result = get_archivist_badge(1)
        self.assertTrue(result)

    def test_get_coffee_badge(self):
        result = get_coffee_badge(1)
        self.assertTrue(result)

    def test_get_gluten_badge(self):
        result = get_gluten_badge(1)
        self.assertTrue(result)

    def test_get_lactose_badge(self):
        result = get_lactose_badge(1)
        self.assertTrue(result)

    def test_get_lectin_badge(self):
        result = get_lectin_badge(1)
        self.assertTrue(result)



    # def test_get_user_stats(self):
    #
    #     self.assertIn( 335, list(.values()) )



if __name__ == '__main__':
    unittest.main()

"python - m unittest -v test_simple_badge.py"
