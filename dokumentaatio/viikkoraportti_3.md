Viikkoraportti 3

Tällä viikolla korjasin ensiksi ydinalgoritmin laskentabugin. Kyse oli yhden lausekkeen väärästä laskujärjestyksestä, joka korjautui sulkeilla. 

Tein ydinalgoritmin ympärille luokan, joka hoitaa ohjelman toimintaa. Ensin mietin, pitäisikö kirjoittaa useampi luokka, mutta sitten totesin että ehkä on kuitenkin yksinkertaisempaa hoitaa ääninäytteen koko analysointi yhden luokan sisällä.

Tästä tosin seuraa ongelma. Olisi fiksua, että metodit ottavat parametreinä dataa ja palauttavat sitä kutsuvalle metodille, mutta mitä tehdä kun koko luokka on samaa ääninäytteen käsittelyä eri vaiheissa? Voisin nimittäin myös kutsua metodeja ilman argumentteja ja metodit voisivat ottaa syötteen esim. muuttujasta self.raakadata ja vastaavasti tallentaa tuloksen self.muunnettudata -kenttään. Mitenkähän tämä kannattaisi hoitaa?

Opiskelin riippuvuuksien injektointia. Testejä en ole päässyt vielä tekemään, kun meteodeissakin on niin paljon hommaa vaikka tiedän, että olisi parasta kirjoittaa niitä samalla tuossa rinnalla. Koetan saada sen johonkin vaiheeseen ennen kuin kaikki metodit ovat kasassa. 

Käytin tällä viikolla tähän aikaa 10 tuntia.

