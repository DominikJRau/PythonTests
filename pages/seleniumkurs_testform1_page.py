from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class SeleniumKursTestform1Page:
    TEXT_UEBERSCHRIFT = (By.TAG_NAME, "h1")
    INPUT_BETREFF = (By.ID, "form-widgets-betreff")
    INPUT_NAME = (By.ID, "form-widgets-name")
    SELECT_KURS = (By.NAME, "form.widgets.auswahl1:list")
    SELECT_FIRMABOX1 = (By.ID, "form-widgets-auswahl2-from")
    BTN_FIRMAAUSWAHL = (By.NAME, "from2toButton")
    SELECT_FIRMABOX2 = (By.ID, "form-widgets-auswahl2-to")
    BTN_FIRMANACHOBENSCHIEBEN = (By.NAME, "upButton")
    BTN_FORMULARSPEICHERN = (By.NAME, "form.buttons.speichern")
    TEXT_STATUSMELDUNG = (By.ID, "message")
    TEXT_ERSTESELEMENTLISTE = (By.XPATH, "//ul[@id='companies']/li[1]")

    def __init__(self, driver):
        self.driver = driver

    def uberschrift_auslesen(self):
        return self.driver.find_element(*self.TEXT_UEBERSCHRIFT).text

    def betreff_eingeben(self, betreff):
        self.driver.find_element(*self.INPUT_BETREFF).send_keys(betreff)

    def name_eingeben(self, name):
        self.driver.find_element(*self.INPUT_NAME).send_keys(name)

    def kurs_auswaehlen(self, kursname):
        kursAuswahl = Select(self.driver.find_element(*self.SELECT_KURS))
        kursAuswahl.select_by_visible_text(kursname)

    def firma_in_box1_auswaehlen(self, auswahl):
        firmaAuswahl = Select(self.driver.find_element(*self.SELECT_FIRMABOX1))
        for i in auswahl:
            firmaAuswahl.select_by_index(i)

    def firma_uebernehmen(self):
        self.driver.find_element(*self.BTN_FIRMAAUSWAHL).click()

    def firma_in_box2_auswaehlen(self, auswahl):
        firmaAuswahl = Select(self.driver.find_element(*self.SELECT_FIRMABOX2))
        for i in auswahl:
            firmaAuswahl.select_by_index(i)

    def firma_nach_oben_schieben(self):
        self.driver.find_element(*self.BTN_FIRMANACHOBENSCHIEBEN).click()

    def formular_speichern(self):
        self.driver.find_element(*self.BTN_FORMULARSPEICHERN).click()

    def statusmeldung_auslesen(self):
        return self.driver.find_element(*self.TEXT_STATUSMELDUNG).text

    def ersteselement_auslesen(self):
        return self.driver.find_element(*self.TEXT_ERSTESELEMENTLISTE).text
