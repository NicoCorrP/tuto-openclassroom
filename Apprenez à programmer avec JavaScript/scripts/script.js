function afficherResulat (score, nombreMots) {
    console.log("Votre score est de " + score + " sur " + nombreMots.length)
} 

function choisirPhrasesOuMots() {
    let choix = prompt("Voulez-vous jouer avec des 'mots' ou des 'phrases' ?")
    while (choix !== "mots" && choix !== "phrases") {
        choix = prompt ("Voulez-vous jouer avec des 'mots' ou des 'phrases' ?")
    }
    return choix
}

function lancerBoucleDeJeu (listePropositions) {
    let score = 0
    for (let i = 0 ; i < listePropositions.length ; i++) {
        let motUtilisateur = prompt("Veuillez retaper :" + listePropositions[i])
        if (motUtilisateur === listePropositions[i]) {
            score++
        }
    }
    return score 
}

function lancerJeu() {
    let choix = choisirPhrasesOuMots();
    let score = 0;
    let nombreMots = 0;

    if (choix === "mots") {
        score = lancerBoucleDeJeu(listeMots);
        nombreMots = listeMots.length
    }

    else if (choix === "phrases") {
        score = lancerBoucleDeJeu(listePhrases);
        nombreMots = listePhrases.length
    }
    afficherResulat(score, nombreMots)
}


