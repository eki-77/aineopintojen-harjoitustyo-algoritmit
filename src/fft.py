from cmath import exp
from math import pi

def fft(vektori):
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
    result_evens = fft(evens)
    result_odds = fft(odds)
    result = []
    for k in range(pituus):
        jj = k % pituus//2
        #print(jj)
        result.append(result_evens[jj] + (kerroin ** -k) * result_odds[jj])
        print(result)
    return result



print(fft([0,1,2,3]))
