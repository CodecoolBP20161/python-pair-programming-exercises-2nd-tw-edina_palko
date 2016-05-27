import unittest
from years_module import years

# Here's our "unit tests".


class YearsTestCase(unittest.TestCase):
    def test_100years(self):
        self.assertEqual(years(35), 2081)
        self.assertEqual(years(2), 2114)
        self.assertEqual(years(99), 2017)


def main():
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    # If here I use datetime function, the test doen't working...
    now_year = 2016
    result = now_year + (100 - age)
    print("Hi", name, ", you will be 100 years old", "in ", result)
    unittest.main()


if __name__ == '__main__':
    main()
