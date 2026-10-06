import wave
import struct
from cmath import exp
from math import pi
from numpy import hanning
import matplotlib.pyplot as plt 
import os

class Analyser:
    """Luokka, jonka avulla analysoidaan ääninäytteestä voimakkaimmat taajuudet.
    """
    def __init__(self):
        pass

    def lataa(self):
        """ladataan wav-tiedosto, jos kanavia on enemmäin kuin 1 otetaan vain 
        ensimmäinen eli vasen kanava.

        Args:
            sample: käsiteltävän tiedoston nimi
        """
        ohjelman_hakemisto = os.path.dirname(__file__)
        self.samplerate = 0
        while self.samplerate == 0:
            try:
                sample_nimi = input("Anna tutkittavan ääninäytteen tiedoston nimi (ohjelma etsii sitä wav-hakemistosta)")
                sample_polkuineen = os.path.join(ohjelman_hakemisto, "wav/", sample_nimi)
                with wave.open(sample_polkuineen) as wav_sample:
                    metadata = wav_sample.getparams()
                    if metadata.sampwidth != 2:
                        raise TypeError("Ääninäytteen tulee olla 16-bittinen")
                    frames = wav_sample.readframes(metadata.nframes)
                self.samplerate = metadata.framerate
            except TypeError as te:
                print(te)
            except:
                print("Tiedoston lataaminen ei onnistunut, yritä uudelleen")
        format = "<" + "h" * (len(frames) // 2)
        audio = list(struct.unpack(format, frames))
        left_channel = audio[::metadata.nchannels]
        #print("Näytteen pituus:", len(left_channel))
        self.data = left_channel
        
    
    def valmistele(self, data):
        # ikkunoidaan ääninäyte ja pidennetään kahden potenssiin
        pituus = len(data)
        ikkunoitu = list(hanning(pituus) * data)
        uusi_pituus = self.kahden_potenssi(pituus)
        self.pituus = uusi_pituus
        result = ikkunoitu + [0.0] * (uusi_pituus - pituus)
        return result

    def kahden_potenssi(self, pituus):
        # palauttaa näytteen pituutta pidemmän seuraavan kahden potenssin
        i = 2
        while pituus > i:
            i *= 2
        return i

    def fft(self, vektori):
        # vektorin pitää olla array, jonka pituus on kahden potenssi
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
        # Otetaan FFT:n tuloksesta vain alkupuoli 0 ... N/2-1
        # Sitten otetaan tulosten itseisarvot ja skaalataan naytteen pituudella
        pituus = len(tulos)
        alkupuoli = tulos[:int(pituus/2)]
        abs_result = [(abs(x) / pituus) for x in alkupuoli]
        return abs_result

    def anna_taajuuskorit(self, tulokset):
        korit = [x * (self.samplerate / self.pituus) for x in range(len(tulokset))]
        return korit

    def plottaa_tulokset(self, tulokset, korit, huiput):
        fig, ax = plt.subplots()
        ax.set_xlabel("Taajuus (Hz)")
        ax.set_ylabel("Suhteellinen teho")
        ax.plot(korit, tulokset)
        huiput_x = [korit[x] for x in huiput]
        huiput_y = [tulokset[x] for x in huiput]
        ax.scatter(huiput_x, huiput_y, c='xkcd:deep purple', marker='s')
        plt.show()

    def etsi_maksimit(self, tulokset):
        maksimit = []
        indeksit = range(1,len(tulokset)-1)
        if tulokset[0] > tulokset[1]:
            maksimit.append(0)
        for i in indeksit:
            if tulokset[i-1] < tulokset[i] and tulokset[i] > tulokset[i+1]:
                maksimit.append(i)
        if tulokset[-1] > tulokset[-2]:
            maksimit.append(len(tulokset)-1)
        #palauta 10 korkeimman huipun indeksit (tai niin monta kuin löytyi, jos vähemmän kuin 10. Tai None jos ei ole huippuja.)
        if len(maksimit) == 0:
            return None
        kovimmat = sorted(maksimit, key = lambda x : tulokset[x], reverse=True)
        if len(kovimmat) < 10:
            return kovimmat
        return kovimmat[:10]

    def analysoi(self):
        self.lataa()
        valmisteltu = self.valmistele(self.data)
        muunnos = self.fft(valmisteltu)
        tulokset = self.skaalaa_reaaliluvuksi(muunnos)
        korit = self.anna_taajuuskorit(tulokset)
        huiput = self.etsi_maksimit(tulokset)
        print("Voimakkaimmat taajuudet ovat (hertseinä): ", [round(korit[x], 1) for x in huiput])
        self.plottaa_tulokset(tulokset, korit, huiput)

if __name__ == "__main__":
    testi = Analyser()
    testi.analysoi()
    
 