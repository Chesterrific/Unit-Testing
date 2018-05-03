import unittest 
from hw1 import *

class Testhw1(unittest.TestCase):

    def test_score_equal(self):
        "General tests for score"
        self.assertEqual(score([(2, 'Clubs'),(8, 'Diamonds')]), 10)
        self.assertEqual(score([(10, 'Hearts'),(3, 'Spades')]), 13)
        
    def test_score_equal_face_cards(self):
        "Tests for face card values to equal 10"
        self.assertEqual(score([(13, 'Clubs'),(11, 'Diamonds')]), 20)

    def test_score_equal_ace_value(self):
        "Tests for correct ace values 11 and 1 depending on current score"
        self.assertEqual(score([(1, 'Clubs'),(1, 'Diamonds')]), 12) 

    def test_deal_perfect(self):
        "Tests case where there are twice as many cards in the deck as there are hands"
        deck = [(2, 'Clubs'),(8, 'Diamonds'),(13, 'Clubs'),(11, 'Diamonds')]
        deal(deck, ([],[]))
        self.assertEqual(deck, []) #Checks to see if deck is empty aka all cards have been dealt

    def test_deal_too_many(self):
        "Test to check if last card in deck is correct"
        deck = [(2, 'Clubs'),(8, 'Diamonds'),(13, 'Clubs'),(11, 'Diamonds'),(9,'Hearts')]
        deal(deck, ([],[]))
        self.assertEqual(deck, [(9,'Hearts')]) #Checks to see if last card left in deck is (9,'Hearts'), which shouldn't be dealt

    def test_deal_exception(self):
        "Tests deal() to see if it raises the correct exception"
        deck = [(2, 'Clubs')]
        with self.assertRaises(TooFewCardsError):
            deal(deck, ([],[]))
        
if __name__ == '__main__':
    unittest.main()
