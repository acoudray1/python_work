#
# Create a program that asks the user for a number and then prints out a list of all the divisors of that number.
# (If you don’t know what a divisor is, it is a number that divides evenly into another number.
# For example, 13 is a divisor of 26 because 26 / 13 has no remainder.)
#

from pip._vendor.distlib.compat import raw_input
end = None
inputError = None

while not end:
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

    answer = raw_input("Do you want to do it again ? press [Y] or [N]\n")
    if answer == 'N':
        end = True
    elif answer == 'Y':
        end = False
    else:
        while not inputError:
            answer = raw_input("Wrong statement, press again [Y] or [N]\n")
            if answer == 'Y':
                inputError = True
                end = False
            elif answer == 'N':
                inputError = True
                end = True
            else:
                inputError = False
