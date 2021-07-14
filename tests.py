"""
Code to test the translator functions in translator.py.
"""

#Import dependencies
import unittest
from translator import englishtofrench

class TestEnglishToFrench(unittest.TestCase):
    """
    Class to handle all testing of the English to French translator
    """
    def test1(self):
        #Test the basic 'Hello' greeting
        self.assertEqual(englishtofrench('Hello'), 'Bonjour')

    def test2(self):
        #Test a more complex sentence
        self.assertEqual(englishtofrench(\
            'What are you doing today?'), "Que faites-vous aujourd'hui?")

    def test3(self):
        #Test for null input
        self.assertRaises(ValueError, englishtofrench, None)

unittest.main()