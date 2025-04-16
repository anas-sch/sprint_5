import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import WebDriverException


@pytest.fixture (scope="function")
def browser():
    options = Options()
    options.add_argument("--window-size=1920, 1080")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    driver = None
    try:
        driver = webdriver.Chrome(options=options)
        driver.set_page_load_timeout(5)
        driver.implicitly_wait(5)

        driver.get("https://stellarburgers.nomoreparties.site/")

        WebDriverWait(driver, 10).until(
            lambda b: "Stellar Burgers" in b.title,
            message = "Главная страница не прогрузилась"
        )

        yield driver

    except WebDriverException as e:
        pytest.fail(f"Ошибка инициализации браузера {str(e)}")

    finally:
        if driver:
            driver.quit()
