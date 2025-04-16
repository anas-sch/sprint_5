from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import AllLocators

class TestConstructor:
    def test_constructor_section_navigation(self, browser):
        SECTIONS = {
            "Соусы": AllLocators.SAUCE_SECTION,
            "Начинки": AllLocators.TOPPINGS_SECTION,
            "Булки": AllLocators.BUNS_SECTION
        }

        for section_name, section_locator in SECTIONS.items():
            try:
                element = WebDriverWait(browser, 10).until(
                    EC.presence_of_element_located(section_locator)
                )
                element.click()

                active_section = WebDriverWait(browser, 10).until(
                    EC.presence_of_element_located(AllLocators.ACTIVE_SECTION)
                )
                assert section_name in active_section.text

            except Exception as e:
                print(f"Ошибка при работе с разделом '{section_name}':")
                print(f"Локатор: {section_locator}")
                print(f"Ошибка: {str(e)}")
                raise

