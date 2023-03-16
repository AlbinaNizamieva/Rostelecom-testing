from pages.reg_page import RegPage
from selenium.webdriver.common.keys import Keys
from settings import valid_email, valid_phone, valid_password


def test_reg_page_looks_left(web_browser):
    """Внешний вид страницы регистрации (левая часть)"""

    page = RegPage(web_browser)
    page.reg_page.click()

    assert page.logo.is_visible() # Баг
    assert page.slogan.is_visible() # Баг


def test_reg_page_looks_right(web_browser):
    """Внешний вид страницы регистрации (правая часть)"""

    page = RegPage(web_browser)
    page.reg_page.click()

    assert page.reg_title.is_visible()
    assert page.first_name.is_visible()
    assert page.last_name.is_visible()
    assert page.region.is_visible()
    assert page.address.is_visible()
    assert page.password.is_visible()
    assert page.password_conf.is_visible()
    assert page.reg_btn.is_visible()
    assert page.auth_policy.is_visible()
    assert page.link.is_visible()


def test_reg_page_region_choice(web_browser):
    """Внешний вид страницы регистрации (правая часть)"""

    page = RegPage(web_browser)
    page.reg_page.click()
    page.region.click()
    page.region_alt.click()

    assert page.region.is_visible()


def test_registration_email_positive(web_browser):
    """Регистрация по почте (позитивный сценарий)"""

    page = RegPage(web_browser)
    page.reg_page.click()
    cur_url = page.get_current_url()

    page.first_name.send_keys(257 * Keys.BACKSPACE)
    page.last_name.send_keys(257 * Keys.BACKSPACE)
    page.address.send_keys(257 * Keys.BACKSPACE)
    page.password.send_keys(257 * Keys.BACKSPACE)
    page.password_conf.send_keys(257 * Keys.BACKSPACE)

    page.first_name.send_keys('Тест')
    page.last_name.send_keys('Тестов')
    page.address.send_keys(valid_email)
    page.password.send_keys(valid_password)
    page.password_conf.send_keys(valid_password)

    page.reg_btn.click()
    assert 'Подтверждение email' in page.email_verif.get_text()
    assert page.phone_chng_btn.is_visible()
    assert page.get_current_url() != cur_url


def test_registration_phone_positive(web_browser):
    """Регистрация по телефону (позитивный сценарий)"""

    page = RegPage(web_browser)
    page.reg_page.click()
    cur_url = page.get_current_url()

    page.first_name.send_keys(257 * Keys.BACKSPACE)
    page.last_name.send_keys(257 * Keys.BACKSPACE)
    page.address.send_keys(257 * Keys.BACKSPACE)
    page.password.send_keys(257 * Keys.BACKSPACE)
    page.password_conf.send_keys(257 * Keys.BACKSPACE)

    page.first_name.send_keys('Тест')
    page.last_name.send_keys('Тестов')
    page.address.send_keys(valid_phone)
    page.password.send_keys(valid_password)
    page.password_conf.send_keys(valid_password)

    page.reg_btn.click()
    assert 'Подтверждение телефона' in page.phone_verif.get_text()
    assert page.phone_chng_btn.is_visible()
    assert page.get_current_url() != cur_url
