from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import AllLocators


class TestGoToAccount:
    def test_account_page_access(self, browser):
        browser.find_element(*AllLocators.ACCOUNT_BUTTON).click()

        signin_header = WebDriverWait(browser, 10).until(
            EC.visibility_of_element_located(AllLocators.LOGIN_BUTTON_SIGNIN)
        )

        assert signin_header.is_displayed(), 'Заголовок "Вход" не отображается'