import datetime


class Base():
    def __init__(self, driver):
        self.driver = driver

    """Method get current url"""

    def get_current_url(self):
        get_url = self.driver.current_url
        print("Current url " + get_url)

    """Method assert text main page"""

    def assert_word(self, word, result):
        value_word = word.text
        assert value_word == result
        print("The word is correct")

    """Method Screenshot"""

    def get_screenshot(self):
        now_date = datetime.datetime.utcnow().strftime("%Y.%m.%d.%H.%M.%S")
        name_screenshot = 'screenshot' + now_date + '.png'
        self.driver.save_screenshot(
            'C:\\Users\\VictoriaMartyanova\\PycharmProjects\\finishProject\\screenshot\\' + name_screenshot)

    """Method assert current url"""

    def assert_url(self, result):
        get_url = self.driver.current_url
        assert get_url == result
        print("The current url is correct")