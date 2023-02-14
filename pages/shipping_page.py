import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from base.base_class import Base


class Shipping_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    pick_up_option = "/html/body/div[7]/section/div[@class='content_div']" \
                     "/div[2]//form[@action='/checkout/shippingmethod']" \
                     "/div[@class='choosable_delivery_boxes']/label[2]/span[@class='checkmark']"
    confirm_button = ".blue_button.error_btn.exit_popup"
    account_info = ".add_address_block.shippingmethod_account_info > h5"

    first_name = "/html//input[@id='FirstName']"
    last_name = "/html//input[@id='LastName']"
    number_phone = "/html//input[@id='Phone']"
    ident_number_field = "/html//input[@id='IdentificationNumber']"
    branch_dropdown = ".choose_branch_field [role] [role='presentation']:nth-of-type(2)"
    tbilisi_city = ".mCSB_container > li:nth-of-type(2)"
    city_mall_point = "/html/body/div[7]/section/div[@class='content_div']" \
                      "//form[@action='/checkout/shippingmethod']/div[@class='checkout-branch']" \
                      "//div[@class='founded_branches']" \
                      "/div[3]/div/div[@class='mCSB_container']/div[2]" \
                      "/label[3]/span[@class='checkmark choose_branch_btn n-in-stock']"
    continue_button = "//div[@id='branch-next-step']/button[@class='blue_button delivery_method_continue_btn']"

    pay_by_points_bullet = "/html/body/div[@class='body']/section/div[@class='content_div']" \
                           "/div[2]//div[@class='choosable_delivery_boxes']/label[4]/span[@class='checkmark']"

    data_bank = "/html/body/div[@class='body']/section/div[@class='content_div']" \
                "//div[@class='js-bank-method']/h5[.='აირჩიეთ ბანკი']"

    payment_bank = "/html/body/div[@class='body']/section/div[@class='content_div']" \
                   "//div[@class='js-bank-method']/label[1]/span[@class='checkmark']"

    agree_to_terms_checkbox = "//label[@id='agree-to-terms']/span[@class='checkmark']"
    continue_conf_button = "/html/body/div[@class='body']/section/div[@class='content_div']//" \
                      "button[@class='blue_button delivery_method_continue_btn js-confrim-order js-confrim-order-pixel']"

    # Gettors

    def get_pick_up_option(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.pick_up_option)))

    def get_confirm_button(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, self.confirm_button)))

    def get_account_info(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, self.account_info)))

    def get_first_name(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.first_name)))

    def get_last_name(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.last_name)))

    def get_number_phone(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.number_phone)))

    def get_ident_number(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.ident_number_field)))

    def get_branch(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.branch_dropdown)))

    def get_tbilisi_city(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.tbilisi_city)))

    def get_city_mall_point(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.city_mall_point)))

    def get_continue_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.continue_button)))

    def get_pay_by_points_bullet(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.pay_by_points_bullet)))

    def get_data_bank(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.data_bank)))

    def get_payment_bank(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.payment_bank)))

    def get_agree_to_terms_checkbox(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.agree_to_terms_checkbox)))

    def get_continue_conf_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.continue_conf_button)))

    # Actions

    def click_pick_up_option(self):
        self.get_pick_up_option().click()
        print("Choose to pick up option")

    def click_confirm_button(self):
        self.get_confirm_button().click()
        print("Click to Confirm button")

    def input_first_name(self, name):
        self.get_first_name().clear()
        self.get_first_name().send_keys(name)
        print("Input First Name")

    def input_last_name(self, surname):
        self.get_last_name().clear()
        self.get_last_name().send_keys(surname)
        print("Input Last Name")

    def input_number_phone(self, number):
        self.get_number_phone().clear()
        self.get_number_phone().send_keys(number)
        print("Input number phone")

    def input_ident_number(self, ident_number):
        self.get_ident_number().clear()
        self.get_ident_number().send_keys(ident_number)
        print("Input identification number")

    def select_branch(self):
        self.get_branch().click()
        print("Choose a branch")

    def select_tbilisi_city(self):
        self.get_tbilisi_city().click()
        print("Choose a Tbilisi branch")

    def choose_city_mall_point(self):
        self.get_city_mall_point().click()
        print("Choose city mall address")

    def click_continue_button(self):
        self.get_continue_button().click()
        print("Click on Continue button")

    def select_pay_by_points_bullet(self):
        self.get_pay_by_points_bullet().click()
        print("Select Pay by points bullet")

    def select_payment_bank(self):
        self.get_payment_bank().click()
        print("Choose a payment bank")

    def select_agree_to_terms_checkbox(self):
        self.get_agree_to_terms_checkbox().click()
        print("Select a agree to terms checkbox")

    def click_to_continue_conf_button(self):
        self.get_continue_conf_button().click()
        print("Click to continue button")

    # Methods

    def select_pick_up_option(self):
        self.get_current_url()
        self.click_pick_up_option()
        self.driver.execute_script("window.scrollTo(0, 450)")
        time.sleep(5)
        self.click_confirm_button()
        self.assert_word(self.get_account_info(), "პირადი ინფრომაცია")
        self.input_first_name("Vika")
        self.input_last_name("Mart")
        self.input_number_phone("+95555110943")
        self.input_ident_number("111111")
        self.driver.execute_script("window.scrollTo(0, 800)")
        self.select_branch()
        self.select_tbilisi_city()
        self.choose_city_mall_point()
        self.click_continue_button()
        self.select_pay_by_points_bullet()
        self.assert_word(self.get_data_bank(), "აირჩიეთ ბანკი")
        self.driver.execute_script("window.scrollTo(0, 450)")
        self.select_payment_bank()
        self.select_agree_to_terms_checkbox()
        self.click_to_continue_conf_button()







