import wave
import struct
from cmath import exp
from math import pi
from numpy import hanning

class Analyser:
    def __init__(self, sample):
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
        print(len(left_channel))
        print(max(left_channel))
        print(min(left_channel))
        self.data = left_channel
        self.samplerate = metadata.framerate
    
    def valmistele(self, data):
        # ikkunoidaan ääninäyte ja pidennetään kahden potenssiin
        pituus = len(data)
        ikkunoitu = list(hanning(pituus) * data)
        uusi_pituus = self.kahden_potenssi(pituus)
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
        pituus = len(tulos)
        abs_result = [(abs(x) / pituus) for x in tulos]
        return abs_result

if __name__ == "__main__":
    testi = Analyser("sample1.wav")
    #print(testi.fft([0,1,2,3]))
    #print(testi.data)
    muunnos = testi.fft(testi.data[:16384])
    tulokset = testi.skaalaa_reaaliluvuksi(muunnos)
    print(tulokset[:16])
    print(max(tulokset))
    print(min(tulokset))
    print(hanning(16))
    #print(type(hanning(16) * tulokset[:16]))
    print(list(hanning(16) * tulokset[:16]))
    print(testi.kahden_potenssi(5))
    testi = list(hanning(16) * tulokset[:16])
    print(testi + [0.0] * 5)

        