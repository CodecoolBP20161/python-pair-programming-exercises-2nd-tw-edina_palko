def palindrome(word):
    return word.lower().replace(" ", "") == word.lower()[::-1].replace(" ", "")


def main():
    return plaindrome(word)


if __name__ == '__main__':
    main()
