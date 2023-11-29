# PURPOSE: Learn how to use a random number combined with arrays

import random

arne_valg = ""
nina_valg = ""

muligheder = ["sten", "saks", "papir"]

arne_index = random.randint(1, 3)
arne_valg = muligheder[arne_index-1]

while (nina_valg not in muligheder):
    nina_valg = input("Indtast Nina valg (sten/saks/papir): ").lower()
    nina_valg = nina_valg.lower()

print("Arne vælger " + arne_valg)
print("Nina vælger " + nina_valg)

if (arne_valg == "sten"):
    if (nina_valg == "sten"):
        print("Uafgjort")
    elif (nina_valg == "saks"):
        print("Arne vinder")
    elif (nina_valg == "papir"):
        print("Nina vinder")
elif (arne_valg == "saks"):
    if (nina_valg == "sten"):
        print("Nina vinder")
    elif (nina_valg == "saks"):
        print("Uafgjort")
    elif (nina_valg == "papir"):
        print("Arne vinder")
elif (arne_valg == "papir"):
    if (nina_valg == "sten"):
        print("Arne vinder")
    elif (nina_valg == "saks"):
        print("Nina vinder")
    elif (nina_valg == "papir"):
        print("Uafgjort")