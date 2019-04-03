#
# Ask the user for a string and print out whether this string is a palindrome or not.
# (A palindrome is a string that reads the same forwards and backwards.)
#

from pip._vendor.distlib.compat import raw_input


def reverse(word):
    x = ''
    for i in range(len(word)):
        x += word[len(word)-i-1]
    return x


while True:
    inputString = raw_input("Enter a String :\n")
    reverseWord = reverse(inputString)

    print(reverseWord)

    if inputString == reverseWord:
        print("This word is a palindrome !")
    else:
        print("This word is not a palindrome !")

    x = input('\n\nto continue, press enter\nto quit, write \'q\' and press enter\n')
    if x == 'q':
        break
