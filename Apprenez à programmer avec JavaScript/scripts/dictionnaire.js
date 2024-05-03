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

// Voici un exercice de code basé sur
// la fonction "afficherNumeros" mais avec des
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

// function calculerMoyenne(notes) {
//     let sum = 0;
//     for (let note of notes) {
//         sum += note;
//     }
//     return sum / notes.length;
// }
// let notesEleves = [10, 13, 12, 18];
// let moyenneClasse = calculerMoyenne(notesEleves);
// console.log(moyenneClasse);

// 2eme essai:
// function calculerMoyenne(notes) {
//     let sum = 0;
//     for (let note of notes) {
//       sum += note / notes.length;
//     }
//     return sum;
//   }
//   let moyenne = [10, 13, 12, 16, 20];
//   let moyenneDesNotes = calculerMoyenne(moyenne);
//   console.log(moyenneDesNotes);


// Ici, nous avons une fonction qui nous premets
// de trouver le plus grand nombre dans un tableau

// function trouverMaximum(tableau) {
//     let maximum = tableau[0];
//     for (let i = 0 ; i < tableau.length ; i++)
//     {
//         if (tableau[i] > maximum) {
//             maximum = tableau[i];
//         }
//     }
//     return maximum;
// }

// let performances = [10.5, 12.7, 24.2, 56.8];
// let performanceMaximale = trouverMaximum(performances);
// console.log(performanceMaximale);


// Ici, nous allons verifier dans un stock si
// l'article recherche y est present:

// function verifierPresence(stock, articleRecherche) {
//     for (let article of stock) {
//         if (article === articleRecherche) {
//             return true;
//         }
//     }
//     return false;
// }
// let stockArticles = ["chaussures", "chaussettes", "chemises", "pantalons"];
// let articleRecherche = "chaussettes";
// const estPresent = verifierPresence(stockArticles, articleRecherche);
// console.log("L'article " + articleRecherche + " est present dans le stock :" + estPresent);

// function trouverBallon(salleDeSport, ballonRecherche) {
//     for (let differentesSalles of salleDeSport) {
//       if (differentesSalles === salleDeSport) {
//         return true;
//       }
//     }
//     return false;
//   }
//   let ballons = ["rugby", "football", "waterpolo", "handball"];
//   let ballonRecherche = "waterpolo";
//   let ballonTrouve = trouverBallon(ballons, ballonRecherche);
//   console.log("Le ballon de " + ballonRecherche + " as-t'-il ete trouve dans la pile de ballons ?: " + ballonTrouve);

// Ecrire une fonction qui prends en parametre une
// liste de string et les affiches ligne par
// ligne

// function affichageMots(listeString) {
//     let motsProposes = "";
//     for (let i = 0 ; i < listeString.length ; i++) {
//         motsProposes += listeString[i];
//         console.log(listeString[i]);
//     }
// }
// let TableauDeMots = ["arbre", "soleil", "vache", "champs", "campagne"];
// affichageMots(TableauDeMots);

// Maitenant il faut concatener la liste de mots
// pour en faire une phrase

// function affichageMots(listeString) {
//     let motsProposes = "";
//     for (let i = 0 ; i < listeString.length ; i++) {
//         motsProposes += listeString[i];
//     }
//   return motsProposes

// ici, return permets de stocker l'ensemble des
// mots de la liste et de les retourner concaténés,
// cependant, comme on peux le voir, ils sont tous
// liés sans aucun espace

// }
// let TableauDeMots = ["arbre", "soleil", "vache", "champs", "campagne"];
// let resultat = affichageMots(TableauDeMots);
// console.log(resultat);


// Ici, on affiche donc la liste de mots en mettant un
// espace avant chaque mots sauf pour le premier

// function affichageMots(listeString) {
//     let motsProposes = "";
//     for (let i = 0 ; i < listeString.length ; i++) {
//       if (i === 0) {
//         motsProposes += listeString[i];
//       }

// c'est ici que le premier mot qui commence a 0
// (car la liste commence toujours a 0), ne va
// pas avoir d'espace qui le precede mais les
// suivants en auront bien un

//       else {
//       motsProposes += " "+ listeString[i];
//       }
//     }
//   return motsProposes
// }
// let TableauDeMots = ["arbre", "soleil", "vache", "champs", "campagne"];
// let resultat = affichageMots(TableauDeMots);
// console.log(resultat);


// Ici, on affiche à l'inverse la liste de mots 
// en mettant un espace après chaque mots sauf 
// pour le dernier

// function affichageMots(listeString) {
//     let motsProposes = "";
//     for (let i = 0 ; i < listeString.length ; i++) {
//       if (i === (listeString.length-1)) {

// ici, on prends la valeur totale de listeString
// a laquelle on enleve 1 car la liste commence
//  toujours a 0, comme ça on ajoute l'espace après
// chaque  mots sauf pour le dernier de la liste

//         motsProposes += listeString[i];
//       }
//       else {
//       motsProposes += listeString[i] + " ";
//       }
//     }
//   return motsProposes
// }
// let TableauDeMots = ["arbre", "soleil", "vache", "champs", "campagne", "fleur"];
// let resultat = affichageMots(TableauDeMots);
// console.log(resultat);

// Ecrire une autre fonction qui prends en 
// parametre une liste de string et les affichent 
// ligne par ligne


// function affichageMots(listeString) {
//     let listes = "";
//     for (let listes of listeString) {
//       console.log(listes); 
//     }
//   }
//   let tableauMots = ["jonquille", "tullipe", "rose", "magnolia"];
//   affichageMots(tableauMots);
  