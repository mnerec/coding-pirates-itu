# PURPOSE: 

import random

muligheder = ["sten", "saks", "papir"]

def beslut_vinder(menneske_valg, computer_valg):
    if menneske_valg == computer_valg:
        return "ingen"

    hvad_slaar_ordbog = {
        "sten":  "papir",
        "saks":  "sten",
        "papir": "saks"
    }

    menneske_bliver_slaaet_af = hvad_slaar_ordbog[menneske_valg]
    if computer_valg == menneske_bliver_slaaet_af:
        return "Computer"
    else:
        return "Menneske"

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

