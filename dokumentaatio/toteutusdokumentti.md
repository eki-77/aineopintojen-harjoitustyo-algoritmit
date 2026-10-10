# Spektrianalysaattorin toteutus

Ohjelmassa on yksi luokka, joka toteuttaa ääninäytteen spektrianalyysin (Analyser) sekä apuluokka, joka hoitaa io:n (KonsoliIo). Luokan initialisointi ei tee mitään muuta, kuin ottaa io-olion parametrikseen, mutta "analysoi"-metodi ajaa luokan metodit järkevässä järjestyksessä käyttäen edellisen metodin palauttamaa arvoa seuraavan vaiheen syötteenä. Jotkut arvot kirjoitetaan luokan sisäisiin muuttujiin, esimerkiksi näytteenottotaajuus joka saadaan heti ensimmäisellä metodilla mutta jota tarvitaan vasta ihan lopussa tuloksia ilmoitettaessa.

Ohjelmassa on aika monta importtia, mutta ydinmetodi fft ei käytä muita kuin cmath.exp (kompleksieksponentti) ja math.pi (piin likiarvo). 

Ohjelman käyttöliittymä koostuu siitä, että ohjelma kysyy käsiteltävän tiedoston nimen ja etsii tiedostoa src/wav-hakemistosta. Äänitiedoston pitää olla WAV-formaattia, 1- tai 2- kanavainen (mono tai stereo) ja 16-bittinen resoluutioltaan. Lopuksi ohjelma tulostaa näytteen voimakkaimmat taajuudet tekstinä sekä näyttää ikkunassa FFT:n käyränä, jossa on korostettu 10 voimakkainta taajuutta.

Jos olisin ymmärtänyt aloittaessani työtä poetrystä enemmän, olisin alkanut heti jollakin uudemmalla python3-versiolla kuin 3.10. Numpy ja matplotlib -kirjastojen uudet versiot eivät nimittäin suostu leikkimään 3.10-version kanssa, vaan pitäisi olla uudempi. Sen vuoksi jouduin poetryllä erikseen määrittelemään, että molemmista kirjastoista tarvitaan vanhat (tietyt) versiot. Yritin kyllä päivittää pythonia, mutta se olisikin vaatinut koko linux-version päivityksen uudempaan, ja tässä tuli odottamattomia hankaluuksia.

Wav-kansio sisältää muutamia ääninäytteitä wav-muodossa. Niitä löytyy lisää esim. sivustolta freewavesamples.com . 

## Laajat kielimallit

Työtä tehtäessä en ole käyttänyt laajoja kielimalleja. Jonkin verran tiettyjä detaljeja googlatessa (esim. tietyt poetryn toiminnot) olen silmäillyt låpi googlen AI-yhteenvetoja aiheesta, mutta varsinaisen asian olen opiskellut googlen löytämistä oikeista lähteistä.

## O-analyysi

Oletetaan, että analysoitava ääninäyte on jo valmiiksi jonkin kahden potenssin pituinen, eli sitä ei tarvitse pidentää nollilla. FFT-algoritmi jakaa näytteen kahteen osaan ja ajaa osat rekursiivisesti fft-algoritmin läpi, kunnes analysoitavan näytteen pituus on 1. Sen FFT palauttaa sellaisenaan. Raskas laskenta tapahtuu näitä kahtia jaettuja osamuunnoksia yhdistettäessä. Käsittääkseni kaikki sen ympärillä tapahtuva on melko triviaalia O-laskennan kannalta, joten keskitytään yhdistämiseen. Yhdistäminen vaatii tulosvektorin pituuden verran laskutoimituksia.

Jos näyte on 16 samplen pituinen, ydistäminen alkaa siitä että on 8kpl 1+1 samplepareja yhdistettävänä, eli 16 laskutoimitusta. Tämän jälkeen yhdistetään 4kpl 2+2 samplea, jälleen 16 laskutoimitusta. samoin 2 * (4+4) ja 8+8, eli yhteensä 4 * 16 = 64 laskutoimitusta. 

Jos tuplataan näytteen pituus 32 sampleen, se jaetaan ensin kahtia ja nämä molemmat vaativat edellisen kappaleen mukaisella laskutoimituksella 64 laskutoimitusta, eli yhteensä 128. Tämän lisäksi tulee 1 * (16+16) eli 32 laskutoimitusta, yhteensä 160. 

Tuplataan jälleen 64 sampleen, jolloin saadaan 160*2 + 64 = 384.

Tästä voidaan päätellä, että kun n tuplaantuu, laskutoimitusten määrä hieman yli tuplaantuu. Selvästikin aikavaativuus on suurempi kuin O(n), muttei läheskään niin suuri kuin O(n<sup>2</sup>), joten mitä ilmeisimmin se on O(n log n), mikä sen piti lähteiden mukaan ollakin.
 
## Lähteet

- Huttunen, Heikki: Signaalinkäsittelyn perusteet (Tampereen teknillinen yliopisto 2014). https://urn.fi/URN:ISBN:978-952-15-3222-1
- https://en.wikipedia.org/wiki/Fast_Fourier_transform
- https://en.wikipedia.org/wiki/Discrete_Fourier_transform
- Python-dokumentaatio
- Stack overflow -foorumi
