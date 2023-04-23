from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


class SeleniumKursWebShopAGBPage:

    SELECT_LAND = (By.CSS_SELECTOR, "select")
    CHECK_AGB = (By.CSS_SELECTOR, ".chkAgree")
    BTN_WEITER = (By.CSS_SELECTOR, "div > button")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 6)

    def land_auswaehlen(self, land):
        land_auswahl = Select(self.driver.find_element(*self.SELECT_LAND))
        land_auswahl.select_by_value(land)

    def agb_anklicken(self):
        self.driver.find_element(*self.CHECK_AGB).click()

    def weiter_anklicken(self):
        self.driver.find_element(*self.BTN_WEITER).click()
















