#
# Create a program that asks the user to enter their name and their age.
# Print out a message addressed to them that tells them the year that they will turn 100 years old.
#

from pip._vendor.distlib.compat import raw_input

while True:
    name = raw_input("What is your name ?\n")
    age = int(input("What is your age ?\n"))

    if int(age) > 100:
        print("Your name is " + name + " and you already are older than 100\n")
    else:
        res = 100 - int(age)
        print("Your name is " + name + " and you will be 100 years old in " + str(res) + "\n")

    x = input('\n\nto continue, press enter\nto quit, write \'q\' and press enter\n')
    if x == 'q':
        break
