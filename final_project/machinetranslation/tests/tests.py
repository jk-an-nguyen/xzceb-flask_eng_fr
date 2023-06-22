"""
Provides the unit test cases for translator
"""
import unittest

from translator import english_to_french, french_to_english

class TestTranslator(unittest.TestCase):
    """Test cases to verify translator tools"""

    def test_english_to_french(self):
        """Input = Hello & Output = Bonjour"""
        self.assertEqual(english_to_french('Hello'), 'Bonjour')
    
    def test_french_to_english(self):
        """Input = Bonjour & Output = Hello"""
        self.assertEqual(french_to_english('Bonjour'), 'Hello')

unittest.main()