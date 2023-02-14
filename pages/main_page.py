
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from base.base_class import Base


class Main_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators

    navigation_menu = "//div[@class='navigation-header']"
    mobile_phones = "//li[@data-show-id='1']"

    # Gettors

    def get_navigation_menu(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.navigation_menu)))

    def get_mobile_phones(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.mobile_phones)))

    # Actions

    def click_navigation_menu(self):
        self.get_navigation_menu().click()
        print("Click Navigation menu")

    def click_mobile_phones(self):
        self.get_mobile_phones().click()
        print("Click mobile phones button")


    # Method

    def phone_navigation(self):
        self.get_current_url()
        self.click_navigation_menu()
        self.click_mobile_phones()
        self.assert_url("https://zoommer.ge/mobilurebi-2?orderby=30")


