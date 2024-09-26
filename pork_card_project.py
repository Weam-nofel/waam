# Poker Game

import random

class Card:
    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return f"{self.rank} of {self.suit}"

class Deck:
    def __init__(self):
        self.cards = [Card(suit, rank) for suit in Card.suits for rank in Card.ranks]
        random.shuffle(self.cards)

    def deal(self):
        return self.cards.pop() if self.cards else None

class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []

    def draw(self, deck):
        card = deck.deal()
        if card:
            self.hand.append(card)

    def show_hand(self):
        return ', '.join(str(card) for card in self.hand)

class PokerGame:
    def __init__(self, player_names):
        self.deck = Deck()
        self.players = [Player(name) for name in player_names]

    def deal_hands(self):
        for _ in range(2):  # Each player gets 2 cards
            for player in self.players:
                player.draw(self.deck)

    def show_hands(self):
        for player in self.players:
            print(f"{player.name}'s hand: {player.show_hand()}")

if __name__ == "__main__":
    game = PokerGame(['Alice', 'Bob', 'Charlie'])
    game.deal_hands()
    game.show_hands()
