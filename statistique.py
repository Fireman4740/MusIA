import itertools
import collections
from collections import Counter
# Define the values of the cards
card_values = {
    'Roi': 12,
    'Cavalier': 11,
    'Valet': 10,
    '7': 7,
    '6': 6,
    '5': 5,
    '4': 4,
    '3': 3,
    '2': 2,
    'As': 1
}

# Define the deck of cards
deck = ['Roi', 'Cavalier', 'Valet', '7', '6', '5', '4', '3', '2', 'As'] * 4

# Define the given hand
given_hand = ['Roi', 'Roi', '2', 'As']

for card in given_hand:
    deck.remove(card)
# Calculate the value of the given hand
given_hand_value = [card_values[card] for card in given_hand]
given_hand_value.sort(reverse=True)
print (given_hand_value)

# Generate all possible hands
possible_hands = list(itertools.combinations(deck, 4))

# Initialize the count of wins
wins = 0

# Compare the given hand with all possible hands
for hand in possible_hands:
    hand_value = [card_values[card] for card in hand]
    hand_value.sort(reverse=True)
    if given_hand_value > hand_value:
        wins += 1

# Calculate the probability of winning
probabilityGrand = wins / len(possible_hands) *100

winsP = 0

# Compare the given hand with all possible hands
given_hand_value.sort(reverse=False)
for hand in possible_hands:
    hand_value = [card_values[card] for card in hand]
    hand_value.sort(reverse=False)
    if given_hand_value < hand_value:
        winsP += 1

# Calculate the probability of winning
probabilityPetit = winsP / len(possible_hands) *100


# Initialize the count of wins
winsP = 0

def calculate_rank(hand):
    counts = Counter(hand)
    if 4 in counts.values():
        return (3, max(card_values[card] for card in counts.keys()))  # rank 3 for a carré (considered as a double pair)
    elif 3 in counts.values():
        return (2, max(card_values[card] for card in counts.keys()))  # rank 2 for a brelan
    elif list(counts.values()).count(2) == 2:
        return (3, max(card_values[card] for card in counts.keys()))  # rank 3 for a double pair
    elif 2 in counts.values():
        return (1, max(card_values[card] for card in counts.keys()))  # rank 1 for a pair
    else:
        return (0, 0)  # no combination

# Calculate the rank of the given hand
given_hand_rank = calculate_rank(given_hand)

# Generate all possible hands
possible_hands = list(itertools.combinations(deck, 4))

# Filter the possible hands to keep only those with a pair, brelan or carré
possible_hands = [hand for hand in possible_hands if calculate_rank(hand)[0] > 0]

# Identify pairs, three-of-a-kinds and four-of-a-kinds in the given hand
for hand in possible_hands:
    if given_hand_rank > calculate_rank(hand):
        winsP += 1

# Calculate the probability of winning
probabilityPaires = winsP / len(possible_hands) *100

print(f"The probability of winning with the given hand in the 'Paires' phase is {probabilityPaires:.2f}%")

print(f"The probability of winning with the given hand is  {probabilityGrand:.2f}% at the grand ")
print(f"The probability of winning with the given hand is  {probabilityPetit:.2f}% at the petit ")
