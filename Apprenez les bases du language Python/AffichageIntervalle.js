function AffichageIntervalle(num1, num2) {
    for (let i=num1; i <= num2 ; i++) {
        console.log(i) 
        }
    }
    AffichageIntervalle(5, 20)
// on affiche chaque valeur entre 5 et 20 ligne par ligne

function affichageListe(un, deux) {
    let ligneChiffres = ' '
  for (let i=un;i <= deux;i++){
    ligneChiffres += i + ' ';
  }
    console.log(ligneChiffres.trim())
  }
  affichageListe(10, 15)
//   on affiche chaque valeur entre 5 et 20 sur une même ligne
