# Määrittelydokumentti

Tietorakenteet ja algoritmit harjoitustyö tutkintoa tietojenkäsittelytieteen kandidaatti (TKT) varten. Projektissa käytän Python kieltä. Itse koodin kieli ja sen kommenttien kieli tulee olemaan englanniksi.

## Sovelluksen tarkoitus

Sovelluksen on tarkoitus generoida luolasto kartta.

## Sovelluksen toiminta ja algoritmit

Ohjelman tulee ensin generoida huoneet kartalle, tähän käytetään algoritmia joka satunnaisesti asettaa käyttäjän halutun määrän huoneita kartalle siten että ne eivät ole päällekkäin.
Huoneiden asettamisen jälkeen ohjelma trianguloi huoneiden keskipisteet, mistä saadaan huoneiden verkko. Triangulointiin käytetään Bowyer-Watson algoritmia.
Tämä verkko muutetaan minimum spanning tree:ksi.
Lopuksi ohjelma yhdistää huoneet minimum spanning tree:n mukaisesti.

## Ongelman motivaatio

Valitsin ongelman koska halusin tutustua miten pelit generoivat karttoja. Valitsin Bowyer-Watson algoritmin koska se vaikuttaa olevan hyvä tapa laskea miten huoneet voidaan kiinnittää toisiinsa.

## Ohjelman syötteet ja käyttö

Ohjelmaan voi antaa syötteenä minkä kokoisen kartan käyttäjä haluaa ja kuinka monta huonetta kartalle. Ohjelma piirtää käyttäjälle parametreista riippuvan kartan Pygame ikkunaan.

## Aikavaativuus

Ainakin Bowyer-Watson algoritmin aikavaativuus on toivottavasti luokkaa O(n^2) missä on n on huoneiden määrä. Algoritmia on myös myös optimoida siten että aikavaativuus olisi O(n log(n)).

## Lähteet

https://en.wikipedia.org/wiki/Bowyer%E2%80%93Watson_algorithm

https://www.youtube.com/watch?v=V1dwbYlfLIw&ab_channel=SebastianBitsch

https://www.gamedeveloper.com/programming/procedural-dungeon-generation-algorithm