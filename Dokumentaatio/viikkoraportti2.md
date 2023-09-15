- testasin pygame:n toiminnan WSL2 kanssa. Ei vielä ongelmia.

- Huoneiden generointi siten että ne eivät ole päällekkäin toteutettu pygame kirjaston Rect olion avulla. Rect olio voi kertoa jos se on päällekkäin minkään listassa olevan Rect olion kanssa metodilla "collidelistall". Toteutukseni huoneiden generoinnille käyttää tätä metodia varmistamaan että mikään huone ei ole päällekkäin.

- Luotu funktio joka palauttaa kaikkien huoneiden keskipisteen Rect olioiden "center" atribuutin avulla.

- Luotu luokka kolmioille joka laskee myös kolmion ympyrän keskipisteen.
    - Luokalle luotu metodi joka pystyy kertomaan jos jokin piste on kolmion ympyrän sisällä.

- Aloittettu Bowyer-Watson algoritmin työstäminen.

- Algoritmin generoi kolmiot väärin. Palautetut kolmiot menevät päällekkäin. Luultavasti virhe on huonojen kolmioiden poistamisessa ja uusien kolmioiden luomisessa.