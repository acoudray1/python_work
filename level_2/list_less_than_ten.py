#
# Take a list, say for example this one: a = [1, 1, 2, 3, 5, 8, 10, 13, 21, 34, 55, 89]
# and write a program that prints out all the elements of the list that are less than the number given by the user.
#

from pip._vendor.distlib.compat import raw_input
a = [1, 1, 2, 3, 5, 8, 10, 13, 21, 34, 55, 89]
b = []
end = None
inputError = None

while not end:
    b.clear()
    inputValue = int(input("Enter a number :\n"))
    for i in a:
        if i < inputValue:
            b.append(i)

    print("The numbers that are lower than " + str(inputValue) + " are the following : " + str(b) + "\n")

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
