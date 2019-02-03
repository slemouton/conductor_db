import unittest
from conductor import Sequence,Bar,Data

class ConductorTest(unittest.TestCase):
    seq_test = Sequence()
    seq_test.load('../datasets/data_txt/ck_id_01_01.txt',
              '../datasets/markers/ck_id_01_01_markers.txt',
              '../datasets/time_signatures/ck_id_01_01.csv')

    def test_load_data(self):
        """verifie la taille de la liste de mesures chargée"""
        self.assertEqual(self.seq_test.bar_list.__len__(),68)
    def test_find_bars(self):
        """verifie qu'on trouve une signature correcte en contexte"""
        self.assertEqual(self.seq_test.bar_list[self.seq_test.trouve('4/4_4/4_4/4')[0][0]].mesure,'4/4')
    def test_create_sequence(self):
        """verifie qu'on cree une sequence par concatenation des mesures trouvees"""
        markers = [85, 2664, 5333, 7991, 10231]
        signatures = ['4/4', '7/4', '6/4', '6/4', '5/4']
        seq_a = self.seq_test.cas1(signatures, markers)
        self.assertIsInstance(seq_a.bar_list[0], Bar)
        self.assertEqual(seq_a.bar_list[1].mesure,'7/4')

