from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class SeleniumKursWebShopKassePage:

    INPUT_COUPON = (By.CSS_SELECTOR, ".promoCode")
    BTN_COUPON = (By.CSS_SELECTOR, ".promoBtn")
    TEXT_PROMO = (By.CSS_SELECTOR, ".promoInfo")
    TEXT_PREIS = (By.CSS_SELECTOR, ".discountAmt")
    BTN_BESTELLEN = (By.CSS_SELECTOR, "div > button:last-child")


    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 6)

    def coupon_eingeben(self, code):
        self.driver.find_element(*self.INPUT_COUPON).send_keys(code)

    def coupon_aktivieren(self):
        self.driver.find_element(*self.BTN_COUPON).click()

    def promocode_auslesen(self):
        return self.wait.until(EC.element_to_be_clickable(self.TEXT_PROMO)).text

    def preis_auslesen(self):
        return self.driver.find_element(*self.TEXT_PREIS).text

    def bestellen_klicken(self):
        self.driver.find_element(*self.BTN_BESTELLEN).click()











