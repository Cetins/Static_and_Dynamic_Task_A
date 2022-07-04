import unittest
from src.card import Card
from src.card_game import CardGame

class TestCardGame(unittest.TestCase):
    def setUp(self):
        self.card1 = Card('Diamonds', 1)
        self.card2 = Card('Clubs', 2)
        self.cards = [self.card1, self.card2]
        self.card_game = CardGame(self.cards)
        
    def test_check_for_ace_true(self):
        result = self.card_game.check_for_ace(self.card1)
        self.assertEqual(result, True)
    
    def test_check_for_ace_false(self):
        result = self.card_game.check_for_ace(self.card2)
        self.assertEqual(result, False)
        
    def test_highest_card(self):
        high_card = self.card_game.highest_card(self.card1, self.card2)
        self.assertEqual(high_card, self.card2)
        
    def test_cards_total(self):
        self.assertEqual(self.card_game.cards_total(), "You have a total of 3")
    