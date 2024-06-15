import unittest
import pet_analysis as pa
import pandas as pd

class TestPetAnalysis(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.df = pa.load_data('../Parth_Project/pets.csv')
        cls.df = pa.clean_data(cls.df)

    def test_load_data(self):
        self.assertIsInstance(self.df, pd.DataFrame)

    def test_calculate_average_price(self):
        avg_price = pa.calculate_average_price(self.df, 'Dog')
        self.assertIsInstance(avg_price, float)

    def test_find_pets_with_feature(self):
        pets = pa.find_pets_with_feature(self.df, 'Blood Type')
        self.assertIsInstance(pets, list)

    def test_get_species_statistics(self):
        stats = pa.get_species_statistics(self.df)
        self.assertIsInstance(stats, dict)
        self.assertIn('Dog', stats)

if __name__ == '__main__':
    unittest.main()
