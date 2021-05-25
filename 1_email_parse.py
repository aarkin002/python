import re


def email_parse(usr_email):
    msg = f'wrong email: {usr_email}'
    username, domain = re.split('@', usr_email)
    re_email = re.compile(r'^[\w.-]+@[\w.-]+\.\w+$')
    if re_email.match(usr_email) is not None:
        email_dict = {'username': username, 'domain': domain}
        return email_dict
    else:
        raise ValueError(msg)


print(email_parse('someone@geekbrains.ru'))
