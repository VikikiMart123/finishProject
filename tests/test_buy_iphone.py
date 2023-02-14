
from selenium import webdriver

from pages.finish_page import Finish_page
from pages.login_page import Login_page
from pages.main_page import Main_page
from pages.mobile_gallery_page import Mobile_page
from pages.shipping_page import Shipping_page


def test_buy_iphone():
    driver = webdriver.Chrome('C:\\Users\\VictoriaMartyanova\\PycharmProjects\\python_selenium\\chromedriver.exe')

    login = Login_page(driver)
    login.autorization()

    mp = Main_page(driver)
    mp.phone_navigation()

    mob_p = Mobile_page(driver)
    mob_p.select_apple_checkbox()

    sh_p = Shipping_page(driver)
    sh_p.select_pick_up_option()

    f = Finish_page(driver)
    f.screenshot()