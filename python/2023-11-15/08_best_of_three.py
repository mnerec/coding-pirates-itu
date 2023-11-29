# PURPOSE: Automated game, no user input, don't accept ties, end game after 3 wins

import random

muligheder = ["sten", "saks", "papir"]

arne_valg = ""
nina_valg = ""
vinder = "ingen"

afgjorte_spil_nr = 0

while (vinder == "ingen" or afgjorte_spil_nr < 3):
    arne_index = random.randint(1, 3)
    arne_valg = muligheder[arne_index-1]

    nina_index = random.randint(1, 3)
    nina_valg = muligheder[nina_index-1]

    print("")
    print("Arne vælger " + arne_valg)
    print("Nina vælger " + nina_valg)

    if (arne_valg == "sten"):
        if (nina_valg == "sten"):
            vinder = "ingen"
        elif (nina_valg == "saks"):
            vinder = "Arne"
        elif (nina_valg == "papir"):
            vinder = "Nina"
    elif (arne_valg == "saks"):
        if (nina_valg == "sten"):
            vinder = "Nina"
        elif (nina_valg == "saks"):
            vinder = "ingen"
        elif (nina_valg == "papir"):
            vinder = "Arne"
    elif (arne_valg == "papir"):
        if (nina_valg == "sten"):
            vinder = "Arne"
        elif (nina_valg == "saks"):
            vinder = "Nina"
        elif (nina_valg == "papir"):
            vinder = "ingen"

    if (vinder == "ingen"):
        print("Uafgjort")
    else:
        print(vinder + " vinder")
        afgjorte_spil_nr = afgjorte_spil_nr +1 
