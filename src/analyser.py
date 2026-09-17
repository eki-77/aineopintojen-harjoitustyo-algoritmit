import wave
import struct
from cmath import exp
from math import pi

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
        pass
    
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


testi = Analyser("sample1.wav")
#print(testi.fft([0,1,2,3]))
#print(testi.data)
muunnos = testi.fft(testi.data[:16384])
tulokset = testi.skaalaa_reaaliluvuksi(muunnos)
print(tulokset[:16])
print(max(tulokset))
print(min(tulokset))


        