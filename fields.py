from settings import valid_phone, valid_email

with open('registration.txt', encoding="utf-8") as file:
    data1 = file.read()
    data2 = data1.split('\n')
    data = []
    for i in data2:
        data.append(i.split('\t'))

fnms = ['8', 'Б', '为人民服务为人民服务', 'Тест', 'Nick', 'ААААААААААААААААААААААААААААААА', '!!@$#%!!@$#%']
lnms = ['Nick', '为人民服务为人民服务', 'ААААААААААААААААААААААААААААААА', 'Тестов', 'Б', '!!@$#%!!@$#%', '8']
phone_field = ['!!@$#%!!@$#%', '为人民服务为人民服务', 'ААААААААААААААААААААААААААААААА', '8', 'абвгдеёж', '+79999999999']
email_field = ['!!@$#%!!@$#%', '为人民服务为人民服务', 'ААААААААААААААААААААААААААААААА', '8', 'alb9061@yandex.ru', 'абвгдеёж']
login_field = ['!!@$#%!!@$#%', '为人民服务为人民服务', 'ААААААААААААААААААААААААААААААА', '8', 'абвгдеёж', 'alb9061']
ls_field = ['!!@$#%!!@$#%', '为人民服务为人民服务', 'ААААААААААААААААААААААААААААААА', '8', 'абвгдеёж', '123456789123']
pswd = ['为人民服务为人民服务1Gg', 'abcdefgh1', 'ABCDEFGH1', 'Abcdefgh', '!!@$#%!!@$#%', 'абвгдеёж', '8', 'AAAAAAAAAAAAAAAAAAAAA']

auth_data = [phone_field, email_field, pswd]

# phone_chng = valid_phone.split(' ')
# phone_hidden = phone_chng[0] + ' ••• •••-' + phone_chng[3] + '-' + phone_chng[4]
#
# email_chng = valid_email.split('@')
# email_hidden = email_chng[0][0] + (len(email_chng[0])-1) * '*' + '@' + email_chng[1]
