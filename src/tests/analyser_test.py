import unittest
from analyser import Analyser

class TestAnalyser(unittest.TestCase):
    def setUp(self):
        self.testi = Analyser()

    def test_fft(self):
        vastaus = self.testi.fft([0,1,2,3])
        pyoristetty = [round(x.real, 2) + round(x.imag, 2) * 1j for x in vastaus]
        self.assertEqual(pyoristetty, [6, -2+2j, -2, -2-2j])

    def test_valmistele_pidentaa_naytetta_oikein(self):
        pituus1 = len(self.testi.valmistele([1,2,3,4,5]))
        pituus2 = len(self.testi.valmistele([1,2,3,4]))
        pituus3 = len(self.testi.valmistele(([1]*1000000)))
        self.assertEqual(pituus1, 8)
        self.assertEqual(pituus2, 4)
        self.assertEqual(pituus3, 1048576)

    def test_maksimien_haku(self):
        maksimit = self.testi.etsi_maksimit([6,2,3,4,1,3,2,3,5,7])
        self.assertEqual(maksimit, [9,0,3,5])
        maksimit = self.testi.etsi_maksimit([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
        self.assertEqual(maksimit, None)
        maksimit = self.testi.etsi_maksimit([6,2,3,4,1,3,2,3,5,7,0,1,0,1,0,2,0,2,0,2,0,2,0,2,0,2,0,1,0,1,0])
        self.assertEqual(maksimit, [9,0,3,5,15,17,19,21,23,25])