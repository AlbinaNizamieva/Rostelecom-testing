from pages.auth_page import AuthPage
from selenium.webdriver.common.keys import Keys
from settings import valid_password, valid_phone, valid_email, valid_login, valid_ls


def test_auth_page_phone(web_browser):
    """Авторизация по номеру телефона(позитивный сценарий)"""

    page = AuthPage(web_browser)

    page.user.send_keys(valid_phone)
    page.password.send_keys(valid_password)

    page.btn.click()

    assert page.logout_btn.is_presented()


def test_auth_page_email(web_browser):
    """Авторизация по почте (позитивный сценарий)"""

    page = AuthPage(web_browser)

    page.user.send_keys(valid_email)
    page.password.send_keys(valid_password)

    page.btn.click()

    assert page.logout_btn.is_presented()


def test_auth_page_login(web_browser):
    """Авторизация по логину (позитивный сценарий)"""

    page = AuthPage(web_browser)

    page.user.send_keys(valid_login)
    page.password.send_keys(valid_password)

    page.btn.click()

    assert page.logout_btn.is_presented()


def test_auth_page_ls(web_browser):
    """Авторизация по лицевому счету (позитивный сценарий)"""

    page = AuthPage(web_browser)

    page.user.send_keys(valid_ls)
    page.password.send_keys(valid_password)

    page.btn.click()

    assert page.logout_btn.is_presented()