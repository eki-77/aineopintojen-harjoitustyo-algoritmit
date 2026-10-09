import wave
import struct
from cmath import exp
from math import pi
from numpy import hanning
import matplotlib.pyplot as plt 
import os
import sys

class KonsoliIo:
    """Luokka, joka hoitaa syötteen luvun käyttäjältä sekä tulostuksen.
    Otettiin käyttöön, jotta voidaan tehdä automaattitestejä eri syötteillä.
    """
    def lue(self, teksti):
        return input(teksti)

    def kirjoita(self, teksti):
        print(teksti)

class Analyser:
    """Luokka, jonka avulla analysoidaan ääninäytteestä voimakkaimmat taajuudet.
    """
    def __init__(self, io_olio):
        self._io_olio = io_olio
        pass

    def lataa(self):
        """ladataan wav-tiedosto, jos kanavia on enemmäin kuin 1 otetaan vain 
        ensimmäinen eli vasen kanava.

        Kysytään tiedoston nimeä käyttäjältä kunnes tiedoston lataaminen onnistuu.
        """
        ohjelman_hakemisto = os.path.dirname(__file__)
        self.samplerate = 0
        while self.samplerate == 0:
            try:
                sample_nimi = self._io_olio.lue("Anna tutkittavan ääninäytteen tiedoston nimi (ohjelma etsii sitä wav-hakemistosta) tai q lopettaaksesi: ")
                if sample_nimi == "q":
                    sys.exit(0)
                sample_polkuineen = os.path.join(ohjelman_hakemisto, "wav/", sample_nimi)
                with wave.open(sample_polkuineen) as wav_sample:
                    metadata = wav_sample.getparams()
                    if metadata.sampwidth != 2:
                        raise TypeError("Ääninäytteen tulee olla 16-bittinen")
                    frames = wav_sample.readframes(metadata.nframes)
                self.samplerate = metadata.framerate
            except TypeError as t_e:
                self._io_olio.kirjoita(t_e)
            except wave.Error as w_e:
                self._io_olio.kirjoita("Wav-tiedosto on jollakin tapaa epäkelpo:")
                self._io_olio.kirjoita(w_e)
            except SystemExit:
                sys.exit(0)
            except:
                self._io_olio.kirjoita("Tiedoston lataaminen ei onnistunut, yritä uudelleen")
        format = "<" + "h" * (len(frames) // 2)
        audio = list(struct.unpack(format, frames))
        left_channel = audio[::metadata.nchannels]
        self.data = left_channel
        
    
    def valmistele(self, data):
        """ ikkunoidaan ääninäyte ja pidennetään kahden potenssiin. Kerrotaan ääninäytteen samplet samanpituisella
        Hann-ikkunalla (tai "hanning"-ikkunalla) ja sen jälkeen lisätään näytteeseen niin paljon nollia perään, 
        että näytteen pituus on seuraava kahden potenssi.

        Args:
            data (list): ääninäyte

        Returns:
            list: ikkunoitu ja pidennetty ääninäyte
        """
        # 
        pituus = len(data)
        ikkunoitu = list(hanning(pituus) * data)
        uusi_pituus = self.kahden_potenssi(pituus)
        self.pituus = uusi_pituus
        result = ikkunoitu + [0.0] * (uusi_pituus - pituus)
        return result

    def kahden_potenssi(self, pituus):
        """palauttaa näytteen pituutta pidemmän seuraavan kahden potenssin

        Args:
            pituus (int): näytteen pituus

        Returns:
            int: pituutta seuraava kahden potenssi, esim. 11 -> 16
        """
        # 
        i = 2
        while pituus > i:
            i *= 2
        return i

    def fft(self, vektori):
        """Toteutaan FFT eli nopea fourier-muunnos (Fast Fourier Transform).
        Ääninäytteen (vektori) pituus on jokin kahden potenssi. Jos vektorin pituus on suurempi kuin 1, 
        jaetaan se kahdeksi vektoriksi erottamalla parilliset ja parittomat indeksit ja kutsutaan rekursiivisesti
        fft-funktiota uudelleen näillä uusilla vektoreilla. Jos vektorin pituus on 1, palautetaan se sellaisenaan.
        Palautetut arvot yhdistetään monimutkaisella kaavalla ja saadaan alkuperäisen vektorin FFT, joka on yhtä pitkä 
        kuin argumenttina tullut vektori.

        Args:
            vektori (list): ääninäyte, jonka pituus on kahden potenssi.

        Returns:
            list: kompleksiluvuista koostuva ääninäytteen fourier-muunnos.
        """
        pituus = len(vektori)
        kerroin = exp(2 * pi * (0 + 1j) / pituus)
        evens = []
        odds = []
        if pituus == 1:
            return vektori
        for i in range(0, pituus//2):
            evens.append(vektori[i*2])
            odds.append(vektori[i*2+1])
        result_evens = self.fft(evens)
        result_odds = self.fft(odds)
        result = []
        for k in range(pituus):
            jj = k % (pituus // 2)
            result.append(result_evens[jj] + (kerroin ** -k) * result_odds[jj])
            #print(result)
        return result
    
    def skaalaa_reaaliluvuksi(self, tulos):
        """ Otetaan FFT:n tuloksesta vain alkupuoli 0 ... N/2-1, sillä tuloksen loppupuoli on alkupuolen peilikuva.
        Sitten otetaan tulosten (eli kompleksilukujen) itseisarvot ja jaetaan ne naytteen pituudella.

        Args:
            tulos (list): fourier-muunnos, kompleksilukuja.

        Returns:
            list: puolta lyhyempi lista reaalilukuja (float)
        """
        pituus = len(tulos)
        alkupuoli = tulos[:int(pituus/2)]
        abs_result = [(abs(x) / pituus) for x in alkupuoli]
        return abs_result

    def anna_taajuuskorit(self, tulokset):
        """lasketaan, mitä taajuutta kukin fourier-muunnoksen indeksi vastaa.

        Args:
            tulokset (list): reaaliarvoinen fourier-muunnos

        Returns:
            list: indeksejä vastaavat taajudet
        """
        korit = [x * (self.samplerate / self.pituus) for x in range(len(tulokset))]
        return korit

    def plottaa_tulokset(self, tulokset, korit, huiput):
        """Tuottaa käppyrän FFT:n tuloksesta. 
        Piirretään käyränä ääninäytteen reaaliarvoinen fourier-muunnos ja 
        korostetaan siitä neliöiden avulla 10 voimakkainta taajuushuippua.

        Args:
            tulokset (_type_): reaaliarvoinen fourier-muunnos
            korit (_type_): fourier-muunnoksen indeksejä vastaavat taajuudet (x-akseli)
            huiput (_type_): 10 voimakkaimman huipun indeksit
        """
        fig, ax = plt.subplots()
        ax.set_xlabel("Taajuus (Hz)")
        ax.set_ylabel("Suhteellinen teho")
        ax.plot(korit, tulokset)
        huiput_x = [korit[x] for x in huiput]
        huiput_y = [tulokset[x] for x in huiput]
        ax.scatter(huiput_x, huiput_y, c='xkcd:deep purple', marker='s')
        plt.show()

    def etsi_maksimit(self, tulokset):
        """etsitään fourier-muunnoksesta kaikki paikalliset huiput, järjestetään ne korkeuden mukaan ja palautetaan 
        10 korkeimman huipun indeksit korkeimmasta matalimpaan. Jos huippuja on vähemmän, palautetaan ne kaikki. 
        Jos huippuja ei ole, palautetaan None.
        Paikallinen huippu tarkoittaa arvoa, joka on sekä sitä edeltävää että seuraavaa arvoa suurempi.

        Args:
            tulokset (list): reaaliarvoinen fourier-muunnos

        Returns:
            list: korkeimpien huippujen indeksit tai None jos huippuja ei ole.
        """
        maksimit = []
        indeksit = range(1,len(tulokset)-1)
        if tulokset[0] > tulokset[1]:
            maksimit.append(0)
        for i in indeksit:
            if tulokset[i-1] < tulokset[i] and tulokset[i] > tulokset[i+1]:
                maksimit.append(i)
        if tulokset[-1] > tulokset[-2]:
            maksimit.append(len(tulokset)-1)
        if len(maksimit) == 0:
            return None
        kovimmat = sorted(maksimit, key = lambda x : tulokset[x], reverse=True)
        if len(kovimmat) < 10:
            return kovimmat
        return kovimmat[:10]

    def analysoi(self):
        """Toteuteuttaa ääninäytteen analysoinnin. Ajaa metodit oikeassa järjestyksessä ja
        lopuksi plottaa tulokset.
        """
        self.lataa()
        valmisteltu = self.valmistele(self.data)
        muunnos = self.fft(valmisteltu)
        tulokset = self.skaalaa_reaaliluvuksi(muunnos)
        korit = self.anna_taajuuskorit(tulokset)
        huiput = self.etsi_maksimit(tulokset)
        self._io_olio.kirjoita("Voimakkaimmat taajuudet ovat (hertseinä): ", [round(korit[x], 1) for x in huiput])
        self.plottaa_tulokset(tulokset, korit, huiput)

if __name__ == "__main__":
    io = KonsoliIo()
    testi = Analyser(io)
    testi.analysoi()
    
 