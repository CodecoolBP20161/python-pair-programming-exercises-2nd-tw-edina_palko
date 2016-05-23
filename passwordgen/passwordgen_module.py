# def passwordgen():
#     return
#
#
# def main():
#     return
#
#
# if __name__ == '__main__':
#     main()

import string
import random

def randompassword():
    chars = string.unicode_uppercase + string.unicode_lowercase + string.digits
    size = 4
    return ''.join(random.choice(chars) for x in range(size,12))

print(randompassword())
