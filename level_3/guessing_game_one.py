#
# Generate a random number between 1 and 9 (including 1 and 9). Ask the user to guess the number,
# then tell them whether they guessed too low, too high, or exactly right.
#

import random

num_to_guess = random.randint(1, 9)
guess = None
times = 0

while not (guess == num_to_guess):
    print("***********************************************************************************************************")
    print(num_to_guess)
    times += 1
    guess = int(input("Enter the number that you think is the good number :\n"))

    if guess < num_to_guess:
        print("The value to guess is higher\n")
    elif guess > num_to_guess:
        print("The value to guess is lower\n")
    elif guess == num_to_guess:
        print("Good job ! You found the number to guess in " + str(times) + " times\n")
        break

    x = input('\nto continue, press enter\nto quit, write \'q\' and press enter\n')
    if x == 'q':
        break
