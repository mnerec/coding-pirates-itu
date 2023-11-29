# PURPOSE: Automated game, no user input, don't accept ties, end game after 3 wins, determine winner

import random

muligheder = ["sten", "saks", "papir"]

menneske_valg = ""
computer_valg = ""
vinder = "ingen"
endelig_vinder = ""

afgjorte_spil_nr = 0
menneske_vundet_antal = 0
computer_vundet_antal = 0

while (vinder == "ingen" or afgjorte_spil_nr < 3):

    print("")

    menneske_valg = ""
    while menneske_valg not in muligheder:
        menneske_valg = input("Indtast sten, saks eller papir: ").lower()

    computer_index = random.randint(1, 3)
    computer_valg = muligheder[computer_index-1]

    print("Computer vælger " + computer_valg)

    if (menneske_valg == "sten"):
        if (computer_valg == "sten"):
            vinder = "ingen"
        elif (computer_valg == "saks"):
            vinder = "Menneske"
        elif (computer_valg == "papir"):
            vinder = "Computer"
    elif (menneske_valg == "saks"):
        if (computer_valg == "sten"):
            vinder = "Computer"
        elif (computer_valg == "saks"):
            vinder = "ingen"
        elif (computer_valg == "papir"):
            vinder = "Menneske"
    elif (menneske_valg == "papir"):
        if (computer_valg == "sten"):
            vinder = "Menneske"
        elif (computer_valg == "saks"):
            vinder = "Computer"
        elif (computer_valg == "papir"):
            vinder = "ingen"

    if (vinder == "ingen"):
        print("Uafgjort")
    elif (vinder == "Menneske"):
        menneske_vundet_antal = menneske_vundet_antal + 1
        print(vinder + " vinder")
        afgjorte_spil_nr = afgjorte_spil_nr +1 
    elif (vinder == "Computer"):
        computer_vundet_antal = computer_vundet_antal + 1
        print(vinder + " vinder")
        afgjorte_spil_nr = afgjorte_spil_nr +1 

if (menneske_vundet_antal > computer_vundet_antal):
    endelig_vinder = "Menneske"
else:
    endelig_vinder = "Computer"

print("")
print("Endelig vinder er " + endelig_vinder.upper() + "!!!")
