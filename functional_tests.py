from selenium import webdriver
import unittest


class HomePageTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_opens_homepage_when_opening_site(self):

        # Someone notices post about Emils portfolio website and goes ahed to check it out
        self.browser.get('http://localhost:8000')

        # Upon opening site, page title and header indicates that ir indeed is Emils portfolio website
        self.assertIn('Emils Berzs', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('Emils Berzs', header_text)


if __name__ == '__main__':
    unittest.main(warnings='ignore')
