# PURPOSE: Automated game, no user input

import random

arne_valg = ""
nina_valg = ""

muligheder = ["sten", "saks", "papir"]

arne_index = random.randint(1, 3)
arne_valg = muligheder[arne_index-1]

nina_index = random.randint(1, 3)
nina_valg = muligheder[nina_index-1]

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