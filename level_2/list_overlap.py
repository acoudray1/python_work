#
# Take two lists, say for example these two:
#   a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#   b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# and write a program that returns a list that contains only the elements that are common between the lists
# (without duplicates). Make sure your program works on two lists of different sizes.
#

import random

a = []
b = []
res = set()

for x in range(random.randint(0, 100)):
    a.append(random.randint(0, 20))

for x in range(random.randint(0, 100)):
    b.append(random.randint(0, 20))

print("a : " + str(a) + "\nb : " + str(b) + "\n")

# methode basique
# for x in a:
#    if x in b:
#        res.add(x)
# print("Les éléments que les deux listes ont en communs sont : " + str(res) + "\n")

# methode de génie
print("Les éléments que les deux listes ont en communs sont : " + str(set(a) & set(b)))
