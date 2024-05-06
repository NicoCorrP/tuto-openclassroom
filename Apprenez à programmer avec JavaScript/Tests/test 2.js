const fruits = ["fraise", "framboise", "myrtille"]
const légumes = ["salade", "tomates", "oignons"]

score = 0

let choix = prompt("Voulez vous manger des 'fruits' ou des 'légumes' ?")
while (choix !== "fruits" && choix !== "légumes") {
    choix = prompt("Voulez vous manger des 'fruits' ou des 'légumes' ?")
}

if (choix === "fruits") {
    for (let i = 0 ; i < fruits.length ; i++){
    let motUtilisateur = prompt("Entrez le mot " + fruits[i]);
    if (motUtilisateur === fruits[i]) {
        score ++
    }
}
console.log("Score de " + score + " sur " + fruits.length)

} else if
    (choix === "légumes"){
    for (let i = 0 ; i < légumes.length ; i++){
    let motUtilisateur = prompt("Entrez le mot " + légumes[i]);
    if (motUtilisateur === légumes[i]) {
        score ++
    }
}
console.log("Score de " + score + " sur " + légumes.length)
}