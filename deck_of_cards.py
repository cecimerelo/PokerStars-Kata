from card import Card


class DeckOfCards:
    def __init__(self, ladder, suits):
        self.ladder = ladder
        self.suits = suits

        self._deck = []
        self._build_deck()

    def _build_deck(self):
        for number in self.ladder.items():
            for suit in self.suits:
                card = Card(number, suit)
                self._deck.append(card)

    def remove_card(self, card):
        self._deck.remove(card)

    def shuffle(self):
        pass

    def get_deck(self):
        return self._deck
