import unittest
from app.uniqueElementsTemplate import *
from app.uniqueItensAlgorithm import *


class TestUniqueElements(unittest.TestCase):

    def test_uniqueNaive(self):
        self.uniqueElements(UniqueNaive)

    def test_uniqueSort(self):
        self.uniqueElements(UniqueSort)

    def test_uniqueHash(self):
        self.uniqueElements(UniqueHash)

    def uniqueElements(self, algorithmClass:UniqueElementsTemplate):
        uniqueElements = [51, 81, 6, 93, 79, 38, 41, 52, 43, 10, 4, 89, 66, 46, 60, 48, 30, 95, 45, 71]
        notUniqueElements = ["Maçã", "Banana", "Laranja", "Uva", "Manga",
                                  "Abacaxi", "Melancia", "Morango", "Pera", "Cereja",
                                  "Kiwi", "Pêssego", "Limão", "Amora", "Framboesa", "Laranja"
                                                                                    "Tangerina", "Acerola", "Goiaba",
                                  "Caju", "Pitaya", "Amora"]
        self.assertFalse(algorithmClass.hasUniqueElements(notUniqueElements))
        self.assertTrue(algorithmClass.hasUniqueElements(uniqueElements))
