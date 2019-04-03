#
# Create a program that asks the user for a number and then prints out a list of all the divisors of that number.
# (If you don’t know what a divisor is, it is a number that divides evenly into another number.
# For example, 13 is a divisor of 26 because 26 / 13 has no remainder.)
#

while True:
    inputNumber = int(input("Enter a number :\n"))
    number = inputNumber % 2
    children = 0
    res = []

    while number == 0:
        if children == 0:
            children = inputNumber / 2
        else:
            children = children / 2

        res.append(children)
        number = children % 2

    if len(res) != 0:
        print("The number " + str(inputNumber) + " has " + str(len(res)) + " divisors that are the following : "
              + str(res) + "\n")
    else:
        print("The number " + str(inputNumber) + " has no divisors\n")

    x = input('\n\nto continue, press enter\nto quit, write \'q\' and press enter\n')
    if x == 'q':
        break
