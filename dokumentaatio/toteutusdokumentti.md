Spektrianalysaattori, toteutus:

Ohjelmassa on yksi luokka, joka toteuttaa ääninäytteen spektrianalyysin. Luokan initialisointi ei tee vielä mitään, mutta "analysoi"-metodi ajaa luokan metodit järkevässä järjestyksessä käyttäen edellisen metodin palauttamaa arvoa seuraavan vaiheen syötteenä. Jotkut arvot kirjoitetaan luokan sisäisiin muuttujiin, esimerkiksi näytteenottotaajuus joka saadaan heti ensimmäisellä metodilla mutta jota tarvitaan vasta ihan lopussa tuloksia ilmoitettaessa.

Ohjelmassa on aika monta importtia, mutta ydinmetodi fft ei käytä muita kuin cmath.exp (kompleksieksponentti) ja math.pi (piin likiarvo). 

Varsinaista käyttöliittymää ei vielä ole. Koodin viimeisille riveille voi laittaa tutkittavan äänitiedoston nimen, sen pitää olla samassa src-hakemistossa kuin koodi. Äänitiedoston pitää olla WAV-formaattia, 1- tai 2- kanavainen (mono tai stereo) ja 16-bittinen resoluutioltaan.

O-analyyseja tai muita suorituskykyarviointeja ei olla vielä tehty.

Tästä puuttuu vielä käyttöliittymä ja monenlaisia virhetarkistuksia. Jos olisin ymmärtänyt aloittaessani työtä poetrystä enemmän, olisin alkanut heti jollakin uudemmalla python3-versiolla kuin 3.10. Numpy ja matplotlib -kirjastojen uudet versiot eivät nimittäin suostu leikkimään 3.10-version kanssa, vaan pitäisi olla uudempi. Sen vuoksi jouduin poetryllä erikseen määrittelemään, että molemmista kirjastoista tarvitaan vanhat (tietyt) versiot.

Pahoittelut vertaisarvioijalle, että tämän mukana tulee vain kaksi testiäänitiedostoa! Niitä löytyy kyllä lisää esim. sivustolta freewavesamples.com . 
 
