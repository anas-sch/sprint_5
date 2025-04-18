from selenium.webdriver.common.by import By

class AllLocators:
    # Главная
    ACCOUNT_BUTTON = (By.XPATH, '//a[@href="/account"]')  # Личный кабинет
    LOGIN_BUTTON = (By.XPATH, '//button[contains(@class, "button_button_size_large") and text()="Войти в аккаунт"]') # Войти в аккаунт

    #Конструктор (табы)
    BUNS_SECTION = (By.XPATH, '//div[contains(@class, "tab") and .="Булки"]') #раздел Булки
    SAUCE_SECTION = (By.XPATH, '//div[contains(@class, "tab") and .="Соусы"]')# раздел Соусы
    TOPPINGS_SECTION = (By.XPATH, '//div[contains(@class, "tab") and .="Начинки"]')  #раздел Начинки

    #Активные табы
    MAKE_ORDER = (By.XPATH, '//button[contains(text(),"Оформить заказ")]') #Оформить заказ
    ACTIVE_SECTION = (By.XPATH, '//div[contains(@class, "tab_tab_type_current")]') #блок с навигацией

    #Логин
    LOGIN_EMAIL = (By.XPATH, "//input [@name= 'name']") #Email
    LOGIN_PASSWORD = (By.XPATH, "//input[@type='password' and @name='Пароль']") #Пароль, можно использовать в Регистрации
    LOGIN_BUTTON_SIGNIN = (By.XPATH, "//button[contains(text(), 'Войти')]") #Войти
    REGISTER_LINK = (By.XPATH, "//a[@href='/register']") #Зарегистрироваться (ссылка)
    FORGOT_PASSWORD = (By.XPATH,  "//a[contains (text(), 'Восстановить пароль' )]") #Восстановить пароль
    FORGOT_BUTTON_LOGIN = (By.XPATH, "// a[ @ href = '/login' and text() = 'Войти']") #кнопка Войти с "Забыли пароль?"
    CONSTRUCTOR_BUTTON = (By.LINK_TEXT, "Конструктор") #кнопка конструктора
    HEADER_LOGO = (By.CLASS_NAME, "AppHeader_header__logo__2D0X2") #лого Stellar
    HEADER_LOGIN = (By.XPATH, "//h2[contains (text),'Вход')]") #Вход (заголовок)

    #Регистрация
    REGISTER_NAME = (By.XPATH, "//label[text()='Имя']/following-sibling::input")  # Имя
    REGISTER_EMAIL = (By.XPATH, "//label[text()='Email']/following-sibling::input")  # Email
    REGISTER_BUTTON = (By.XPATH, "//button[text()='Зарегистрироваться']")  # Зарегистрироваться
    ERROR_PASSWORD = (By.XPATH, "//p[contains(@class, 'input__error') and contains(text(), 'Некорректный пароль')]")  # Некорректный пароль
    SIGNIN_LINK = (By.XPATH, "//a[contains (text(), 'Войти')]")  # Войти (можно использовать на странице забыли пароль)

    #Выход
    LOGOUT_BUTTON = (By.XPATH, "//button[@type='button' and text()='Выход']")