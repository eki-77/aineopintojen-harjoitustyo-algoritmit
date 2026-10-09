Tällä viikolla muokkasin ohjelmaa niin, että sen sijaan että käsiteltävän tiedoston nimi olisi kovakoodattu ohjelmaan, se kysytään käyttäjältä tiedostonlatausmetodissa. 

Lisäksi tein paljon vertaisarvioinnissa vinkattuja asioita: lisäsin juttuja gitignoreen ja kirjoitin ohjelmaan docstring-tyyppiset kommentit. Laajensin testejä testaussession vinkkien perusteella. Sain tehtyä ensimmäiset testit, jotka testaavat itse fft-funktiota. Siihen vaadittiin kompleksilukujen pyöristystä, jotta tulokset tulkitaan yhtäsuuriksi.

Seuraavaksi opiskelin riippuvuuksien injektointia, ja tein io-toiminnoista oman luokan kurssimateriaalin ohjeen mukaan. Nyt pystyin yksikkötesteissä syöttämään ladattavien tiedostojen nimiä. Kirjoitin vielä tiedoston lataamismetodiin mahdollisuuden lopettaa suoritus kirjoittamalla "q". Muutoin latauksen virheiden virheilmoituksia testatessa ohjelma ei olisi päättynyt, koska se kysyy uudelleen jos lataus ei onnistu. Nyt pitikin sitten opetella yksikkötestaaminen tilanteessa, jossa testattava ohjelma tuottaa poikkeuksen.

Kirjoitin paljon testejä loppujen metodien testaamiseen. Sain lopulte tehtyä myös yksikkötestin, joka testaa koko ohjelman läpikäymistä tietyllä tiedostolla. Käytin mock-modulin patch-toimintoa estääkseni plot-ikkunan näyttämisen testeissä, jottei suoritus keskeydy. Nyt testikattavuus on 96% ja projekti kaipaa enää dokumentoinnin täydentämisen, pientä viilausta ja käyttöohjeet.

Tällä viikolla käytin tähän 12h.
