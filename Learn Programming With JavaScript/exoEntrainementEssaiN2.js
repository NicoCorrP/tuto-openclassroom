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

function saluer(prenom) {
    let message = "Bonjour " + prenom + " comment vas-tu aujourd'hui ?";
        return message;
} 
let retFonction = saluer("Alice")
console.log(retFonction) 

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