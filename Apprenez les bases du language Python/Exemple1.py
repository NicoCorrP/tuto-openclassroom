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

fruits = {"pomme":"rouge", "banane":"jaune", "orange":"orange"}
fruits["kiwi"] = "vert"
couleur_banane = fruits["banane"]
fruits["pomme"] = "vert"
del fruits["orange"]
print(fruits.keys())