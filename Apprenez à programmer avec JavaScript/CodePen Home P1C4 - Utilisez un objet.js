const ticket = {
    nomFilm: "Batman", 
    prix: 10, 
    numeroSalle: 3
  }
  
  let nom = "David"
  
  // Bonjour nom, votre film NOMDEFILM est en salle NUMERODELASALE
  
  let texteAffichage = "Bonjour " + nom + ", votre film " + ticket.nomFilm + " est en salle " + ticket.numeroSalle
  
  console.log(texteAffichage)