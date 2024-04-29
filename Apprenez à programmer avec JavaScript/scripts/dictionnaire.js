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

function afficherNumeros(nombres) {
    let affiche = 0;
    for (let nombre of nombres) {
        affiche += nombre;
    }
    return affiche;
}
let valeurs = [10, 20, 30, 40, 50];
const affichageFinal = afficherNumeros(valeurs);

console.log(affichageFinal);

// A l'inverse, ici nous allons concaténer chaque 
// numéro avec son index et le séparateur approprié:

// function afficherNumeros(nombres) {
//     for (let i = 0; i < nombres.length; i++) {
//         console.log(i + ": " + nombres[i]);
//     }
// }

// const valeurs = [10, 20, 30, 40, 50];
// afficherNumeros(valeurs);
