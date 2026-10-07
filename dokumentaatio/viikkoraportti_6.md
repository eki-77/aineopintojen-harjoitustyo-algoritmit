Tällä viikolla muokkasin ohjelmaa niin, että sen sijaan että käsiteltävän tiedoston nimi olisi kovakoodattu ohjelmaan, se kysytään käyttäjältä tiedostonlatausmetodissa. 

Lisäksi tein paljon vertaisarvioinnissa vinkattuja asioita: lisäsin juttuja gitignoreen ja kirjoitin ohjelmaan docstring-tyyppiset kommentit. Laajensin testejä testaussession vinkkien perusteella. Sain tehtyä ensimmäiset testit, jotka testaavat itse fft-funktiota. Siihen vaadittiin kompleksilukujen pyöristystä, jotta tulokset tulkitaan yhtäsuuriksi.

Minulle on vielä hieman avoinna, pystynkö testaamaan yksikkötesteillä jotenkin koko ohjelman toimivuutta. Minun pitäisi varmaankin muuttaa ohjelman rakennetta jonkin verran, jotta voisin käyttää sitä muuttujien injektointitekniikkaa ja saisin testattua homman tiedoston lukemisesta taajuuksien ilmoittamiseen asti.

Olen toki testannut tätä käsin monta kertaa, siis ajanut ohjelmaa äänisingnaalilla, jonka sisällön tunnen hyvin ja katsonut että tulee oikeita tuloksia. Tässä on sallittava pieni epätarkkuus, esim. 440Hz siniaallosta analyysi voi sanoa että voimakkain taajuus on 440.2 Hz ja toisella tiedostolla 339.9 Hz. 

Tällä viikolla käytin tähän 8h.
