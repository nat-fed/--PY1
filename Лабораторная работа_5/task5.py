from random import sample
import string

def get_random_password() -> str:
    uppercase_char = string.ascii_uppercase
    lowercase_char = string.ascii_lowercase
    digits = string.digits
    all_char = uppercase_char + lowercase_char + digits

    n = 8
    password = sample(all_char, n)

    return "".join(password)
    # TODO написать функцию генерации случайных паролей

print(get_random_password())
