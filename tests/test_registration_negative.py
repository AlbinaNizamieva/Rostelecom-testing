from pages.reg_page import RegPage
from selenium.webdriver.common.keys import Keys
from settings import valid_phone, valid_password
from fields import data


def test_reg_password_negative(web_browser):
    """Регистрация с несовпадающими паролями"""

    page = RegPage(web_browser)
    page.reg_page.click()
    cur_url = page.get_current_url()


    page.first_name.send_keys('Тест')
    page.last_name.send_keys('Тестов')
    page.address.send_keys(valid_phone)
    page.password.send_keys(valid_password)
    page.password_conf.send_keys(f'{valid_password}1')
    page.reg_btn.click()
    assert page.wrong_pass_conf.get_text() == "Пароли не совпадают"
    assert page.wrong_pass_conf.is_visible()
    assert page.get_current_url() == cur_url


def test_reg_empty_negative(web_browser):
    """Регистрация с пустыми полями"""

    page = RegPage(web_browser)
    page.reg_page.click()
    cur_url = page.get_current_url()

    page.first_name.send_keys(32 * Keys.BACKSPACE)
    page.last_name.send_keys(32 * Keys.BACKSPACE)
    page.address.send_keys(32 * Keys.BACKSPACE)
    page.password.send_keys(32 * Keys.BACKSPACE)
    page.password_conf.send_keys(32 * Keys.BACKSPACE)
    page.reg_btn.click()

    assert 'Необходимо заполнить поле кириллицей. От 2 до 30 символов.' in page.wrong_fname.get_text()
    assert 'Необходимо заполнить поле кириллицей. От 2 до 30 символов.' in page.wrong_lname.get_text()
    assert 'Введите телефон в формате +7ХХХХХХХХХХ или +375XXXXXXXXX, или email в формате example@email.ru' in page.wrong_addr.get_text()
    assert 'Длина пароля должна быть не менее 8 символов' in page.wrong_pass.get_text()
    assert 'Длина пароля должна быть не менее 8 символов' in page.wrong_pass_conf.get_text()
    assert page.wrong_lname.is_visible()
    assert page.wrong_addr.is_visible()
    assert page.wrong_pass.is_visible()
    assert page.wrong_pass_conf.is_visible()
    assert page.get_current_url() == cur_url


def test_reg_fields_negative(web_browser):
    """Регистрация с некорректными данными"""

    page = RegPage(web_browser)
    page.reg_page.click()
    cur_url = page.get_current_url()

    for item in data:
        page.first_name.send_keys(32 * Keys.BACKSPACE)
        page.last_name.send_keys(32 * Keys.BACKSPACE)
        page.address.send_keys(32 * Keys.BACKSPACE)
        page.password.send_keys(32 * Keys.BACKSPACE)
        page.password_conf.send_keys(32 * Keys.BACKSPACE)

        page.first_name.send_keys(item[0])
        page.last_name.send_keys(item[1])
        page.address.send_keys(item[2])
        page.password.send_keys(item[3])
        page.password_conf.send_keys(item[3])

        page.reg_btn.click()

        if item[0] != 'Тест':
            assert 'Необходимо заполнить поле кириллицей. От 2 до 30 символов.' in page.wrong_fname.get_text()

        if item[1] != 'Тестов':
            assert page.wrong_lname.is_visible()
            assert 'Необходимо заполнить поле кириллицей. От 2 до 30 символов.' in page.wrong_lname.get_text()

        if item[2] != 'alb9061@yandex.ru' and item[2] != '+79179023150':
            assert page.wrong_addr.is_visible()
            assert 'Введите телефон в формате +7ХХХХХХХХХХ или +375XXXXXXXXX, или email в формате example@email.ru' in page.wrong_addr.get_text()

        if len(item[3]) < 8:
            assert page.wrong_pass.is_visible()
            assert page.wrong_pass_conf.is_visible()
            assert 'Длина пароля должна быть не менее 8 символов' in page.wrong_pass.get_text()
            assert 'Длина пароля должна быть не менее 8 символов' in page.wrong_pass_conf.get_text()

        if len(item[3]) > 20:
            assert page.wrong_pass.is_visible()
            assert page.wrong_pass_conf.is_visible()
            assert 'Длина пароля должна быть не более 20 символов' in page.wrong_pass.get_text()
            assert 'Длина пароля должна быть не более 20 символов' in page.wrong_pass_conf.get_text()

        if item[3] == 'абвгдеёж':
            assert page.wrong_pass.is_visible()
            assert page.wrong_pass_conf.is_visible()
            assert 'Пароль должен содержать только латинские буквы' in page.wrong_pass.get_text()
            assert 'Пароль должен содержать только латинские буквы' in page.wrong_pass_conf.get_text()

        if item[3] == '为人民服务为人民服务1Gg':
            assert page.wrong_pass.is_visible()
            assert page.wrong_pass_conf.is_visible()
            assert 'Пароль должен содержать только латинские буквы' in page.wrong_pass.get_text()
            assert 'Пароль должен содержать только латинские буквы' in page.wrong_pass_conf.get_text()

        if item[3] == 'ABCDEFGH1':
            assert page.wrong_pass.is_visible()
            assert page.wrong_pass_conf.is_visible()
            assert 'Пароль должен содержать хотя бы одну прописную букву' in page.wrong_pass.get_text()
            assert 'Пароль должен содержать хотя бы одну прописную букву' in page.wrong_pass_conf.get_text()

        if item[3] == 'Abcdefgh':
            assert page.wrong_pass.is_visible()
            assert page.wrong_pass_conf.is_visible()
            assert 'Пароль должен содержать хотя бы 1 спецсимвол или хотя бы одну цифру' in page.wrong_pass.get_text()
            assert 'Пароль должен содержать хотя бы 1 спецсимвол или хотя бы одну цифру' in page.wrong_pass_conf.get_text()

        if item[3] == '!!@$#%!!@$#%' or item[3] == 'abcdefgh1':
            assert page.wrong_pass.is_visible()
            assert page.wrong_pass_conf.is_visible()
            assert 'Пароль должен содержать хотя бы одну заглавную букву' in page.wrong_pass.get_text()
            assert 'Пароль должен содержать хотя бы одну заглавную букву' in page.wrong_pass_conf.get_text()

        assert page.get_current_url() == cur_url
