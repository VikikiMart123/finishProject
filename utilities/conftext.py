import pytest
from selenium.webdriver.chrome import webdriver


@pytest.fixture()
def set_up():
    print("Start test")
    yield
    print("Finish test")