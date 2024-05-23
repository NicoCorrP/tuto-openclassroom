# nourriture_preferee = "Glace"
# nouvelle_nourriture_preferee = "Pizza"
# nourriture_preferee = "Pâtes"
# print(nourriture_preferee)

# nom = "Nico"
# age = "24"
# print (f"Bonjour, je m'appelle {nom} et j'ai {age} ans.")
# age += 10
# print (f"Bonjour, je m'appelle {nom} et j'ai {age} ans.")

# nom = "Nicolas"
# age = 24
# taille = 1.73
# est_etudiant = True

# print(f"Nom: {nom}")
# print(f"Age: {age}")
# print(f"Taille: {taille}")
# print(f"Est étudiant: {est_etudiant}")

# print(f"Type nom: {type(nom)}")
# print(f"Type age: {type(age)}")
# print(f"Type taille: {type(taille)}")
# print(f"Type est étudiant: {type(est_etudiant)}")

# fruits = ["pomme", "banane", "orange"]
# fruits.append("Kiwi")
# fruits.remove("Orange")
# fruits[1] = "Ananas"
# print("La liste fruits contient", len(fruits), "éléments.")
# fruits.sort()
# print(fruits)

# fruits = {"pomme":"rouge", "banane":"jaune", "orange":"orange"}
# fruits["kiwi"] = "vert"
# couleur_banane = fruits["banane"]
# fruits["pomme"] = "vert"
# del fruits["orange"]
# print(fruits.keys())

# def main ():
#     nombre_a_gauche = input("Entrez un nombre entier : ")
#     nombre_a_droite = input("Entrez un nombre entier : ")
#     operation = input("Entrez l'opération souhaitée ['+', '-', '*' ou '/'] : ")
    
#     resultat = 0

#     if not nombre_a_gauche.isnumeric() or not nombre_a_droite.isnumeric():
#         print("Erreur: les deux nombres doivent être des nombres entiers")

#     else:
#         nombre_a_gauche = int(nombre_a_gauche)
#         nombre_a_droite = int(nombre_a_droite)

#         match operation:
#             case "+":
#                 resultat = nombre_a_gauche + nombre_a_droite
#             case "-":
#                 resultat = nombre_a_gauche - nombre_a_droite
#             case "*":
#                 resultat = nombre_a_gauche * nombre_a_droite
#             case "/":


#                 if nombre_a_droite == 0:
#                     print("Erreur: impossible de diviser par zéro.")
#                 else:
#                     resultat = nombre_a_gauche / nombre_a_droite
#             case _:
#                 print("Erreur: le symbole d'opération doit être '+', '-', '*' ou '/'.")

#         print (f"Le résultat de l'opération est: {resultat}")

# if __name__ == "__main__":
#     main()

# def main():
#     nombres = input("Saisissez une liste de nombres séparés par des virgules : ")
#     nombres = nombres.split(",")
#     print("Liste des nombres: ", nombres)

#     somme = 0
#     for nombre in nombres:
#         somme += int(nombre)
#     print("Somme des nombres :", somme)

#     moyenne = somme / len(nombres)
#     print("Moyenne des nombres :", moyenne)

#     nombre_sup_moyenne = 0
#     for nombre in liste:
#         if int(nombre) > moyenne:
#             nombre_sup_moyenne += 1
#     print("Nombre de nombres supérieurs à la moyenne :", nombre_sup_moyenne)

#     nombre_pairs = 0
#     i = 0
#     while i < len(liste):
#         if int(liste[i]) % 2 == 0:
#             nombre_pairs += 1
#         i += 1
#     print("Nombre de nombres pairs :", nombre_pairs)


# # Ne touchez pas le code ci-dessous
# if __name__ == "__main__":
#     main()

# def salaire_mensuel(salaire_annuel):
#     return salaire_annuel / 12

# def salaire_hebdomadaire(salaire_mensuel):
#     return salaire_mensuel / 4

# def salaire_horaire(salaire_hebdomadaire, heures_travaillees):
#     return salaire_hebdomadaire / heures_travaillees 

# def main(): 
#     salaire_annuel = float(input("Veuillez saisir ici votre salaire annuel: "))
#     heures_travaillees = float(input("Veuillez saisir ici votre nombres d'heures travaillées par semaine: "))

#     mensuel = salaire_mensuel(salaire_annuel)
#     hebdomadaire = salaire_hebdomadaire(mensuel)
#     horaire = salaire_horaire(hebdomadaire, heures_travaillees) 

#     print("Votre salaire horaire est de", horaire, "euros.") 

# if __name__ == "__main__":
#     main()

# def salaire_mensuel(salaire_annuel):
#     return salaire_annuel / 12

# def salaire_hebdomadaire(salaire_mensuel):
#     return salaire_mensuel / 4

# def salaire_horaire(salaire_hebdomadaire, heures_travaillees):
#     return salaire_hebdomadaire / heures_travaillees

# def main():
#     salaire_annuel = float(input("Entrez ici votre salaire annuel: "))
#     heures_travaillees = float(input("Entrez ici le nombres d'heures total travaillées par semaine: "))

#     mensuel = salaire_mensuel(salaire_annuel)
#     hebdomadaire = salaire_hebdomadaire(mensuel)
#     horaire = salaire_horaire(hebdomadaire, heures_travaillees) 

#     print("Votre salaire horaire est de", horaire, "euros.")

    
def horaires_mensuels(horaires_annuels):
    return horaires_annuels / 12

def horaires_hebdos(horaires_mensuels):
    return horaires_mensuels / 6

def horaires_fixe(horaires_hebdos, horaires_totaux):
    return horaires_hebdos / horaires_totaux

def main():