# Harjoitustyön määrittelydokumentti

Erkki Nurmi
tietojenkäsittelytieteen kandiohjelma (TKT)
Dokumentaatio on toteutettu muutoin suomeksi, mutta koodin sisäiset kommentit ovat englanniksi.

- aihe: Signaalinkäsittely, spektrianalyysi annetusta signaalista ja voimakkaimpien taajuuksien tunnistaminen.
- Harjoitustyössä toteutetaan oma FFT-algoritmi.
- Ohjelma ottaa syötteenä näytteen äänitiedostona WAV-formaatissa ja tuottaa sen perusteella:
  1. spektrianalyysin eli kuvaajan, jonka x-akseli on taajuus ja y-akseli voimakkuus sekä
  2. Luettelon näytteen voimakkaimmista taajuuksista (em. kuvaajan huippujen taajuudet)
- FFT-algoritmin pitäisi olla aikavaativuudeltaan O(n log n). 
  - Wikipedian mukaan FFT-algoritmeilla pitäisi päästä tähän. Luulisin, että toteutan Cooley-Tukeyn FFT-algoritmin. 
  - Mahdollisesti sitä ennen muokataan näytteen pituutta jatkamalla siitä nollilla (zero-padding), kunnes näytteen pituus on FFT:lle optimaalinen, esim. seuraava kahden potenssi.
  - Määritelmästä johdettu DFT eli diskreetti fourier-muunnos ilman sitä "fast"-etuliitettä olisi aikavaativuudeltaan O(n<sup>2</sup>).
  - FFT pilkkoo näytteen pieniksi paloiksi, tekee jokaiselle erillisen DFT:n ja yhdistää tulokset. Tämä keventää laskentakuormaa huomattavasti.
- Ohjelman toteutan pythonilla.
- Python on luultavasti ainoa ohjelmointikieli, jolla pystyn vertaisarvioinnin toteuttamaan. Olen tehnyt 20 vuotta sitten FFT-asioita Matlabilla, mutta siitä on 20 vuotta. 35 vuotta sitten osasin GW-BASICcia oikein hyvin.
- Aion käyttää lähteinä wikipedian ja sen lähteiden tietoja FFT-algoritmeista. Jos se ei riitä, etsin sivuja joilla olisi mielellään jonkinlaisella pseudokoodilla selostettu algoritmin toiminta.

Harjoitustyön ydin on toteuttaa itsekirjoitettu FFT-algoritmi voimakkaiden taajuuksien tunnistamiseen ääninäytteestä.

## Monimutkaistusideoita

Mikäli tämä ei riitä harjoitustyön vaatimusten täyttämiseen:

- Tätä voisi kehittää toteuttamalla spektrianalyysin sijasta spektrogrammi.
- Tällöin ääninäytteestä otettaisiin limittyviä ikkunoita, jotka tutkittaisiin FFT:llä.
- Kuvaaja olisi spektrogrammi, jossa x-akseli on aika, y on taajuus ja lämpöväreillä esitetään kunkin taajuuskaistan voimakkuus sillä ajan hetkellä.
- Lukuina voisi esittää kullakin hetkellä voimakkaimman taajuuden ja ehkä tehdä niistä erillisen plotin.




