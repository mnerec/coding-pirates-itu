# PURPOSE: Automated game, no user input, don't accept ties, end game after 3 wins, determine winner

import random

muligheder = ["sten", "saks", "papir"]

def beslut_vinder(menneske_valg, computer_valg):
    if (menneske_valg == "sten"):
        if (computer_valg == "sten"):
            return "ingen"
        elif (computer_valg == "saks"):
            return "Menneske"
        elif (computer_valg == "papir"):
            return "Computer"
    elif (menneske_valg == "saks"):
        if (computer_valg == "sten"):
            return "Computer"
        elif (computer_valg == "saks"):
            return "ingen"
        elif (computer_valg == "papir"):
            return "Menneske"
    elif (menneske_valg == "papir"):
        if (computer_valg == "sten"):
            return "Menneske"
        elif (computer_valg == "saks"):
            return "Computer"
        elif (computer_valg == "papir"):
            return "ingen"

menneske_valg = ""
computer_valg = ""
vinder = "ingen"
endelig_vinder = "ingen"

menneske_vundet_antal = 0
computer_vundet_antal = 0

runde = 1

while (vinder == "ingen" or (menneske_vundet_antal + computer_vundet_antal < 3)):
    print("")
    print("***** SPIL NR " + str(runde) + "*****")
    runde = runde + 1

    menneske_valg = ""
    while menneske_valg not in muligheder:
        menneske_valg = input("Indtast sten, saks eller papir: ").lower()

    computer_index = random.randint(1, 3)
    computer_valg = muligheder[computer_index-1]

    print("Computer vælger " + computer_valg)

    vinder = beslut_vinder(menneske_valg, computer_valg)

    print(vinder.title() + " vinder")

    if (vinder == "Menneske"):
        menneske_vundet_antal = menneske_vundet_antal + 1
    elif (vinder == "Computer"):
        computer_vundet_antal = computer_vundet_antal + 1

if (menneske_vundet_antal > computer_vundet_antal):
    endelig_vinder = "Menneske"
else:
    endelig_vinder = "Computer"

print("")
print("Endelig vinder er " + endelig_vinder.upper() + "!!!")

