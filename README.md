# sprint_5 - Проект автоматизации тестирования сайта https://stellarburgers.nomoreparties.site/
1. Основа для написания автотестов
- фреймворк pytest.
2. Установить зависимости - pip install -r requirements. txt.
3. Команда для запуска - pytest -v.
4. Докаторы хранятся в файле locators.py
5. Тестовые данные файле data.py
6. Тесты в папке
Tests:
- test_go_to_account.py - Переход в личный кабинет
- test_go_to_from_account.py - Переход из личного кабинета в конструктор: Переход ( по логотипу Stellar Burgers).
- test_login-py -Вход по кнопке 'Войти в аккаунт" на главной. Вход через кнопку "Личный кабинет. Вход через "Забыли пароль?"
- test_logout_from_account.py -Выход из аккаунта.
- test_registration.py - Успешная регистрация, Ошибка при некорректном пароле.
- test_section_constructor.py - Проверка переключения между разделами конструктора
