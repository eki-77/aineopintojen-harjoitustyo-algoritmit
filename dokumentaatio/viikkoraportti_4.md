Viikko 4

Tällä viikolla koetin saada projektia vertaisarviointikuntoon. Olen aika pahasti jäljessä tämän kanssa. Poetry saatiin asennettua ja käyttöönotettua erinäisten hankaluuksien jälkeen. Huomattiin, että numpy on kirjasto, joka pitää erikseen asentaa, joten se lisättiin poetryyn. Tässä tulikin vähän ongelmia, koska python 3.10 on liian vanha uusimmalle numpylle, joten ratkaisin asian määrittelemällä vaatimuksiin numpy 2.2:n joka tukee vielä python 3.10-versiota. Sama kikka jouduttiin tekemään matplotlib:in kanssa.

Tämän jälkeen aloin tehdä yksikkötestausasiaa. Sain ensimmäisen yksikkötestin tehtyä ja toimimaan, koodin rakennetta piti hieman muuttaa jotta sitä voisi testata tällä tavalla. Ajoin testikattavuusraportit. Tein myös toisen yksikkötestin. Testit tuottavat nyt pitkän listan varoituksia, joita en ihan täysin ymmärrä.

Koodia muokattiin uudelleen niin, että kokosin kaikki spektrianalyysin vaiheet yhteen metodiin, joka kutsuu vaiheita järjestyksessä yksi kerrallaan. Rakensin analyysin tulosten plottauksen kuvaajaan sekä voimakkaimpien taajuuksien laskennan. 

Sitten tein toteutus- ja testausdokumentit.

Käytin tähän tällä viikolla aikaa n. 12 tuntia.

