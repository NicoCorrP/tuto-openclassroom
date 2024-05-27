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
 * Cette fonction construit et affiche l'email. 
 * @param {string} nom : le nom du joueur
 * @param {string} email : l'email de la personne avec qui il veut partager son score
 * @param {string} score : le score. 
 */
function afficherEmail(nom, email, score) {
    let mailto = `mailto:${email}?subject=Partage du score Azertype&body=Salut, je suis ${nom} et je viens de réaliser le score ${score} sur le site d'Azertype !`
    location.href = mailto
}

function validerNom(nom) {
    if (nom.length < 2) {
        throw new Error("Le nom est trop court")
    }

}

function validerEmail(email) {
    let emailRegExp = new RegExp ("[a-z0-9._-]+@[a-z0-9._-]+\\.[a-z0-9._-]+")
    if (!emailRegExp.test(email)) {
    throw new Error ("L’e-mail n’est pas valide")
    }

}

// Cette fonction affiche le message d'erreur passé en paramètre. 
// Si le span existe déjà, alors il est réutilisé pour ne pas multiplier
// les messages d'erreurs. 

function afficherMessageErreur(message) {
    let spanErreurMessage = document.getElementById("erreurMessage")

    if (!spanErreurMessage) {
        let popup = document.querySelector(".popup")
        spanErreurMessage = document.createElement("span")
        spanErreurMessage.id = "erreurMessage"

        popup.append(spanErreurMessage)
    }

    spanErreurMessage.innerText = message
}

function gererFormulaire(scoreEmail) {
    try {
    let baliseNom = document.getElementById("nom")
    let nom = baliseNom.value
    validerNom.nom

    let baliseEmail = document.getElementById("email")
    let email = baliseEmail.value
    validerEmail(email)
    afficherMessageErreur("")
    afficherEmail(nom, email, scoreEmail)

    } catch(erreur) {
        afficherMessageErreur("erreur.message")
    }
}

/**
 * Cette fonction lance le jeu. 
 * Elle demande à l'utilisateur de choisir entre "mots" et "phrases" et lance la boucle de jeu correspondante
 */
function lancerJeu() {
    // Initialisations
    initAddEventListenerPopup()
    let score = 0
    let i = 0
    let listePropositions = 0

    let btnValiderMot = document.getElementById("btnValiderMot")
    let inputEcriture = document.getElementById("inputEcriture")

    afficherProposition(listeMots[i])

    // Gestion de l'événement click sur le bouton "valider"
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

            // Si c'est le premier élément qui a été modifié, alors nous voulons
            // jouer avec la listeMots. 
            if (event.target.value === "1") {
                listePropositions = listeMots
            } else {
                // Sinon nous voulons jouer avec la liste des phrases
                listePropositions = listePhrases
            }
            // Et on modifie l'affichage en direct. 
            afficherProposition(listePropositions[i])
        })
    }

// gestion de l'évènement submit sur le formulaire de partage
let form = document.querySelector('form');

// on place un ecouteur sur le formulaire au submit 
form.addEventListener("submit", (event) => {
    // pour empecher le comportement par defaut =>
    // le raffraichissement de la page
        event.preventDefault();
        let scoreEmail = `${score} / ${i}`
        gererFormulaire(scoreEmail)
})

    afficherResultat(score, i)
}
