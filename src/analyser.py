import wave
import struct
from cmath import exp
from math import pi
from numpy import hanning
import matplotlib.pyplot as plt 

class Analyser:
    def __init__(self):
        pass

    def lataa(self, sample):
        # ladataan wav-tiedosto, jos kanavia on enemmäin kuin 1 otetaan vain 
        # ensimmäinen eli vasen kanava.
        with wave.open(sample) as wav_sample:
            metadata = wav_sample.getparams()
            if metadata.sampwidth != 2:
                print("Virhe: ääninäytteen tulee olla 16-bittinen.")
                quit()
            #print(metadata)
            frames = wav_sample.readframes(metadata.nframes)
        format = "<" + "h" * (len(frames) // 2)
        audio = list(struct.unpack(format, frames))
        left_channel = audio[::metadata.nchannels]
        print("Näytteen pituus:", len(left_channel))
        self.data = left_channel
        self.samplerate = metadata.framerate
    
    def valmistele(self, data):
        # ikkunoidaan ääninäyte ja pidennetään kahden potenssiin
        pituus = len(data)
        ikkunoitu = list(hanning(pituus) * data)
        uusi_pituus = self.kahden_potenssi(pituus)
        self.pituus = uusi_pituus
        result = ikkunoitu + [0.0] * (uusi_pituus - pituus)
        if len(result) != uusi_pituus:
            print("virhe")
            quit
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
        korit = [round(x * (self.samplerate / self.pituus), 1) for x in range(len(tulokset))]
        return korit

    def plottaa_tulokset(self, tulokset, korit):
        fig, ax = plt.subplots()
        ax.set_xlabel("Taajuus (Hz)")
        ax.set_ylabel("Suhteellinen teho")
        ax.plot(korit, tulokset)
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
        return maksimit

if __name__ == "__main__":
    testi = Analyser()
    testi.lataa("sample1.wav")
    valmisteltu = testi.valmistele(testi.data)
    print("valmistellun pituus", len(valmisteltu))
    #print(testi.fft([0,1,2,3]))
    #print(testi.data)
    #muunnos = testi.fft(testi.data[:16384])
    muunnos = testi.fft(valmisteltu)
    print("muunnoksen pituus", len(muunnos))
    tulokset = testi.skaalaa_reaaliluvuksi(muunnos)
    print("tulosten pituus", len(tulokset))
    print(valmisteltu[:16])
    print(tulokset[:16])
    print(len(tulokset))
    print(type(muunnos[0]))
    print(type(valmisteltu[0]))
    print(type(tulokset[0]))
    #print(tulokset[-16:])
    #print(valmisteltu[-16:])
    print(max(tulokset))
    print(min(tulokset))
    korit = testi.anna_taajuuskorit(tulokset)
    print("koreja:", len(korit))
    print(korit[:10])
    print(korit[-10:])
    testi.plottaa_tulokset(tulokset, korit)
    #plt.plot(tulokset)
    #plt.show()
    #print(hanning(16))
    #print(type(hanning(16) * tulokset[:16]))
    #print(list(hanning(16) * tulokset[:16]))
    #print(testi.kahden_potenssi(5))
    #testi = list(hanning(16) * tulokset[:16])
    #print(testi + [0.0] * 5)

