from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_USERNAME = (By.CSS_SELECTOR, "#id_login-username.form-control")
    REGISTRATION_USERNAME = (By.CSS_SELECTOR, "#id_registration-email")
    LOGIN_URL = (By.CSS_SELECTOR, "#login_link")


class ProductPageLocators():
    BUTTON = (By.CSS_SELECTOR, "#add_to_basket_form")
