from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import AllLocators
from data import correct_password, my_email


class TestLogin:

    def test_login_from_page(self, browser):
        browser.find_element(*AllLocators.LOGIN_BUTTON).click()
        browser.find_element(*AllLocators.LOGIN_EMAIL).send_keys(my_email)
        browser.find_element(*AllLocators.LOGIN_PASSWORD).send_keys(correct_password)
        browser.find_element(*AllLocators.LOGIN_BUTTON_SIGNIN).click()

        make_order = WebDriverWait(browser, 10).until(
            EC.visibility_of_element_located(AllLocators.MAKE_ORDER)
        )
        assert make_order.is_displayed(), "Кнопка 'Оформить заказ' не отображается — вход не удался или страница не загрузилась"

    def test_login_from_account_button(self, browser):
        browser.find_element(*AllLocators.ACCOUNT_BUTTON).click()
        browser.find_element(*AllLocators.REGISTER_LINK).click()
        browser.find_element(*AllLocators.SIGNIN_LINK).click()

        browser.find_element(*AllLocators.LOGIN_EMAIL).send_keys(my_email)
        browser.find_element(*AllLocators.LOGIN_PASSWORD).send_keys(correct_password)
        browser.find_element(*AllLocators.LOGIN_BUTTON_SIGNIN).click()

        make_order = WebDriverWait(browser, 10).until(
            EC.visibility_of_element_located(AllLocators.MAKE_ORDER)
        )
        assert make_order.is_displayed(), "Кнопка 'Оформить заказ' не отображается — вход не удался или страница не загрузилась"

    def test_login_from_password_recovery(self, browser):
        browser.find_element(*AllLocators.ACCOUNT_BUTTON).click()
        browser.find_element(*AllLocators.FORGOT_PASSWORD).click()
        browser.find_element(*AllLocators.FORGOT_BUTTON_LOGIN).click()

        browser.find_element(*AllLocators.LOGIN_EMAIL).send_keys(my_email)
        browser.find_element(*AllLocators.LOGIN_PASSWORD).send_keys(correct_password)
        browser.find_element(*AllLocators.LOGIN_BUTTON_SIGNIN).click()

        make_order = WebDriverWait(browser, 10).until(
            EC.visibility_of_element_located(AllLocators.MAKE_ORDER)
        )
        assert make_order.is_displayed(), "Кнопка 'Оформить заказ' не отображается — вход не удался или страница не загрузилась"