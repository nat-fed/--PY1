from random import sample
import string

def get_random_password(n=None) -> str:
    uppercase_char = string.ascii_uppercase
    lowercase_char = string.ascii_lowercase
    digits = string.digits
    all_char = uppercase_char + lowercase_char + digits

    if n is None:
        password = sample(all_char, 8)
    else:
        password = sample(all_char, n)

    return "".join(password)

print(get_random_password())
