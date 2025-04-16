from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import AllLocators
from data import correct_password, my_email

class TestLogout:

    def test_logout(self, browser):
        browser.find_element(*AllLocators.LOGIN_BUTTON).click()
        browser.find_element(*AllLocators.LOGIN_EMAIL).send_keys(my_email)
        browser.find_element(*AllLocators.LOGIN_PASSWORD).send_keys(correct_password)
        browser.find_element(*AllLocators.LOGIN_BUTTON_SIGNIN).click()
        browser.find_element(*AllLocators.ACCOUNT_BUTTON).click()
        WebDriverWait(browser, 5).until(
            EC.visibility_of_element_located(AllLocators.LOGOUT_BUTTON)
        ).click()

        login_button_signin = WebDriverWait(browser, 10).until(
            EC.visibility_of_element_located(AllLocators.LOGIN_BUTTON_SIGNIN)
        )
        assert login_button_signin.is_displayed(), "Кнопка 'Войти' не отображается — пользователь не вышел из аккаунта"
