from selenium.webdriver.common.by import By
import time

BASIC_URL = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'


def test_get_button(browser):
    browser.get(BASIC_URL)
    time.sleep(30)
    btn = browser.find_element(By.ID, "add_to_basket_form")
    assert btn, "Button not"
