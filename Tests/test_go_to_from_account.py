from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import AllLocators

class TestGoTo:
    def test_return_to_constructor(self, browser):
        browser.find_element(*AllLocators.ACCOUNT_BUTTON).click()
        constructor_button = WebDriverWait(browser, 10).until(
            EC.visibility_of_element_located(AllLocators.CONSTRUCTOR_BUTTON)
        )
        constructor_button.click()

        make_order_button = WebDriverWait(browser, 10).until(
            EC.visibility_of_element_located(AllLocators.LOGIN_BUTTON_SIGNIN)
        )
        assert make_order_button.is_displayed(), "Не вернулись в конструктор через кнопку 'Конструктор'"

    def test_return_with_logo(self, browser):
        browser.find_element(*AllLocators.ACCOUNT_BUTTON).click()
        logo = WebDriverWait(browser, 10).until(
            EC.visibility_of_element_located(AllLocators.HEADER_LOGO)
        )
        logo.click()

        make_order_button = WebDriverWait(browser, 10).until(
            EC.visibility_of_element_located(AllLocators.LOGIN_BUTTON_SIGNIN)
        )
        assert make_order_button.is_displayed(), "Не вернулись в конструктор через логотип"