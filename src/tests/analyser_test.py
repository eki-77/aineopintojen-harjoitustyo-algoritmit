import unittest
from analyser import Analyser, KonsoliIo

class StubIo:
    def __init__(self, inputs):
        self.inputs = inputs
        self.outputs = []

    def lue(self, teksti):
        return self.inputs.pop(0)

    def kirjoita(self, teksti):
        self.outputs.append(teksti)

class TestAnalyser(unittest.TestCase):
    def setUp(self):
        io = KonsoliIo()
        self.testi = Analyser(io)

    def test_lataa(self):
        io = StubIo(["200Hz_-17dBFS_440Hz_-17dBFS_1s.wav"])
        self.testi = Analyser(io)
        self.testi.lataa()
        self.assertEqual(len(self.testi.data), 44101)
        self.assertEqual(self.testi.samplerate, 44100)

    def test_lataa_yleinen_latausvirhe(self):
        io = StubIo(["virhenimi", "q"])
        self.testi = Analyser(io)
        with self.assertRaises(SystemExit):
            self.testi.lataa()
        self.assertEqual(io.outputs[0], "Tiedoston lataaminen ei onnistunut, yritä uudelleen")

    def test_lataa_rikkinainen_wav(self):
        io = StubIo(["epakelpo_wav.wav", "q"])
        self.testi = Analyser(io)
        with self.assertRaises(SystemExit):
            self.testi.lataa()
        self.assertEqual(io.outputs[0], "Wav-tiedosto on jollakin tapaa epäkelpo:")

    def test_lataa_aaninayte_ei_ole_16_bittinen(self):
        io = StubIo(["Sine1KHz_24bit_eli_ei_toimi.wav", "q"])
        self.testi = Analyser(io)
        with self.assertRaises(SystemExit):
            self.testi.lataa()
        self.assertEqual(str(io.outputs[0]), "Ääninäytteen tulee olla 16-bittinen")

    def test_valmistele_pidentaa_naytetta_oikein(self):
        pituus1 = len(self.testi.valmistele([1,2,3,4,5]))
        pituus2 = len(self.testi.valmistele([1,2,3,4]))
        pituus3 = len(self.testi.valmistele(([1]*1000000)))
        self.assertEqual(pituus1, 8)
        self.assertEqual(pituus2, 4)
        self.assertEqual(pituus3, 1048576)

    def test_fft(self):
        vastaus = self.testi.fft([0,1,2,3])
        pyoristetty = [round(x.real, 2) + round(x.imag, 2) * 1j for x in vastaus]
        self.assertEqual(pyoristetty, [6, -2+2j, -2, -2-2j])

    def test_skaalaa_reaaliluvuksi(self):
        vektori = [6, -3+4j, -2, -3-4j, 6, -2+2j, -2, -2-2j]
        self.assertEqual(self.testi.skaalaa_reaaliluvuksi(vektori), [0.75, 0.625, 0.25, 0.625])




    def test_maksimien_haku(self):
        maksimit = self.testi.etsi_maksimit([6,2,3,4,1,3,2,3,5,7])
        self.assertEqual(maksimit, [9,0,3,5])
        maksimit = self.testi.etsi_maksimit([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
        self.assertEqual(maksimit, None)
        maksimit = self.testi.etsi_maksimit([6,2,3,4,1,3,2,3,5,7,0,1,0,1,0,2,0,2,0,2,0,2,0,2,0,2,0,1,0,1,0])
        self.assertEqual(maksimit, [9,0,3,5,15,17,19,21,23,25])