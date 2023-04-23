import unittest

from selenium import webdriver


from pages.seleniumkurs_home_page import SeleniumKursHomePage
from pages.seleniumkurs_login_page import SeleniumKursLoginPage
from pages.seleniumkurs_test_app_page import SeleniumKursTestappPage
from pages.seleniumkurs_webshop_agb_page import SeleniumKursWebShopAGBPage
from pages.seleniumkurs_webshop_kasse_page import SeleniumKursWebShopKassePage
from pages.seleniumkurs_webshop_produkte_page import SeleniumKursWebShopProduktePage


class TestWebShopSeleniumKursFirefox(unittest.TestCase):

    def setUp(self) -> None:
        print("Initialisiere Webdriver")
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(2)
        self.driver.maximize_window()
        self.driver.get("https://seleniumkurs.codingsolo.de")


    def tearDown(self) -> None:
        print("Test abgeschlossen")
        #self.driver.close()

    def test_webshop(self):
        print("Starte den Webshop Test")

        ## Arrange

        ## Login

        loginPage = SeleniumKursLoginPage(self.driver)
        loginPage.zugangsdaten_eingeben("selenium42", "R5vxI0j60")
        loginPage.login_button_anklicken()

        ## Navigation zum Webshop

        homePage = SeleniumKursHomePage(self.driver)
        homePage.hauptmenu_aufrufen()
        homePage.link_seleniumtestapps_aufrufen()

        testappPage = SeleniumKursTestappPage(self.driver)
        testappPage.link_webshop()

        ## Act

        webshopProduktePage = SeleniumKursWebShopProduktePage(self.driver)
        webShopKassenPage = SeleniumKursWebShopKassePage(self.driver)
        webShopAGBPage = SeleniumKursWebShopAGBPage(self.driver)

        webshopProduktePage.produkt_suche_ausfuehren("Brems")

        webshopProduktePage.produkt_anzahl_auswaehlen("Bremssattel Hinten Audi", 4)
        webshopProduktePage.produkt_in_warenkorb_legen("Bremssattel Hinten Audi")

        webshopProduktePage.produkt_anzahl_auswaehlen("Bremsscheiben Set Vorne Audi", 2)
        webshopProduktePage.produkt_in_warenkorb_legen("Bremsscheiben Set Vorne Audi")

        preis1 = webshopProduktePage.preis_auslesen()

        webshopProduktePage.warenkorb_aufklappen()
        webshopProduktePage.kasse_anklicken()

        webShopKassenPage.coupon_eingeben("codingsolo")
        webShopKassenPage.coupon_aktivieren()
        promoinfo = webShopKassenPage.promocode_auslesen()
        preis2 = webShopKassenPage.preis_auslesen()

        webShopKassenPage.bestellen_klicken()

        webShopAGBPage.land_auswaehlen("Germany")
        webShopAGBPage.agb_anklicken()
        webShopAGBPage.weiter_anklicken()

        ## Assert

        self.assertEqual(preis1, "760.58")

        self.assertTrue("aktiviert" in promoinfo)

        self.assertEqual(preis2, "684")


if __name__ == '__main__':
    main()









