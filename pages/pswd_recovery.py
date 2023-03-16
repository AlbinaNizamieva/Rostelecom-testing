#!/usr/bin/python3
# -*- encoding=utf8 -*-

import os,pickle

from pages.base import WebPage
from pages.elements import WebElement
from pages.elements import ManyWebElements


class PassRecoveryPage(WebPage):

    def __init__(self, web_driver, url=''):
        if not url:
            url = os.getenv("MAIN_URL") or 'https://b2c.passport.rt.ru'

        super().__init__(web_driver, url)

    # Text
    recovery_text = WebElement(xpath='//*[text()="Восстановление пароля"]')
    msg_text = WebElement(xpath='//*[text()="Введите данные и нажмите «Продолжить»"]')
    agreement_text = WebElement(xpath='//*[text()=" Продолжая использовать наш сайт, вы даете согласие на обработку файлов "]')
    agreement_link = WebElement(id="rt-footer-agreement-link")
    forgot = WebElement(xpath='//*[text()="Забыл пароль"]')
    hint = WebElement(xpath='//*[text()="Введите символы с картинки"]')
    sms = WebElement(xpath=f'//*[text()="По SMS на номер телефона"]')
    letter = WebElement(xpath=f'//*[text()="По ссылке на почту"]')


    # Tabs
    tabs = ManyWebElements(class_name='rt-tab.rt-tab--small')
    active_tab = WebElement(class_name="rt-tab.rt-tab--small.rt-tab--active")

    # Buttons
    tab_phone = WebElement(id='t-btn-tab-phone')
    tab_mail = WebElement(id='t-btn-tab-mail')
    tab_login = WebElement(id='t-btn-tab-login')
    tab_ls = WebElement(id='t-btn-tab-ls')
    cont = WebElement(id="reset")
    back = WebElement(id="reset-back")
    cancel = WebElement(name="cancel_reset")

    # Forms
    forms = ManyWebElements(class_name="rt-input__placeholder")
    user = WebElement(id="username")
    capcha_field = WebElement(id="captcha")
    capcha = WebElement(xpath='//*[@id="page-right"]/div[1]/div[1]/div[1]/form[1]/div[2]/div[1]/div[1]/img[1]')


    btn = WebElement(id="kc-login")

    err_msg = WebElement(id="form-error-message")
