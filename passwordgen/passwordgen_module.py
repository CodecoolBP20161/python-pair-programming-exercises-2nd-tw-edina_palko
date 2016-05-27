import string
import random


def passwordgen():
    spec = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "?"]
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    number = string.digits
    password_test = ''.join(random.choice(spec) + random.choice(lower) + random.choice(upper) + random.choice(number) for x in range(0, 2))
    return password_test


def main():
    return


if __name__ == '__main__':
    main()

# ''.join(string.ascii_letters + string.digits +for x in range(size, 8))
