#!/usr/bin/python3
# -*- encoding=utf8 -*-

import os

from pages.base import WebPage
from pages.elements import WebElement
from pages.elements import ManyWebElements


class AuthPage(WebPage):

    def __init__(self, web_driver, url=''):
        if not url:
            url = os.getenv("MAIN_URL") or 'https://b2c.passport.rt.ru'

        super().__init__(web_driver, url)


    # Authorisation page
    right_side = WebElement(class_name="card-container__title")
    left_side = WebElement(id="page-left")

    # Tabs
    tabs = ManyWebElements(class_name='rt-tab.rt-tab--small')
    active_tab = WebElement(class_name="rt-tab.rt-tab--small.rt-tab--active")

    # Forms
    forms = ManyWebElements(class_name="rt-input__placeholder")
    user = WebElement(id="username")
    password = WebElement(id="password")

    # Tab buttons
    tab_phone = WebElement(id='t-btn-tab-phone')
    tab_mail = WebElement(id='t-btn-tab-mail')
    tab_login = WebElement(id='t-btn-tab-login')
    tab_ls = WebElement(id='t-btn-tab-ls')

    btn = WebElement(id="kc-login")
    logout_btn = WebElement(id="logout-btn")
    forgot_passive = WebElement(class_name="rt-link.rt-link--orange.rt-link--muted.login-form__forgot-pwd.login-form__forgot-pwd--muted")
    forgot_active = WebElement(class_name="rt-link.rt-link--orange.login-form__forgot-pwd.login-form__forgot-pwd--muted")

    err_msg = WebElement(id="form-error-message")
    capcha = WebElement(xpath='//*[@id="page-right"]/div[1]/div[1]/div[1]/form[1]/div[3]/div[1]/div[1]/img[1]')
    temp_code = WebElement(xpath='//*[text()="Авторизация по коду"]')
