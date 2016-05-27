def fizzbuzz(x):
    if x % 15 == 0:
        x = "FizzBuzz"
    elif x % 3 == 0:
        x = "Fizz"
    elif x % 5 == 0:
        x = "Buzz"
    # print(x)
    return x

for i in range(1, 101):
    print(fizzbuzz(i))

def main():
    return fizzbuzz(x)

if __name__ == '__main__':
    main()
