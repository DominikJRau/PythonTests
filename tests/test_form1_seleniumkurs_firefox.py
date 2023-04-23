import json
import requests

from parameterized import parameterized_class
from selenium import webdriver
import unittest

from pages.seleniumkurs_home_page import SeleniumKursHomePage
from pages.seleniumkurs_login_page import SeleniumKursLoginPage
from pages.seleniumkurs_test_app_page import SeleniumKursTestappPage
from pages.seleniumkurs_testform1_page import SeleniumKursTestform1Page


url = 'https://github.com/DominikJRau/PythonTests/blob/main/tests/test_config.json'

response = requests.get(url)
if response.status_code == 200:
    with open('C:/drivers/test_config.json', 'wb') as f:
        f.write(response.content)
        print("Die 'test_config.json'-Datei wurde erfolgreich heruntergeladen und gespeichert.")
else:
    print("Fehler beim Herunterladen der 'test_config.json'-Datei:", response.status_code)

# Laden der 'test_config.json'-Datei und Verwendung mit @parameterized_class-Decorator
config_file = open('C:/drivers/test_config.json', 'r')
config = json.load(config_file)

# Verwendung des 'tests'-Schlüssels aus der 'test_config.json'-Datei im @parameterized_class-Decorator
@parameterized_class(config['tests'])

#@parameterized_class(json.load(open('https://github.com/DominikJRau/PythonTests/blob/main/tests/test_config.json'))['tests'])

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

        homePage = SeleniumKursHomePage(self.driver)
        homePage.hauptmenu_aufrufen()
        homePage.link_seleniumtestapps_aufrufen()

        testappPage = SeleniumKursTestappPage(self.driver)
        testappPage.testform1_anklicken()
        testformPage = SeleniumKursTestform1Page(self.driver)
        testformPage.betreff_eingeben(self.betreff)
        testformPage.name_eingeben(self.name)
        testformPage.kurs_auswaehlen(self.kurstitel)
        testformPage.firma_in_box1_auswaehlen(self.firmenbox1)
        testformPage.firma_uebernehmen()
        testformPage.firma_in_box2_auswaehlen(self.firmenbox2)
        testformPage.firma_nach_oben_schieben()

        # Act

        testformPage.formular_speichern()

        # Assert

        erfolg = testformPage.statusmeldung_auslesen()
        self.assertTrue(self.assert1 in erfolg)

        erstesElement = testformPage.ersteselement_auslesen()
        self.assertTrue(self.assert2 in erstesElement)



if __name__ == '__main__':
    main()
