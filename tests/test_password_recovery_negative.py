from pages.pswd_recovery import PassRecoveryPage
from fields import phone_field, email_field, login_field, ls_field


def test_password_recovery_phone_negative(web_browser):
    """Восстановление пароля по телефону (негативный сценарий)"""

    page = PassRecoveryPage(web_browser)
    page.forgot.click()

    page.tab_phone.click()
    page.user.click()
    for item in phone_field:
        page.user.send_keys(item)
        page.cont.click()
        assert page.err_msg.is_visible()
        assert 'Неверный логин или текст с картинки' in page.err_msg.get_text()



def test_password_recovery_email_negative(web_browser):
    """Восстановление пароля по почте (негативный сценарий)"""

    page = PassRecoveryPage(web_browser)
    page.forgot.click()

    page.tab_mail.click()
    page.user.click()
    for item in email_field:
        page.user.send_keys(item)
        page.cont.click()
        assert page.err_msg.is_visible()
        assert 'Неверный логин или текст с картинки' in page.err_msg.get_text()


def test_password_recovery_login_negative(web_browser):
    """Восстановление пароля по логину (негативный сценарий)"""

    page = PassRecoveryPage(web_browser)
    page.forgot.click()

    page.tab_login.click()
    page.user.click()
    for item in login_field:
        page.user.send_keys(item)
        page.cont.click()
        assert page.err_msg.is_visible()
        assert 'Неверный логин или текст с картинки' in page.err_msg.get_text()


def test_password_recovery_ls_negative(web_browser):
    """Восстановление пароля по лицевому счету (негативный сценарий)"""

    page = PassRecoveryPage(web_browser)
    page.forgot.click()

    page.tab_ls.click()
    page.user.click()
    for item in ls_field:
        page.user.send_keys(item)
        page.cont.click()
        assert page.err_msg.is_visible()
        assert 'Неверный логин или текст с картинки' in page.err_msg.get_text()