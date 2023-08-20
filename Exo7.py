moyenne = float(input("Entrez votre moyenne : "))

if moyenne < 0 or moyenne > 20:
    print("Note invalide")
if moyenne < 10:
    print("Mention: Faible")
elif moyenne < 15 and moyenne > 10:
    print("Mention: Assez bien")
elif moyenne < 17 and moyenne > 14:
    print("Mention: Bien")
else:
    if moyenne > 17:
        print("Très bien")
