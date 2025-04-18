from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import AllLocators
from data import name, incorrect_password
from helpers import new_email, new_password

class TestRegistration:
    def test_successful_registration(self, browser):
        browser.find_element(*AllLocators.ACCOUNT_BUTTON).click()
        browser.find_element(*AllLocators.REGISTER_LINK).click()

        browser.find_element(*AllLocators.REGISTER_NAME).send_keys(name)
        browser.find_element(*AllLocators.REGISTER_EMAIL).send_keys(new_email)
        browser.find_element(*AllLocators.LOGIN_PASSWORD).send_keys(new_password)
        browser.find_element(*AllLocators.REGISTER_BUTTON).click()

        success_element = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located(AllLocators.LOGIN_BUTTON_SIGNIN),
            message="Кнопка входа не появилась после регистрации"
        )
        assert success_element.is_displayed(), "Регистрация не удалась: кнопка входа не отображается"

    def test_failed_registration(self, browser):
        browser.find_element(*AllLocators.ACCOUNT_BUTTON).click()
        browser.find_element(*AllLocators.REGISTER_LINK).click()

        browser.find_element(*AllLocators.REGISTER_NAME).send_keys(name)
        browser.find_element(*AllLocators.REGISTER_EMAIL).send_keys(new_email)
        browser.find_element(*AllLocators.LOGIN_PASSWORD).send_keys(incorrect_password)
        browser.find_element(*AllLocators.REGISTER_BUTTON).click()

        error_message = WebDriverWait(browser, 10).until(
            EC.visibility_of_element_located(AllLocators.ERROR_PASSWORD)
        )
        assert error_message.is_displayed(), "Ошибка 'Некорректный пароль' не отобразилась"