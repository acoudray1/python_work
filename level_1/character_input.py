#
# Create a program that asks the user to enter their name and their age.
# Print out a message addressed to them that tells them the year that they will turn 100 years old.
#

from pip._vendor.distlib.compat import raw_input
end = None
inputError = None

while not end:
    name = raw_input("What is your name ?\n")
    age = int(input("What is your age ?\n"))

    if int(age) > 100:
        print("Your name is " + name + " and you already are older than 100\n")
    else:
        res = 100 - int(age)
        print("Your name is " + name + " and you will be 100 years old in " + str(res) + "\n")

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
