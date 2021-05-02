class Card:
    def __init__(self, number, suit):
        self.number = number
        self.suit = suit

    def __eq__(self, other):
        return self.number[0] == other.number[0] and \
               self.number[1] == other.number[1] and \
               self.suit == other.suit
