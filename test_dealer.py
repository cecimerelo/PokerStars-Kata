from unittest import TestCase

from dealer import Dealer
from deck_of_cards import DeckOfCards


class DealerTest(TestCase):
    SAMPLE_LADDER = {'A': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 11, 'Q': 12,
                     'K': 13}
    SAMPLE_SUITS = ['♠️', '♦️', '♣️', '♥️']
    SAMPLE_NUMBER_OF_CARDS = 5
    SAMPLE_NUMBER_OF_PEOPLE = 5

    def setUp(self):
        self.deck_of_cards_class = DeckOfCards(self.SAMPLE_LADDER, self.SAMPLE_SUITS)
        self.deck_of_cards = self.deck_of_cards_class.get_deck()

    def test_shuffle_when_called_then_cards_have_been_shuffled(self):
        self.setUp()
        current_first_card = self.deck_of_cards[0]
        current_last_card = self.deck_of_cards[-1]

        dealer = Dealer(self.deck_of_cards_class)
        dealer.shuffle_cards()

        shuffled_first_card = self.deck_of_cards[0]
        shuffled_last_card = self.deck_of_cards[-1]

        self.assert_deck_has_been_shuffled(current_first_card, current_last_card, shuffled_first_card,
                                           shuffled_last_card)

    # TODO: this test is a bit random 🤔, what should i do ?
    def assert_deck_has_been_shuffled(self, current_first_card, current_last_card, shuffled_first_card,
                                      shuffled_last_card):
        self.assertNotEqual(current_first_card, shuffled_first_card)
        self.assertNotEqual(current_last_card, shuffled_last_card)

    def test_distribute_cards_when_called_then_number_of_hands_expected_are_returned(self):
        self.setUp()
        dealer = Dealer(self.deck_of_cards_class)
        dealer.shuffle_cards()

        hands = dealer.distribute_cards(self.SAMPLE_NUMBER_OF_CARDS, self.SAMPLE_NUMBER_OF_PEOPLE)

        self.assertEqual(len(hands), self.SAMPLE_NUMBER_OF_PEOPLE,
                         'Should\'ve created the same number of cards as people')

    def test_distribute_cards_when_called_then_number_of_cards_expected_are_returned(self):
        self.setUp()
        dealer = Dealer(self.deck_of_cards_class)
        dealer.shuffle_cards()

        hands = dealer.distribute_cards(self.SAMPLE_NUMBER_OF_CARDS, self.SAMPLE_NUMBER_OF_PEOPLE)

        self.assertEqual(len(hands[0]), self.SAMPLE_NUMBER_OF_CARDS,
                         'Should\'ve created the same number of cards as people')