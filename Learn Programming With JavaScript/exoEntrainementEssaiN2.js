// // Step 1 : Calcule la somme des habitants

//const habitants = [10000, 3000, 500000, 600, 0];
// let somme = 0;
// for (let i = 0 ; i < habitants.length ; i++) {
//     somme += habitants[i];
// }
// console.log(somme)


// // Step 2 : Créer une fonction prenant en paramètre une array
// // de nombre et retournant une somme (en réutilisant
// // le code que tu viens de faire)

// const habitants = [10000, 3000, 500000, 600, 0];
// function addition(nombre) {
//     for (let i = 0 ; i < nombre.length ; i++) {
//         console.log(nombre[i]);
//     }
// }
// addition(habitants)

// Générateur de Salutations Personnalisées
// Description :
// Créez une fonction en JavaScript qui prend en 
// entrée un prénom et retourne une salutation 
// personnalisée pour cette personne. Cette tâche 
// permettra de comprendre comment passer des 
// variables à une fonction et utiliser des 
// chaînes de caractères.

// Instructions détaillées:
// 1. Définir la fonction: Nommez votre fonction 
// saluer'. Elle doit prendre un seul argument : 
// une chaîne de caractères représentant le 
// prénom d'une personne (par exemple, '"Alice"*).

// 2. Générer la salutation: À l'intérieur de la 
// fonction, créez une variable message qui 
// contient le texte de la salutation. Par exemple, 
// si le prénom est '"Alice"*, le message pourrait 
// être "Bonjour Alice, comment vas-tu 
// aujourd'hui?"'

// 3. Retourner la salutation: La 
// fonction doit retourner la variable message qui 
// contient la salutation complète.

// function saluer(prenom) {
//     let message = "Bonjour " + prenom + " comment vas-tu aujourd'hui ?";
//         return message;
// } 
// let retFonction = saluer("Alice")
// console.log(retFonction) 

// Définir la fonction: Nommez votre fonction 
// saluerAvecHeure. Elle doit prendre deux 
// arguments: une chaîne de caractères pour le 
// prénom et un nombre pour l'heure du jour.

// Utiliser les conditions : À l'intérieur de 
// la fonction, utilisez des conditions 
// ("if', 'else if', else*) pour décider de la 
// salutation appropriée selon l'heure. 
// Par exemple:

// De 5h à 12h, utilisez "Bonjour".
// De 12h01 à 18h, utilisez "Bon après-midi".
// De 18h01 à 22h, utilisez "Bonsoir".
// De 22h01 à 4h59, utilisez "Bonne nuit"

// 3. Assembler et retourner la salutation: 
// Créez une variable message qui assemble la 
// salutation appropriée avec le prénom de la 
// personne, par exemple '"Bonsoir Alice, comment 
// vas-tu ce soir ?"'. La fonction doit retourner 
// ce message.

function saluerAvecHeure(heureDuJour, prenom) {
    let Salutation = "";
    if (heureDuJour >= 5 && heureDuJour <= 12) {
        Salutation = "Bonjour "
    }
            
    else if (heureDuJour >= 12.1 && heureDuJour <= 18) {
        Salutation = "Bon après-midi "
    }
        
    else if (heureDuJour >= 18.1 && heureDuJour <= 22) {
        Salutation = "Bonsoir "
    }
        
    else if (heureDuJour >= 22.1 && heureDuJour <= 4.59) {
        Salutation = "Bonne nuit "
    }

    let message = (Salutation + prenom + " comment vas-tu aujourd'hui ?")
    return message

}
let retFonction = saluerAvecHeure(18.9, "Alice");
console.log(retFonction) 