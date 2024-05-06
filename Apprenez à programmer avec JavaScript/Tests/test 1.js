const viande = ["boeuf", "porc", "vollaile"]
const poisson = ["deux kilos svp", "j'aime la viande", "la truffe, l'araignée et la poire"]

let score = 0

let choix = prompt("Quelle protéine voulez-vous : 'viande' ou 'poisson' ?")
while (choix !== "viande" && choix !== "poisson") {
    choix= prompt("Quelle protéine voulez-vous : 'viande' ou 'poisson' ?") 
}

if (choix === "viande") {
for (let i = 0 ; i < viande.length ; i++) {
    let motUtilisateur = prompt("Entrez le mot : " + viande[i])
        if (motUtilisateur === viande[i]){
            score++
}
}
console.log("Votre score est de :" + score + " sur " + viande.length)

} else if (choix === "poisson") {
for (let i = 0 ; i < poisson.length ; i++) {
    let motUtilisateur = prompt("Entrez le mot : " + poisson[i]) 
        if (motUtilisateur === poisson[i]) {
            score++
}
}
console.log("Votre score est de :" + score + " sur " + poisson.length)
}