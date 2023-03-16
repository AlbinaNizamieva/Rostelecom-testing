from pages.pswd_recovery import PassRecoveryPage
from settings import valid_phone, valid_email, valid_login, valid_ls


def test_password_recovery(web_browser):
    """Внешний вид"""

    page = PassRecoveryPage(web_browser)
    page.forgot.click()

    assert page.recovery_text.is_visible()
    assert page.msg_text.is_visible()
    assert page.agreement_text.is_visible()
    assert page.agreement_link.is_visible()
    assert page.capcha.is_visible()
    assert page.capcha_field.is_visible()
    assert page.cont.is_visible()
    assert page.back.is_visible()
    assert page.hint.is_visible()
    assert page.tabs.get_text() == ['Телефон', 'Почта', 'Логин', 'Лицевой счёт']


def test_password_recovery_fields(web_browser):
    """Работа кнопок и полей"""

    page = PassRecoveryPage(web_browser)
    page.forgot.click()

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
    page.capcha_field.click()
    phone_check = page.active_tab.get_text()

    page.tab_login.click()
    page.user.send_keys('mail@mail.com')
    page.capcha_field.click()
    mail_check = page.active_tab.get_text()

    page.tab_phone.click()
    page.user.send_keys('login')
    page.capcha_field.click()
    login_check = page.active_tab.get_text()

    page.tab_mail.click()
    page.user.send_keys('123456789123')
    page.capcha_field.click()
    ls_check = page.active_tab.get_text()
    assert phone == ['Мобильный телефон', 'Символы']
    assert mail == ['Электронная почта', 'Символы']
    assert login == ['Логин', 'Символы']
    assert ls == ['Лицевой счёт', 'Символы']
    assert phone_check == 'Телефон'
    assert mail_check == 'Почта'
    assert login_check == 'Логин'
    assert ls_check == 'Лицевой счёт'


def test_password_recovery_phone(web_browser):
    """Восстановление пароля по телефону"""

    page = PassRecoveryPage(web_browser)
    page.forgot.click()

    page.tab_phone.click()
    page.user.click()
    page.user.send_keys(valid_phone)

    assert page.sms.is_visible() # Проверка возможности выбора (БАГ)


def test_password_recovery_email(web_browser):
    """Восстановление пароля по почте"""

    page = PassRecoveryPage(web_browser)
    page.forgot.click()

    page.tab_mail.click()
    page.user.click()
    page.user.send_keys(valid_email)

    assert page.letter.is_visible() # Проверка возможности выбора (БАГ)


def test_password_recovery_login(web_browser):
    """Восстановление пароля по логину"""

    page = PassRecoveryPage(web_browser)
    page.forgot.click()

    page.tab_mail.click()
    page.user.click()
    page.user.send_keys(valid_login)

    assert page.letter.is_visible() or page.sms.is_visible() # Проверка возможности выбора (БАГ)


def test_password_recovery_ls(web_browser):
    """Восстановление пароля по ЛС"""

    page = PassRecoveryPage(web_browser)
    page.forgot.click()

    page.tab_mail.click()
    page.user.click()
    page.user.send_keys(valid_ls)

    assert page.letter.is_visible() or page.sms.is_visible() # Проверка возможности выбора (БАГ)
