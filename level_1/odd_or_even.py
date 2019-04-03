#
# Ask the user for a number. Depending on whether the number is even or odd,
# print out an appropriate message to the user.
#

while True:
    number = int(input("Enter a number :\n"))
    resultTwo = number % 2
    resultFour = number % 4

    if resultTwo == 0 and resultFour == 0:
        print("This number is an even number, and a multiple of 4 !\n")
    elif resultTwo == 0 and resultFour != 0:
        print("This number is an even number !\n")
    else:
        print("This is an odd number !\n")

    x = input('\n\nto continue, press enter\nto quit, write \'q\' and press enter\n')
    if x == 'q':
        break
