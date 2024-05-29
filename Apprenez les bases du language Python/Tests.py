# Écrire un programme Python qui convertit une température donnée en Celsius en Fahrenheit et vice versa.

# Instructions :

# 	1.	Demandez à l’utilisateur d’entrer une température.
# 	2.	Demandez à l’utilisateur de choisir le type de conversion : de Celsius en Fahrenheit (C -> F) ou de Fahrenheit en Celsius (F -> C).
# 	3.	Effectuez la conversion choisie.
# 	4.	Affichez le résultat de la conversion.

# Formules de Conversion :

# 	•	De Celsius en Fahrenheit :  F = C \times \frac{9}{5} + 32 
# 	•	De Fahrenheit en Celsius :  C = (F - 32) \times \frac{5}{9} 

# Exemple de sortie :

# Entrez la température : 100
# Choisissez la conversion (C->F, F->C) : C->F
# 100 degrés Celsius équivaut à 212 degrés Fahrenheit

# def celsius_to_fahrenheit(celsius):
#     return celsius * 9/5 + 32

# def fahrenheit_to_celsius(fahrenheit):
#     return (fahrenheit - 32) * 5/9

# def convertisseur_temperature():
#     try:
#         temperature = float(input("Entrez la température : "))
#     except ValueError:
#         print("Erreur : Veuillez entrer une valeur numérique valide pour la température.")
#         return

#     conversion = input("Choisissez la conversion (C->F, F->C) : ")

#     if conversion.upper() == "C->F":
#         result = celsius_to_fahrenheit(temperature)
#         print(f"{temperature} degrés Celsius équivaut à {result:.2f} degrés Fahrenheit")
#     elif conversion.upper() == "F->C":
#         result = fahrenheit_to_celsius(temperature)
#         print(f"{temperature} degrés Fahrenheit équivaut à {result:.2f} degrés Celsius")
#     else:
#         print("Erreur : Conversion non valide. Choisissez 'C->F' ou 'F->C'.")

# if __name__ == "__main__":
#     convertisseur_temperature()

# Écrire un programme Python qui permet à l’utilisateur de gérer une liste de courses. L’utilisateur doit pouvoir ajouter des articles, supprimer des articles et afficher la liste actuelle.

# Instructions :

# 	1.	Affichez un menu avec les options : “Ajouter un article”, “Supprimer un article”, “Afficher la liste”, “Quitter”.
# 	2.	Demandez à l’utilisateur de choisir une option.
# 	3.	En fonction de l’option choisie, effectuez l’action correspondante.
# 	4.	Répétez jusqu’à ce que l’utilisateur choisisse de quitter.

# 1. Ajouter un article
# 2. Supprimer un article
# 3. Afficher la liste
# 4. Quitter
# Choisissez une option : 1
# Entrez le nom de l'article : Pommes
# L'article "Pommes" a été ajouté à la liste.

def afficher_menu():
    print("1. Ajouter un article")
    print("2. Supprimer un article")
    print("3. Afficher la liste")
    print("4. Quitter")

def ajouter_article(liste):
    article = input("Entrez le nom de l'article : ")
    liste.append(article)
    print(f'L\'article "{article}" a été ajouté à la liste.')

def supprimer_article(liste):
    article = input("Entrez le nom de l'article à supprimer : ")
    if article in liste:
        liste.remove(article)
        print(f'L\'article "{article}" a été supprimé de la liste.')
    else:
        print(f'L\'article "{article}" n\'est pas dans la liste.')

def afficher_liste(liste):
    if liste:
        print("Liste de courses :")
        for idx, article in enumerate(liste, 1):
            print(f"{idx}. {article}")
    else:
        print("La liste de courses est vide.")

def gestionnaire_liste_courses():
    liste_courses = []
    while True:
        afficher_menu()
        choix = input("Choisissez une option : ")
        if choix == '1':
            ajouter_article(liste_courses)
        elif choix == '2':
            supprimer_article(liste_courses)
        elif choix == '3':
            afficher_liste(liste_courses)
        elif choix == '4':
            print("Au revoir !")
            break
        else:
            print("Option non valide, veuillez réessayer.")

if __name__ == "__main__":
    gestionnaire_liste_courses()

