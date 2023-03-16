from pages.auth_page import AuthPage
from selenium.webdriver.common.keys import Keys
from fields import phone_field, pswd, email_field, login_field, ls_field


def test_auth_page_phone_negative(web_browser):
    """Авторизация по номеру телефона (негативный сценарий)"""

    page = AuthPage(web_browser)

    for i in phone_field:
        for j in pswd:
            if page.capcha.is_visible():
                page.user.send_keys(i)
                # page.password.send_keys(32 * Keys.BACKSPACE) # Если поля не очищяются
                page.password.send_keys(j)
                page.btn.click()
                assert page.err_msg.get_text() == 'Неверно введен текст с картинки'

            else:
                page.user.send_keys(i)
                # page.password.send_keys(32 * Keys.BACKSPACE) # Если поля не очищяются
                page.password.send_keys(j)
                page.btn.click()
                assert page.err_msg.get_text() == 'Неверный логин или пароль'

            assert page.err_msg.is_visible()
            assert page.forgot_active.is_visible() # Проверяем перекрашивание "Забыл пароль"


def test_auth_page_mail_negative(web_browser):
    """Авторизация по почте (негативный сценарий)"""

    page = AuthPage(web_browser)
    page.tab_mail.click()

    for i in email_field:
        for j in pswd:
            if page.capcha.is_visible():
                page.user.send_keys(i)
                # page.password.send_keys(32 * Keys.BACKSPACE) # Если поля не очищяются
                page.password.send_keys(j)
                page.btn.click()
                assert page.err_msg.get_text() == 'Неверно введен текст с картинки'

            else:
                page.user.send_keys(i)
                # page.password.send_keys(32 * Keys.BACKSPACE) # Если поля не очищяются
                page.password.send_keys(j)
                page.btn.click()
                assert page.err_msg.get_text() == 'Неверный логин или пароль'

            assert page.err_msg.is_visible()
            assert page.forgot_active.is_visible() # Проверяем перекрашивание "Забыл пароль"


def test_auth_page_login_negative(web_browser):
    """Авторизация по логину (негативный сценарий)"""

    page = AuthPage(web_browser)
    page.tab_login.click()

    for i in login_field:
        for j in pswd:
            if page.capcha.is_visible():
                page.user.send_keys(i)
                # page.password.send_keys(32 * Keys.BACKSPACE) # Если поля не очищяются
                page.password.send_keys(j)
                page.btn.click()
                assert page.err_msg.get_text() == 'Неверно введен текст с картинки'

            else:
                page.user.send_keys(i)
                # page.password.send_keys(32 * Keys.BACKSPACE) # Если поля не очищяются
                page.password.send_keys(j)
                page.btn.click()
                assert page.err_msg.get_text() == 'Неверный логин или пароль'

            assert page.err_msg.is_visible()
            assert page.forgot_active.is_visible() # Проверяем перекрашивание "Забыл пароль"


def test_auth_page_ls_negative(web_browser):
    """Авторизация по лицевому счету (негативный сценарий)"""

    page = AuthPage(web_browser)
    page.tab_ls.click()

    for i in ls_field:
        for j in pswd:
            if page.capcha.is_visible():
                page.user.send_keys(i)
                # page.password.send_keys(32 * Keys.BACKSPACE) # Если поля не очищяются
                page.password.send_keys(j)
                page.btn.click()
                assert page.err_msg.get_text() == 'Неверно введен текст с картинки'

            else:
                page.user.send_keys(i)
                # page.password.send_keys(32 * Keys.BACKSPACE) # Если поля не очищяются
                page.password.send_keys(j)
                page.btn.click()
                assert page.err_msg.get_text() == 'Неверный логин или пароль'

            assert page.err_msg.is_visible()
            assert page.forgot_active.is_visible() # Проверяем перекрашивание "Забыл пароль"

