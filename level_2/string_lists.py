#
# Ask the user for a string and print out whether this string is a palindrome or not.
# (A palindrome is a string that reads the same forwards and backwards.)
#

from pip._vendor.distlib.compat import raw_input
end = None
inputError = None

def reverse(word):
    x = ''
    for i in range(len(word)):
        x += word[len(word)-i-1]
    return x

while not end:
    inputString = raw_input("Enter a String :\n")
    reverseWord = reverse(inputString)

    print(reverseWord)

    if inputString == reverseWord:
        print("This word is a palindrome !")
    else:
        print("This word is not a palindrome !")

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
