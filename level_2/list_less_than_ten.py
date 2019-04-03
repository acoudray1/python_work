#
# Take a list, say for example this one: a = [1, 1, 2, 3, 5, 8, 10, 13, 21, 34, 55, 89]
# and write a program that prints out all the elements of the list that are less than the number given by the user.
#

a = [1, 1, 2, 3, 5, 8, 10, 13, 21, 34, 55, 89]
b = []

while True:
    b.clear()
    inputValue = int(input("Enter a number :\n"))
    for i in a:
        if i < inputValue:
            b.append(i)

    print("The numbers that are lower than " + str(inputValue) + " are the following : " + str(b) + "\n")

    x = input('\n\nto continue, press enter\nto quit, write \'q\' and press enter\n')
    if x == 'q':
        break
