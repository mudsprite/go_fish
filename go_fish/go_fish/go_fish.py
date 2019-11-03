import random
from flask import render_template, url_for, flash, redirect, request, abort

class Card():
    """Card Class creates the possible options options for a card."""
    possible_cards=["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
    possible_suit=["h","s","c","d"]

class Deck(Card):
    """Card Class creates a new deck of 52 cards in order. Deals cards to players and manages the current available cards in the deck."""
    def __init__(self):
        self.hand_cache = []
        self.new_deck = []

        for suit in Card.possible_suit:
            for card in Card.possible_cards:
                self.new_deck.append(suit+card)

    def deal(self):
        player_hand = []
        while len(player_hand) < 7:
            random_card = Card.possible_suit[random.randint(0,len(Card.possible_suit)-1)] + Card.possible_cards[random.randint(0,len(Card.possible_cards)-1)]
            if random_card not in player_hand and random_card not in self.hand_cache:
                player_hand.append(random_card)
        self.hand_cache+=player_hand
        self.update()
        return player_hand

    # This function takes a player as a parameter and increases their deck by one random card left in the deck
    def draw_card(self,player):
        random_card = random.choice(self.new_deck)
        self.new_deck.remove(random_card)
        self.hand_cache.append(random_card)
        player.hand.append(random_card)
        self.update()

    def update(self):
        for card in self.hand_cache:
            if card in self.new_deck:
                self.new_deck.remove(card)

class Player(Deck):
    """Player Class creates a player and inherrits the deck class for access to the deal function"""
    def __init__(self, deck, name):
        self.hand = deck.deal()
        self.name = name
        self.pair_deck = []

    def debug_info(self, deck, player2):
        print("\nCurrent Deck:","".join(deck.new_deck))
        print("Player1 Deck:","".join(self.hand))
        print("Player2 Deck:","".join(player2.hand))
