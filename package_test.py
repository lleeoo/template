"""driver for quick model build.
To use in VS Code see https://code.visualstudio.com/docs/python/testing"""
import unittest
import os

import pandas as pd

from package import module as m

class TestUtils(unittest.TestCase):
    "Run basic model"
    @classmethod
    def setUpClass(cls):
        "this runs once for all tests, so a good place to query databases, etc."
        # if the local cache of the data doesn't exist the code below will create it
        base = os.path.dirname(__file__)
        full_csv = f'{base}/data/a_large_file.csv'
        try:
            cls.full_df = pd.read_csv(full_csv)
        except FileNotFoundError:

            # Create a list of dictionaries, each representing a single ad -- from ChatGPT
            ads = [
                {'title': 'Ad 1', 'brand': 'Brand A', 'platform': 'Website',
                    'audience': 'Women 18-35', 'views': 1000, 'clicks': 50, 'conversions': 10,
                    'date': '2022-01-01'},
                {'title': 'Ad 2', 'brand': 'Brand B', 'platform': 'Social Media',
                    'audience': 'Men 25-45', 'views': 2000, 'clicks': 100, 'conversions': 20,
                    'date': '2022-01-02'},
                {'title': 'Ad 3', 'brand': 'Brand A', 'platform': 'TV',
                    'audience': 'All', 'views': 3000, 'clicks': 150, 'conversions': 30,
                    'date': '2022-01-03'},
                {'title': 'Ad 4', 'brand': 'Brand C', 'platform': 'Website',
                    'audience': 'Women 18-35', 'views': 4000, 'clicks': 200, 'conversions': 40,
                    'date': '2022-01-04'},
                {'title': 'Ad 5', 'brand': 'Brand D', 'platform': 'Social Media',
                    'audience': 'Men 25-45', 'views': 5000, 'clicks': 250, 'conversions': 50,
                    'date': '2022-01-05'},
            ]

            # Create a DataFrame from the list of dictionaries
            cls.full_df = pd.DataFrame(ads).set_index('title')
            cls.small_df = cls.full_df.sample(2, random_state=0)

            cls.full_df.to_csv(full_csv)

    def test_day_one(self):
        'Testing the function on a toy dataset'
        mean_views = m.a_function(self.full_df, "views")
        self.assertAlmostEqual(mean_views, 3000, 1)
        return mean_views

    @unittest.skip("Only enabled to run the debugger")
    def test_debug(self):
        "this also tests get tree"
