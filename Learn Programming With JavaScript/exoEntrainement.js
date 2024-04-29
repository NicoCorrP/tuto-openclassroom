// const habitants = [10000, 3000, 500000, 600, 0];

// // Step 1 : Calcule la somme des habitants

// let somme = 0;
// for (let i = 0 ; i < habitants.length ; i++) {
//     somme += habitants[i];
// }
// console.log(somme)

// ou alors 
// let somme = 0;
// for (let nbHabitants of habitants) {
//     somme += nbHabitants;
// }
// console.log(somme)

// Step 2 : Créer une fonction prenant en paramètre une array
// de nombre et retournant une somme (en réutilisant
// le code que tu viens de faire)

// const n1 = 5;
// const n2 = 10;
// const n3 = 8;
// const n4 = 12;
// const n5 = 2;
// const n6 = 34;

// const a1 = n1 + n2;
// const a2 = n3 + n4;
// const a3 = n5 + n6;

// console.log(a1);

// function multiplication(param, param2) {
//     const faire = param * param2;
//     return faire;
// }
// const resultat = multiplication(5, 3)
// console.log(resultat)

// function affichage(cinq) {
//     console.log(cinq)
// }
// affichage(5)

// function listeChiffres(values) {
//     console.log(values)
// }
// let valeurs = [1, 2, 3]
// listeChiffres(valeurs)

// function listeChiffres(nombres) {
//     for (let i = 0 ; i < nombres.length ; i++) {
//         console.log(nombres[i])
//     }
//   }
//   let valeurs = [1, 2, 3]
//   listeChiffres(valeurs)
    
function sommeHabs(nbHabitants) {
    let somme = 0;
    for (let i = 0 ; i < nbHabitants.length ; i++) {
        somme += nbHabitants[i];
    }
    return somme
}
let habitants = [10000, 3000, 500000, 600, 0];
const res = sommeHabs(habitants)

console.log(sommeHabs)