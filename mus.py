import random
from card import Card
from deck import Deck
from player import Player

class Game:
    def __init__(self):
        self.deck = Deck()
        self.players = []
        self.scores = {"Team1": 0, "Team2": 0}

    def add_score(self, team, points):
        self.scores[team] += points
        
    def check_winner(self):
        for team, score in self.scores.items():
            if score >= 40:
                return team
        return None
    def create_players(self, player_names, teams):
        for name, team in zip(player_names, teams):
            player = Player(name, team)
            self.players.append(player)
            

    def distribute_cards(self):
        self.deck.shuffle()
        self.deck = self.deck.distribute()
        card_index = 0
        for player in self.players:
            player.hand = self.deck[card_index:card_index + 4]
            card_index += 4
        self.deck = self.deck[16:]
        
    def play_mus(self):
        while len(self.deck) > 8:
            cards_to_exchange = []
            for player in self.players:
                card_indices = player.choose_cards_to_exchange()
                if card_indices is None:
                    print("Mus phase over")
                    return  # If any player doesn't want to exchange cards, end the Mus phase
                cards_to_exchange.append(card_indices)
                print(self.deck)
            for player, card_indices in zip(self.players, cards_to_exchange):
                if card_indices:
                    discarded_cards = player.discard_cards(card_indices)
                    player.hand.extend(self.deck[:(len(discarded_cards))])
                    self.deck = self.deck[(len(discarded_cards)):]
                    
        print("Mus phase over")
        
        
    def show_all_cards(self):
        for player in self.players:
            player.show_hand()
            
    def start_game(self):
        print("Début de la partie !")

        # ... Distribuer les cartes aux joueurs ...
        # Distribute cards
        self.distribute_cards()
        # Show all cards
        self.show_all_cards()
        self.play_mus()

        
        # ... Continuer avec les autres phases du jeu ...

  # Create a new deck

game = Game()

# Create players
player_names = ["Alice", "Bob", "Charlie", "David"]
teams = ["Team1", "Team1", "Team2", "Team2"]
game.create_players(player_names, teams)

# Démarrer la partie
game.start_game()