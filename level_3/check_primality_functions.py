#
# Ask the user for a number and determine whether the number is prime or not.
#


def divisors(in_number):
    inputNumber = in_number % 2
    listOfNumbers = list(range(2, inputNumber+1))
    res = []

    for num in listOfNumbers:
        if inputNumber % num == 0:
            res.append(num)
    return res


while True:
    input_number = int(input("Enter a number, I will tell you if it is a prime number or not.\n"))
    result = divisors(input_number)

    if len(result) == 0:
        print("This number is a prime number !")
    else:
        print("This number isn't a prime number, its divisors are " + str(result) + "\n")

    x = input('\n\nto continue, press enter\nto quit, write \'q\' and press enter\n')
    if x == 'q':
        break
