import unittest
import time
from Trumpetimagepackage import trumpetimagescrape

class TestScraper(unittest.TestCase):
    def setUp(self):
        self.bot = trumpetimagescrape.Scraper()

    def test_search(self):
        actual_value = bot.driver.current_url
        expected_value = "https://www.johnpacker.co.uk/search/trumpet/"

if __name__ == '__main__':
    unittest.main(argv=[''], verbosity=2)