class Player:
    def __init__(self, name, team):
        self.name = name
        self.team = team
        self.hand = []
        

        
    def show_hand(self):
        print(f"{self.name}'s cards: {self.hand}")
        return self.hand
    def choose_cards_to_exchange(self):
        while True:
            print(f"{self.name}, your hand is: {self.hand}")
            card_indices = input("Enter the indices of the cards you want to exchange, separated by spaces (or enter to keep all cards): ")
            if card_indices.strip() == '':
                # The player chose to keep all cards
                return []
            elif card_indices.strip().lower() == 'no':
            # The player chose to start the game
                return None
            card_indices = [int(index) for index in card_indices.split()]
            if all(0 <= index < len(self.hand) for index in card_indices):
                # All indices are valid
                print(f"{self.name}, your hand is: {self.hand}")
                
                return card_indices
            else:
                print("Invalid indices. Please try again.")

    def discard_cards(self, card_indices):
        discarded_cards = [self.hand[i] for i in card_indices]
        self.hand = [card for i, card in enumerate(self.hand) if i not in card_indices]
        return discarded_cards