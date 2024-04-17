function afficherResulat (score, nombreMots) {
    console.log("Votre score est de " + score + " sur " + nombreMots.length)
}

function choisirPhrasesOuMots () {
let choix = prompt("Avec quelle liste désirez-vous jouer : 'mots' ou 'phrases' ?")
    while (choix !== "mots" && choix !== "phrases") {
        choix = prompt("Avec quelle liste désirez-vous jouer : 'mots' ou 'phrases' ?")
    }
    return choix
}

function lancerBoucleDeJeu (listepropositions) {
    for (let i = 0 ; i < listepropositions.length ; i++) {
        let motUtilisateur = prompt("Veuillez retaper :" +listepropositions[i])
        if (motUtilisateur === listepropositions[i]) {
            score++
        }
        return score 
    }
}

function lancerJeu () {
    let choix = choisirPhrasesOuMots ()
    let score = 0
    let nombreMots = 0

    if (choix === "mots") {
        score = lancerBoucleDeJeu(listeMots)
        nombreMots = listeMots.length
   } else { 
    score = lancerBoucleDeJeu(listePhrases)
    nbMotsProposes = listePhrases.length
}

afficherResultat(score, nbMotsProposes)
}