import random
from card import Card

class Deck:
    def __init__(self):
        self.cards = []
        self.build()

    def build(self):
        ranks = [1, 2, 3, 4, 5, 6, 7, 10, 11, 12]
        self.cards = [Card(rank) for rank in ranks] * 4

    def shuffle(self):
        random.shuffle(self.cards)

    def distribute(self, num_players=4):
        assert len(self.cards) >= num_players, "Not enough cards to distribute"
        self.shuffle()
        return self.cards
    

