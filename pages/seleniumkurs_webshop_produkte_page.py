from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class SeleniumKursWebShopProduktePage:

    INPUT_PRODUKTSUCHE = (By.XPATH, "//input[contains(@placeholder, 'Hier')]")
    TEXT_PREIS = (By.XPATH, "//tbody/tr[last()]//strong")
    BTN_WARENKORB = (By.CSS_SELECTOR, ".cart-icon")
    BTN_KASSE = (By.CSS_SELECTOR, "div.cart-preview > div.action-block button")


    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 5)

    def produkt_suche_ausfuehren(self, name):
        self.driver.find_element(*self.INPUT_PRODUKTSUCHE).send_keys(name)

    def produkt_anzahl_auswaehlen(self, name, anzahl):
        btn_plus = self.driver.find_element(By.XPATH, "//*[text() = '{}']/..//*[@class = 'increment']".format(name))

        for i in range(anzahl-1):
            btn_plus.click()

    def produkt_in_warenkorb_legen(self, name):
        btn_warenkorb = self.driver.find_element(By.XPATH, "//*[text() = '{}']/..//*[@type = 'button']".format(name))
        btn_warenkorb.click()

    def preis_auslesen(self):
        return self.driver.find_element(*self.TEXT_PREIS).text

    def warenkorb_aufklappen(self):
        self.driver.find_element(*self.BTN_WARENKORB).click()

    def kasse_anklicken(self):
        self.driver.find_element(*self.BTN_KASSE).click()




