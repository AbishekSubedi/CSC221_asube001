import unittest
from city_functions import city_country


class CitiesTestCase(unittest.TestCase):
    def test_city_country(self):
        formatted_string = city_country("santiago", "chile")
        self.assertEqual(formatted_string, "santiago, chile")

    def test_city_country_population(self):
        formatted_string = city_country("santiago", "chile", "5000000")
        self.assertEqual(formatted_string, "santiago, chile - population=5000000")


if __name__ == "__main__":
    unittest.main()
