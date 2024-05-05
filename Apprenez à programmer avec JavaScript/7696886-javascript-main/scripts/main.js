/*********************************************************************************
 * 
 * Point d'entrée, c'est lui qui intialise le jeu et lance la boucle de jeu. 
 * 
 *********************************************************************************/

// lancerJeu()

let InputEcriture = document.getElementById("inputEcriture");
let btnValiderMot = document.getElementById("btnValiderMot");

let divZonePropositionDiv = document.querySelector(".zoneProposition");
let spanScore = document.querySelector(".zoneScore span");

let listeBtnRadio = document.querySelectorAll(".optionSource input");
