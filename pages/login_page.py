
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from base.base_class import Base


class Login_page(Base):

    url = 'https://zoommer.ge//'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators

    profile = "//span[@class='welcome-text-desktop']"
    user_name = "//input[@id='EmailOrPhone']"
    password = "//*[@id='Password']"
    login_button = "//button[@id='login-btn']"
    profile_word = "//div[@class='logged_in_welcome']"

    # Gettors

    def get_profile(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.profile)))

    def get_user_name(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.user_name)))

    def get_password(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.password)))

    def get_login_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.login_button)))

    def get_profile_word(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.profile_word)))

    # Actions

    def click_profile(self):
        self.get_profile().click()
        print("Click Profile button")

    def input_user_name(self, user_name):
        self.get_user_name().send_keys(user_name)
        print("Input User name")

    def input_password(self, password):
        self.get_password().send_keys(password)
        print("Input password")

    def click_login_button(self):
        self.get_login_button().click()
        print("Click Login button")

    # Methods

    def autorization(self):
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.get_current_url()
        self.click_profile()
        self.input_user_name("1234565tur@mail.ru")
        self.input_password("fazan321")
        self.click_login_button()
        self.assert_word(self.get_profile_word(), "გამარჯობა")


