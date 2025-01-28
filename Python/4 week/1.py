import re

def check_string(string: str) -> bool:
    phone_pattern = re.compile(
        r'^(8|\+7)?[\s-]?\(?\d{3}\)?[\s-]?\d{3}[\s-]?\d{2}[\s-]?\d{2}$'
    )
    email_pattern = re.compile(
        r'^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$'
    )
    return bool(phone_pattern.match(string) or email_pattern.match(string))


