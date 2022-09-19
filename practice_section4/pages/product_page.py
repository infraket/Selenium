from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):

    def add_to_basket_page(self):
        button = self.browser.find_element(*ProductPageLocators.BUTTON)
        button.click()
        self.solve_quiz_and_get_code()

        assert self.is_element_present(*ProductPageLocators.BUTTON), "Button add_to_basket is not presented"


