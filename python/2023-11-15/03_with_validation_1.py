# PURPOSE: Learn to validate input()

arne_valg = ""
nina_valg = ""

while (arne_valg != "sten" and arne_valg != "saks" and arne_valg != "papir"):
    arne_valg = input("Indtast Arnes valg (sten/saks/papir): ")
    arne_valg = arne_valg.lower()

while (nina_valg != "sten" and nina_valg != "saks" and nina_valg != "papir"):
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