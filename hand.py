from ctypes import Array
from card import Card


class Hand:
    def __init__(self, hand: Array[Card], classification: str) -> None:
        self.hand = hand
        self.classification = classification
