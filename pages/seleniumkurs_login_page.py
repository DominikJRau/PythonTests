from selenium.webdriver.common.by import By

class SeleniumKursLoginPage:

        INPUT_BENUTZERNAME = (By.CSS_SELECTOR, "input.form-control[type='text']")
        INPUT_PASSWORT = (By.CSS_SELECTOR, "input.form-control[type='password']")
        BTN_ANMELDUNG = (By.CSS_SELECTOR, "input.btn-primary")
        STATUS_ANMELDUNG = (By.CSS_SELECTOR, "div.portalMessage:nth-child(1)")

        def __init__(self, driver):
                self.driver = driver

        def zugangsdaten_eingeben(self, benutzername, passwort):
                self.driver.find_element(*self.INPUT_BENUTZERNAME).send_keys(benutzername)
                self.driver.find_element(*self.INPUT_PASSWORT).send_keys(passwort)

        def login_button_anklicken(self):
                self.driver.find_element(*self.BTN_ANMELDUNG).click()

        def statusmeldung_auslesen(self):
                return self.driver.find_element(*self.STATUS_ANMELDUNG).text

