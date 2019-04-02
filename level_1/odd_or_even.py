#
# Ask the user for a number. Depending on whether the number is even or odd,
# print out an appropriate message to the user.
#

from pip._vendor.distlib.compat import raw_input
end = None
inputError = None

while not end:
    number = int(input("Enter a number :\n"))
    resultTwo = number % 2
    resultFour = number % 4

    if resultTwo == 0 and resultFour == 0:
        print("This number is an even number, and a multiple of 4 !\n")
    elif resultTwo == 0 and resultFour != 0:
        print("This number is an even number !\n")
    else:
        print("This is an odd number !\n")

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
