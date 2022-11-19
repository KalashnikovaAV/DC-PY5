import random
import string


def get_random_password() -> str:
    password = ''.join(random.sample(string.ascii_uppercase + string.ascii_lowercase + string.digits, k=8))
    return password


print(get_random_password())
