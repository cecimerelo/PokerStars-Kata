# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
from dealer import Dealer
from deck_of_cards import DeckOfCards

if __name__ == '__main__':
    ladder = {'A': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 11, 'Q': 12,
              'K': 13}
    suits = ['♠️', '♦️', '♣️', '♥️']

    deck_of_cards = DeckOfCards(ladder, suits)

    dealer = Dealer(deck_of_cards)
    dealer.shuffle_cards()

    hands = dealer.distribute_cards(number_of_cards=5, number_of_people=5)
