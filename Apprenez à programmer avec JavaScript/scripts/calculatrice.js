// Afficher le résultat d'une adddition 50 + 28, 
// en utilisant une ou plusieurs fonctions.

// faire une fonction qui prenne en paramètre deux
// nombres et en retourne leur somme

// Exemple de démonstration
// function nomDeLaFonction(paramètreVide1, paramètreVide2) {
//  let variable = paramètreVide1 + paramètreVide2;
//  return variable
// }
// let donnéesParamètresVariable = nomDeLaFonction(1,2);

// console.log(donnéesParamètresVariable)

function somme(nombres, nombredeux) {
    let result = nombres + nombredeux;
    return result
}
let résultat = somme(50,28);

console.log(résultat)

function phrase(Un, Deux) {
    let ensemble = Un + Deux;
    return ensemble 
}
let phraseEntière = phrase("Le ciel ","est bleu");

console.log(phraseEntière)