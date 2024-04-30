// Afficher la concaténation des mots arbre, soleil et nuage, 
// en utilisant une ou plusieurs fonctions.

// faire une fonction qui prenne en paramètre trois
// mots et en retourne leur concaténation

// Exemple de démonstration
// function nomDeLaFonction(paramètreVide1, paramètreVide2) {
//  let variable1 = paramètreVide1 + paramètreVide2;
//  return variable1
// }
// let donnéesFinalesVoulues = nomDeLaFonction(premièreDonnéeParamètre1,premièreDonnéeParamètre2);

// console.log(donnéesFinalesVoulues)

// function poesies(mots) {
//     let poesie = "";
//     for (const mot of mots) {
//         poesie += mot + "";
//     }
//     return poesie;
// }

// const mots = ["L'arbre, ", "le soleil ", "et les nuages."];
// const phrase = poesies(mots);
// console.log(phrase);

// function afficherSurLignesDifferentes(mots) {
//     for (const mot of mots) {
//         console.log(mot);
//     }
// }

// const mots = ["L'arbre,", "le soleil", "et les nuages."];
// afficherSurLignesDifferentes(mots);

// Nous allons ici faire l'addition de tous les 
// nombres de l'array:

// function afficherNumeros(nombres) {
//     let affiche = 0;
//     for (let nombre of nombres) {
//         affiche += nombre;
//     }
//     return affiche;
// }
// let valeurs = [10, 20, 30, 40, 50];
// const affichageFinal = afficherNumeros(valeurs);

// console.log(affichageFinal);

// A l'inverse, ici nous allons concaténer chaque 
// numéro avec son index et le séparateur approprié:

// function afficherNumeros(nombres) {
//     for (let i = 0; i < nombres.length; i++) {
//         console.log(i + ": " + nombres[i]);
//     }
// }

// const valeurs = [10, 20, 30, 40, 50];
// afficherNumeros(valeurs);

// Bien sûr ! Voici un exercice de code basé sur 
// la fonction `afficherNumeros` mais avec des 
// données et un énoncé différent :

// **Exercice : Calcul de la somme des prix**

// Énoncé : Vous travaillez sur un système de caisse
//  pour un magasin en ligne. Écrivez une fonction 
//  nommée `calculerTotal` qui prend un tableau de
//  prix en paramètre et retourne la somme totale
//   de ces prix.

// function calculerTotal(tableauDePrix) {
//     let sum = 0;
//     for (let tableaux of tableauDePrix) {
//         sum += tableaux;
//     }
//     return sum;
// }

// let prixProduits = [10.99, 63.50, 26.19, 51.99];
// const totalAchat = calculerTotal(prixProduits);
// console.log("le total de l'achat est de : $" + totalAchat.toFixed(2));

// **Exercice : Calcul de la moyenne des notes**

// Énoncé : Vous développez un système de gestion 
// des notes pour une classe. Écrivez une fonction
//  nommée `calculerMoyenne` qui prend un tableau 
//  de notes en paramètre et retourne la moyenne
//  de ces notes.

function calculerMoyenne(notes) {
    let sum = 0;
    for (let note of notes) {
        sum += note;
    }
    return sum / notes.length;
}
let notesEleves = [10, 13, 12, 18];
let moyenneClasse = calculerMoyenne(notesEleves); 
console.log(moyenneClasse);
