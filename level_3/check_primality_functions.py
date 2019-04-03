#
# Ask the user for a number and determine whether the number is prime or not.
#


def divisors(in_number):
    number = in_number % 2
    children = 0
    res = []

    while number == 0:
        if children == 0:
            children = in_number / 2
        else:
            children = children / 2

        res.append(children)
        number = children % 2

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
