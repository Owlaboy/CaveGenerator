- testasin pygame:n toiminnan WSL2 kanssa. Ei vielä ongelmia.

- Huoneiden generointi siten että ne eivät ole päällekkäin toteutettu pygame kirjaston Rect olion avulla. Rect olio voi kertoa jos se on päällekkäin minkään listassa olevan Rect olion kanssa metodilla "collidelistall". Toteutukseni huoneiden generoinnille käyttää tätä metodia varmistamaan että mikään huone ei ole päällekkäin.

- Luotu funktio joka palauttaa kaikkien huoneiden keskipisteen Rect olioiden "center" atribuutin avulla.