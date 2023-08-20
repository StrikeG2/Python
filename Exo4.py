type_terrain = input("Entrez le type du terrain (carre, rectangle, triangle) : ")

if type_terrain == "carre":
    longueur_du_cote = int(input("Entrez la longueur du côté : "))
    prix_du_metre_carre = int(input("Entrez le prix du mètre carré : "))
    prix_de_vente = (longueur_du_cote * 4) * prix_du_metre_carre
    print("Le prix de vente de ce terrain est de : ",prix_de_vente, "fcfa")
elif type_terrain == "rectangle":
    longueur = int(input("Entrez la longueur : "))
    largeur = int(input("Entrez la largeur : "))
    prix_de_vente = (longueur * largeur) * prix_du_metre_carre
else:
    if type_terrain == "triangle":
        base = int(input("Entrez la base : "))
        hauteur = int(input("Entrez la hauteur : "))
        prix_de_vente = ((base * hauteur)/2) * prix_du_metre_carre
        
