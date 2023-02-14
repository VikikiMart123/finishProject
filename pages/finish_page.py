

from base.base_class import Base


class Finish_page(Base):

    def __init__(self, driver_g):
        super().__init__(driver_g)
        self.driver_g = driver_g

    # Locators


    # Gettors


    # Actions


    # Method

    def screenshot(self):
        self.get_current_url()
        self.assert_url("https://zoommer.ge/checkout/paymentmethod?shippingMethod=CheckoutTakeIt")
        self.get_screenshot()


