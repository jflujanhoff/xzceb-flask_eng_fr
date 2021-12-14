import unittest

from translator import english_to_french, french_to_english

class TestEnglishToFrench(unittest.TestCase): 
    def test_e2f(self): 
        self.assertNotEqual(english_to_french('Hello'), None) 
        self.assertEqual(english_to_french('Hello'), 'Bonjour')

class TestFrenchToEnglish(unittest.TestCase): 
    def test_f2e(self): 
        self.assertNotEqual(french_to_english('Bonjour'), None) 
        self.assertEqual(french_to_english('Bonjour'), 'Hello') 

unittest.main()