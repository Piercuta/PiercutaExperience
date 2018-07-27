import unittest
from unittest.mock import patch
import random
from ManageDico import *

class Tests(unittest.TestCase):
    """class for testing unittest framework"""
    
    # OpenClassroom example
    def test_choice(self):
        """Test le fonctionnement de la fonction 'random.choice'."""
        liste = list(range(10))
        elt = random.choice(liste)
        # Vérifie que 'elt' est dans 'liste'
        self.assertIn(elt, liste)

    def test_input_checking(self):       
        self.assertEqual(input_checking("y",r"^(y|n)$"), 'y' )

