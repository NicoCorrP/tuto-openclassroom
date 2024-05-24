/*********************************************************************************
 * 
 * Ce fichier contient toutes les fonctions nécessaires au fonctionnement du jeu. 
 * 
 *********************************************************************************/

/**
 * Cette fonction affiche dans la console le score de l'utilisateur
 * @param {number} score : le score de l'utilisateur
 * @param {number} nbMotsProposes : le nombre de mots proposés à l'utilisateur
 */
function afficherResultat(score, nbMotsProposes) {
    let spanScore = document.querySelector(".zoneScore span");

    let affichageScore = `${score} / ${nbMotsProposes}`;

    spanScore.innerText = affichageScore;
    console.log("Votre score est de " + score + " sur " + nbMotsProposes)
}

function afficherProposition(proposition) {
    let zoneProposition = document.querySelector(".zoneProposition")
    zoneProposition.innerText = proposition
}

/**
 * Cette fonction lance le jeu. 
 * Elle demande à l'utilisateur de choisir entre "mots" et "phrases" et lance la boucle de jeu correspondante
 */
function lancerJeu() {
    // Initialisations
    let score = 0
    let i = 0
    let listePropositions = 0

    let btnValiderMot = document.getElementById("btnValiderMot")
    let inputEcriture = document.getElementById("inputEcriture")

    afficherProposition(listeMots[i])

    btnValiderMot.addEventListener("click", () => {
        console.log(inputEcriture.value)
        if (inputEcriture.value === listeMots[i]) {
            score++
        }
        i++
        afficherResultat(score, i)
        inputEcriture.value = ''
        if (listePropositions[i] === undefined) {
            afficherProposition("Le jeu est fini")
            btnValiderMot.disabled = true
        } else {
            afficherProposition(listePropositions[i])
        }
        
    })

    let listeBtnRadio = document.querySelectorAll(".optionSource input")
    for (let i =0; i < listeBtnRadio.length; i++) {
        listeBtnRadio[i].addEventListener("change", (event) => {

            if (event.target.value === "1") {
                listePropositions = listeMots
            } else {
                listePropositions = listePhrases
            }
        
        afficherProposition(listePropositions[i])
    
        })
    }

    afficherResultat(score, i)
}
