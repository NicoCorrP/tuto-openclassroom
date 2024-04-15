const listeMots = ["Cachalot", "Pétunia", "Serviette"]
const listePhrases = ["Pas de panique !", "La vie, l univers et le reste", "Merci pour le poisson"]

let score = 0

let choix = prompt ("Avec quelle liste voulez-vous jouer: 'mots' ou 'phrases' ?")
while (choix !== "mots" && choix !== "phrases") {
    choix = prompt("Avec quelle liste voulez-vous jouer: 'mots' ou 'phrases' ?")
}

if (choix === "mots") {
for (let i = 0 ; i < listeMots.length ; i++) {
    let motUtilisateur = prompt("Entrez le mot : " + listeMots[i])
    if (motUtilisateur === listeMots[i]) {
        score++
    }
}
console.log("Votre score est de " + score + " sur " + listeMots.length)
} else {
    for (let i = 0 ; i < listePhrases.length ; i++) {
        let phraseUtilisateur = prompt("Entrez la phrase : " + listePhrases[i])
        if (phraseUtilisateur === listePhrases[i]) {
            score++
        }
    }
    console.log("Votre score est de " + score + " sur " + listePhrases.length)
}


// let motUtilisateur = prompt ('Entrez le mot: ' + listeMots[0])

// if (motUtilisateur === listeMots[0]) {
//     score++
// }

// motUtilisateur = prompt('Entrez le mot : ' + listeMots[1])
// if (motUtilisateur === listeMots[1]) {
//     score++
// }

// motUtilisateur = prompt('Entrez le mot : ' + listeMots[2])
// if (motUtilisateur === listeMots[2]) {
//     score++
// }

// for (let i = 0 ; i < 3 ; i++) {
//     let motUtilisateur = prompt ('Veuillez retaper le mot: ' + listeMots[i])
//     if (motUtilisateur === listeMots[i]){
//         score++
//     }
//     console.log(listeMots[i])
// }

// console.log("Votre score est de " + score + " sur 3")
