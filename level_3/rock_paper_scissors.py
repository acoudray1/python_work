#
# Make a two-player Rock-Paper-Scissors game.
# Remember the rules:
#     Rock beats scissors
#     Scissors beats paper
#     Paper beats rock
#

from pip._vendor.distlib.compat import raw_input
game_dict = {1: "rock", 2: "paper", 3: "scissors"}
playerOne = 0
playerTwo = 0
end = None
inputError = None


def compare(entry_o, entry_t):
    if entry_o == entry_t:
        print("Equality, try again")
    elif entry_o == 1:
        if entry_t == 2:
            print("Player two won !")
        if entry_t == 3:
            print("Player one won !")
    elif entry_o == 2:
        if entry_t == 1:
            print("Player one won !")
        if entry_t == 3:
            print("Player two won !")
    elif entry_o == 3:
        if entry_t == 1:
            print("Player two won !")
        if entry_t == 2:
            print("Player one won !")


while not end:
    playerOne = 0
    playerTwo = 0
    while not (0 < playerOne < 4) or not (0 < playerOne < 4):
        playerOne = int(input("Player one, tap [1] for rock, [2] for paper, [3] for scissors :\n"))
        playerTwo = int(input("Player two, tap [1] for rock, [2] for paper, [3] for scissors :\n"))

    print("Player one choosed : " + str(game_dict[playerOne]))
    print("Player two choosed : " + str(game_dict[playerTwo]))

    compare(playerOne, playerTwo)

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
