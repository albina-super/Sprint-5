import random
import string

def generate_email(domain="yandex.ru") -> str:
    first_name = "albina"
    last_name = "toktieva"
    cohort = 20
    random_digits = ''.join(random.choices(string.digits, k=3))
    email = f"{first_name}_{last_name}_{cohort}_{random_digits}@{domain}"
    return email

def generate_password(length: int) -> str:
    characters = string.ascii_letters + string.digits + "!@#$%^&*()"
    password = ''.join(random.choices(characters, k=length))
    return password
