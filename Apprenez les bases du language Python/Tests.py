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

def celsius_to_fahrenheit(celsius):
    return celsius * 9/5 + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def convertisseur_temperature():
    try:
        temperature = float(input("Entrez la température : "))
    except ValueError:
        print("Erreur : Veuillez entrer une valeur numérique valide pour la température.")
        return

    conversion = input("Choisissez la conversion (C->F, F->C) : ")

    if conversion.upper() == "C->F":
        result = celsius_to_fahrenheit(temperature)
        print(f"{temperature} degrés Celsius équivaut à {result:.2f} degrés Fahrenheit")
    elif conversion.upper() == "F->C":
        result = fahrenheit_to_celsius(temperature)
        print(f"{temperature} degrés Fahrenheit équivaut à {result:.2f} degrés Celsius")
    else:
        print("Erreur : Conversion non valide. Choisissez 'C->F' ou 'F->C'.")

if __name__ == "__main__":
    convertisseur_temperature()