from pages.base import WebPage
from pages.elements import WebElement, ManyWebElements


class RegPage(WebPage):

    def __init__(self, web_driver, url=''):
        url = 'https://b2c.passport.rt.ru'
        super().__init__(web_driver, url)

    reg_page = WebElement(id="kc-register")
    logo = WebElement(class_name="rt-logo what-is-container__logo")
    slogan = WebElement(class_name="what-is__desc")
    auth_policy = WebElement(class_name="auth-policy")
    reg_title = WebElement(class_name="card-container__title")
    link = WebElement(class_name="rt-link.rt-link--orange")
    reg_btn = WebElement(xpath='//button[@type="submit"]')

    first_name = WebElement(name="firstName")
    last_name = WebElement(name="lastName")
    region = WebElement(xpath='//*[@id="page-right"]/div[1]/div[1]/div[1]/form[1]/div[2]/div[1]/div[1]/input[1]')
    region_alt = WebElement(class_name='rt-select__list-wrapper.rt-select__list-wrapper--rounded')
    address = WebElement(id="address")
    password = WebElement(id="password")
    password_conf = WebElement(id="password-confirm")

    wrong_fname = ManyWebElements(xpath='//*[@id="page-right"]/div[1]/div[1]/div[1]/form[1]/div[1]/div[1]/span[1]')
    wrong_lname = WebElement(xpath='//*[@id="page-right"]/div[1]/div[1]/div[1]/form[1]/div[1]/div[2]/span[1]')
    wrong_addr = WebElement(xpath='//*[@id="page-right"]/div[1]/div[1]/div[1]/form[1]/div[3]/span[1]')
    wrong_pass = WebElement(xpath='//*[@id="page-right"]/div[1]/div[1]/div[1]/form[1]/div[4]/div[1]/span[1]')
    wrong_pass_conf = WebElement(xpath='//*[@id="page-right"]/div[1]/div[1]/div[1]/form[1]/div[4]/div[2]/span[1]')

    phone_verif = WebElement(class_name="card-container__title")
    phone_chng_btn = WebElement(xpath='//button[@name="otp_back_phone"]')
    email_verif = WebElement(class_name="card-container__title")

