import random

class Card:
    def __init__(self, rank):
        self.rank = rank
        

    def __repr__(self):
        return f"{self.rank}"

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
        return [self.cards[i*4:i*4+4] for i in range(num_players)]

class Player:
    def __init__(self, name, team):
        self.name = name
        self.team = team
        self.hand = []
        
    def receive_cards(self, cards):
        self.hand = cards
        
    def show_hand(self):
        print(f"{self.name}'s cards: {self.hand}")
        return self.hand

class Game:
    def __init__(self):
        self.deck = Deck()
        self.players = {}

    def create_players(self, player_names, teams):
        for name, team in zip(player_names, teams):
            self.players[name] = Player(name, team)

    def distribute_cards(self):
        self.deck.shuffle()
        for player in self.players.values():
            player.receive_cards(self.deck.distribute(1))
            
            
    def show_all_cards(self):
        for player in self.players.values():
            player.show_hand()   
  # Create a new deck

game = Game()

# Create players
player_names = ["Alice", "Bob", "Charlie", "David"]
teams = ["Team1", "Team1", "Team2", "Team2"]
game.create_players(player_names, teams)

# Distribute cards
game.distribute_cards()
game.show_all_cards()