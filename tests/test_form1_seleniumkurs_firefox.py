import json

from parameterized import parameterized_class
from selenium import webdriver

import unittest

from pages.seleniumkurs_home_page import SeleniumKursHomePage
from pages.seleniumkurs_login_page import SeleniumKursLoginPage
from pages.seleniumkurs_test_app_page import SeleniumKursTestappPage
from pages.seleniumkurs_testform1_page import SeleniumKursTestform1Page

# Laden der 'test_config.json'-Datei und Verwendung mit @parameterized_class-Decorator
#config_file = open('C:/drivers/test_config.json', 'r')
#config = json.load(config_file)

# Verwendung des 'tests'-Schlüssels aus der 'test_config.json'-Datei im @parameterized_class-Decorator
#@parameterized_class(config['tests'])

#@parameterized_class(json.load(open('https://github.com/DominikJRau/PythonTests/blob/main/tests/test_config.json'))['tests'])

@parameterized_class([
    {"username": "selenium102", "password": "codingsolo", "betreff": "Parametrisierter Test 1", "name": "Dieter",
     "kurstitel": "Java Grundlagen Kurs mit Dieter", "firmenbox1": [2, 4, 6], "firmenbox2": [2],
     "assert1": "Java Grundlagen Kurs",
     "assert2": "Magazzini Alimentari Riuniti"},
    {"username": "selenium102", "password": "codingsolo", "betreff": "Parametrisierter Test 1", "name": "Miriam",
     "kurstitel": "Python Grundlagen Kurs mit Dieter", "firmenbox1": [2, 4, 6], "firmenbox2": [2],
     "assert1": "Python Grundlagen Kurs",
     "assert2": "Magazzini Alimentari Riuniti"}
])

class TestLoginParametrisiertSeleniumkursFirefox(unittest.TestCase):

    def setUp(self) -> None:
        print("Initialisiere Webdriver für Test")
        self.driver = webdriver.Firefox()
        self.driver.get("https://seleniumkurs.codingsolo.de")

    def tearDown(self) -> None:
        print("Nach dem Test. Ich räume auf")
        # self.driver.close()

    def test_login(self):
        print("Starte den Form1 Test")

        # Arrange

        loginPage = SeleniumKursLoginPage(self.driver)
        loginPage.zugangsdaten_eingeben(self.username, self.password)
        loginPage.login_button_anklicken()

if __name__ == '__main__':
    main()
