import pytest
from pages.auth_page import AuthPage


def test_auth_page_look(web_browser):
    """Внешний вид страницы"""

    page = AuthPage(web_browser)

    # Правильно ли отображаются формы ввода
    page.tab_phone.click()
    phone = page.forms.get_text()

    page.tab_mail.click()
    mail = page.forms.get_text()

    page.tab_login.click()
    login = page.forms.get_text()

    page.tab_ls.click()
    ls = page.forms.get_text()

    # Переключаются ли табы автоматически
    page.tab_mail.click()
    page.user.send_keys('+79999999999')
    page.password.click()
    phone_check = page.active_tab.get_text()

    page.user.send_keys('mail@mail.com')
    page.password.click()
    mail_check = page.active_tab.get_text()

    page.user.send_keys('login')
    page.password.click()
    login_check = page.active_tab.get_text()

    page.tab_mail.click()
    page.user.send_keys('123456789123')
    page.password.click()
    ls_check = page.active_tab.get_text()

    assert page.right_side.get_text() == 'Авторизация'
    assert page.tabs.get_text() == ['Телефон', 'Почта', 'Логин', 'Лицевой счёт']
    assert phone == ['Мобильный телефон', 'Пароль']
    assert mail == ['Электронная почта', 'Пароль']
    assert login == ['Логин', 'Пароль']
    assert ls == ['Лицевой счёт', 'Пароль']
    assert page.left_side.get_text() == 'Личный кабинет\nПерсональный помощник в цифровом мире Ростелекома'
    assert phone_check == 'Телефон'
    assert mail_check == 'Почта'
    assert login_check == 'Логин'
    assert ls_check == 'Лицевой счёт'
    assert page.forgot_passive.is_visible()
    assert page.temp_code.is_visible() # Баг

