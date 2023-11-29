# PURPOSE: Learn use of input()

arne_valg = input("Indtast Arnes valg (sten/saks/papir): ")
nina_valg = input("Indtast Nina valg (sten/saks/papir): ")

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
