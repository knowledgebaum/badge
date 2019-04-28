import unittest
from badgeModule import Badge, prepare_csv
from pathlib import Path

class Test_Badge(unittest.TestCase):
    def setUp(self):
        """
        Create an instance of dataframe csv called test user.
        """
        sympPath = Path('C:/webDev/pycharm/dieta/data/ak_symptoms.csv')
        trigPath = Path('C:/webDev/pycharm/dieta/data/ak_triggers.csv')
        df = prepare_csv(sympPath, trigPath)
        self.test_user = Badge(1, df)
        self.test_user.get_user_stats()


    def test_get_user_stats(self):

        self.assertIn( 335 ,self.test_user.show_user_stats_dict().values() )

    def test_get_rank_badge(self):
        result = self.test_user.get_rank_badge()
        self.assertEqual(result, 6)

    def test_get_complex_diet_badge(self):
        result = self.test_user.get_complex_diet_badge()
        self.assertTrue(result)

    def test_get_archivist_badge(self):
        result = self.test_user.get_archivist_badge()
        self.assertTrue(result)

    def test_get_coffee_badge(self):
        result = self.test_user.get_coffee_badge()
        self.assertTrue(result)

    def test_create_table(self):
        result = self.test_user.create_table().get('rank_badge')

        self.assertEqual(6, result)

        # def test_output_to_csv(self):

        "python - m unittest -v test_badge.py"


if __name__ == '__main__':
    unittest.main()