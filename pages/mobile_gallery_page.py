

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from base.base_class import Base


class Mobile_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators

    apple_checkbox = "div:nth-of-type(2) > .accordion_content > label:nth-of-type(1) > .checkmark"
    category_word = "//span[contains(text(),'Apple')]"
    range = "//div[@id='slider-range']/span[1]"
    iphone_14 = "/html//div[@id='js-filter-cont']/div[4]/div[@class='popular_products_div']" \
                "/div/div[1]/div[6]/div[@class='product_blocks']/div[@class='product_top_div']" \
                "/a[@href='/apple-iphone-14-plus-256-gb-blue']"
    iphone_14_add_cart_button = "/html//div[@id='pd-r-content']//button[@class='btn n-buy-btn']"

    # Gettors

    def get_apple_checkbox(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.apple_checkbox)))

    def get_category_word(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.category_word)))

    def get_range(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.range)))

    def get_iphone_14(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.iphone_14)))

    def get_iphone_14_add_cart_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.iphone_14_add_cart_button)))

    # Actions

    def click_apple_checkbox(self):
        self.get_apple_checkbox().click()
        print("Click apple checkbox")

    def slider_range(self):
        action = ActionChains(self.driver)
        action.click_and_hold(self.get_range()).move_by_offset(20, 0).release().perform()
        print("Slide to range")

    def click_iphone_14(self):
        self.get_iphone_14().click()
        print("Select Iphone 14")

    def add_iphone_14(self):
        self.get_iphone_14_add_cart_button().click()
        print("Add Iphone 14 to cart")

    # Method

    def select_apple_checkbox(self):

        self.get_current_url()
        self.driver.execute_script("window.scrollTo(0, 200)")
        self.click_apple_checkbox()
        self.assert_word(self.get_category_word(), "Apple")
        self.slider_range()
        self.driver.execute_script("window.scrollTo(0, 400)")
        self.click_iphone_14()
        self.assert_url("https://zoommer.ge/apple-iphone-14-plus-256-gb-blue")
        self.add_iphone_14()






