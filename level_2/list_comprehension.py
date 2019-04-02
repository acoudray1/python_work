#
# Let’s say I give you a list saved in a variable: a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100].
# Write one line of Python that takes this list a and makes a new list that has only the even elements
# of this list in it.
#

import random

a = []
b = set()

for x in range(random.randint(0, 100)):
    a.append(random.randint(0, 20))

for x in a:
    if x % 2 == 0:
        b.add(x)

print("La liste initiale vaut : " + str(a) + "\n")
print("La liste contient les nombres pairs suivants : " + str(b) + "\n")
