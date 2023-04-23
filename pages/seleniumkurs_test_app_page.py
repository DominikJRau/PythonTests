from selenium.webdriver.common.by import By


class SeleniumKursTestappPage:
    BTN_HAUPTMENU = (By.ID, "portaltab-burger-menu")
    LINK_TESTFORM1 = (By.LINK_TEXT, "Selenium Test Form1")
    LINK_DRAGANDDROP = (By.LINK_TEXT, "Drag and Drop Beispiel")
    LINK_IFRAME = (By.LINK_TEXT, "IFrame Beispiel")
    LINK_WEBELEMENTE = (By.LINK_TEXT, "Web Elemente")
    LINK_KATZENSUCHE = (By.LINK_TEXT, "Katzensuche Testseite (AJAX)")
    LINK_WEBSHOP = (By.LINK_TEXT, "Webshop Testseite")


    def __init__(self, driver):
        self.driver = driver

    def hauptmenu_aufrufen(self):
        self.driver.find_element(*self.BTN_HAUPTMENU).click()

    def testform1_anklicken(self):
        self.driver.find_element(*self.LINK_TESTFORM1).click()

    def draganddrop_anklicken(self):
        self.driver.find_element(*self.LINK_DRAGANDDROP).click()

    def iframe_anklicken(self):
        self.driver.find_element(*self.LINK_IFRAME).click()

    def webelemente_anklicken(self):
        self.driver.find_element(*self.LINK_WEBELEMENTE).click()

    def link_katzensuche(self):
        self.driver.find_element(*self.LINK_KATZENSUCHE).click()

    def link_webshop(self):
        self.driver.find_element(*self.LINK_WEBSHOP).click()


