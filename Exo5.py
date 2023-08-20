nom = input("Entrez votre nom : ")
prenom = input("Entrez votre prénom : ")
poids = float(input("Entrez votre poids : "))
taille = float(input("Entrez votre taille : "))
imc = poids / (taille)**2

if imc < 18.4:
    print("Vous êtes maigre")
elif imc >= 18.5 and imc <= 24.9:
    print("Vous êtes de corpulence normale")
elif imc >= 25 and imc <= 29.9:
    print("Vous êtes en surpoids")
elif imc >= 30 and imc <= 34.9:
    print("Vous êtes en obésité modérée")
elif imc >= 35 and imc <= 39.9:
    print("Vous êtes en obésité sévère")
else:
    if imc > 40:
        print("Vous êtes en obésité morbide")
        