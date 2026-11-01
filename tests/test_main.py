import unittest
from main import proposal,validate_score
class TestProposal(unittest.TestCase):
    def test_score(self):self.assertEqual(proposal('Paseo',70,80,True)['score'],70)
    def test_validation(self):
        for v in [True,'',0,101,'1.5','nan','-1']:
            with self.subTest(v=v),self.assertRaises(ValueError):validate_score(v)
    def test_agreement(self):
        with self.assertRaises(ValueError):proposal('Paseo',70,80)
    def test_name(self):
        with self.assertRaises(ValueError):proposal(' ',70,80,True)
if __name__=='__main__':unittest.main()
