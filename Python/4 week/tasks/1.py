#Написать функцию, которая на вход принимает строку, а на выход выдает булево значение (True или False), 
#которое истинно, если полученная строка соответствует российскому номеру телефона или адресу электронной почты.
#Сигнатура функции:
#check_string(string) -> bool
import re

def check_string(string: str) -> bool:
    phone_pattern = re.compile(
        r'^(8|\+7)?[\s-]?\(?\d{3}\)?[\s-]?\d{3}[\s-]?\d{2}[\s-]?\d{2}$'
    )
    email_pattern = re.compile(
        r'^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$'
    )
    return bool(phone_pattern.match(string) or email_pattern.match(string))


