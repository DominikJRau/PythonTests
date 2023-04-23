from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class WebdeLoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.username_textbox = (By.ID, "freemailLoginUsername")
        self.password_textbox = (By.ID, "freemailLoginPassword")
        self.login_button = (By.XPATH, "//button[contains(text(),'Login')]")
        self.ad_banner_button = (By.ID, "save-all-pur")

    def switch_to_outer_iframe(self):
        # Index des iFrames (0-basiert)
        WebDriverWait(self.driver, 10).until(EC.frame_to_be_available_and_switch_to_it(0))
        print("switched to outer-iframe")

    def switch_to_inner_iframe(self):
        # Index des iFrames (0-basiert)
        WebDriverWait(self.driver, 10).until(EC.frame_to_be_available_and_switch_to_it(0))
        print("switched to inner iframe")

    def click_ad_banner_button(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.ad_banner_button)).click()
        self.driver.switch_to.default_content()
        print("habe Button geklickt")

    def enter_username(self, username):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.username_textbox)).send_keys(username)

    def enter_password(self, password):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.password_textbox)).send_keys(password)

    def click_login_button(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.login_button)).click()
