import random


class Dealer:
    def __init__(self, deck_of_cards):
        self._deck_of_cards_class = deck_of_cards

        self._deck = deck_of_cards.get_deck()

    def shuffle_cards(self):
        random.shuffle(self._deck)

    def distribute_cards(self, number_of_cards, number_of_people):
        hands = []

        for _ in range(number_of_people):
            hand = random.sample(self._deck, number_of_cards)
            self._delete_cards_from_deck(hand)
            hands.append(hand)

        return hands

    def _delete_cards_from_deck(self, hand):
        for card in hand:
            self._deck_of_cards_class.remove_card(card)

    def compare_hands(self, hands):
        pass
