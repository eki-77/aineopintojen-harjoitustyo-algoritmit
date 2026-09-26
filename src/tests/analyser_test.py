import unittest
from analyser import Analyser

class TestAnalyser(unittest.TestCase):
    def setUp(self):
        self.testi = Analyser()

    def test_valmistele_pidentaa_naytetta_oikein(self):
        pituus1 = len(self.testi.valmistele([1,2,3,4,5]))
        pituus2 = len(self.testi.valmistele([1,2,3,4]))
        pituus3 = len(self.testi.valmistele(([1]*1000000)))
        self.assertEqual(pituus1, 8)
        self.assertEqual(pituus2, 4)
        self.assertEqual(pituus3, 1048576)

    def test_maksimien_haku(self):
        maksimit = self.testi.etsi_maksimit([6,2,3,4,1,3,2,3,5,7])
        self.assertEqual(maksimit, [0,3,5,9])