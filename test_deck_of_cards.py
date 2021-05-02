import random
from unittest import TestCase

from card import Card
from deck_of_cards import DeckOfCards


class DeckOfCardsTest(TestCase):
    SAMPLE_LADDER = {'A': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 11, 'Q': 12,
                     'K': 13}
    SAMPLE_SUITS = ['♠️', '♦️', '♣️', '♥️']

    def test_deck_of_cards_when_instantiated_then_deck_is_built(self):
        deck_of_cards = DeckOfCards(self.SAMPLE_LADDER, self.SAMPLE_SUITS).get_deck()
        self.assertIsNotNone(deck_of_cards, "Should\'ve built a deck of cards")

    def test_deck_of_cards_when_built_has_card_elements(self):
        deck_of_cards = DeckOfCards(self.SAMPLE_LADDER, self.SAMPLE_SUITS).get_deck()
        self.assertIsInstance(deck_of_cards[0], Card, "Should\'ve built a deck of cards with cards inside")

    def test_remove_card_when_called_then_card_is_removed(self):
        deck_of_cards_class = DeckOfCards(self.SAMPLE_LADDER, self.SAMPLE_SUITS)
        old_deck = deck_of_cards_class.get_deck()
        random_card = random.choice(old_deck)

        deck_of_cards_class.remove_card(random_card)
        new_deck = deck_of_cards_class.get_deck()

        self.assertNotIn(random_card, new_deck, "Should\'ve deleted the card from the deck")

