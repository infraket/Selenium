from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        login_link = self.browser.find_element(*LoginPageLocators.LOGIN_URL)
        login_link.click()
        # реализуйте проверку на корректный url адрес
        assert "/login" in self.open(), "login is absent in current url"

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина

        assert self.is_element_present(*LoginPageLocators.LOGIN_USERNAME), "Login form is not presented"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_USERNAME), "REGISTRATION form link is not presented"