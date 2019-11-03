#Back end concept for go fish card game in python

# GENERATE A RANDOM 7 CARD HAND
import random


class Card():
    """Card Class creates the possible options options for a card."""
    possible_cards=["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
    possible_suit=["H","S","C","D"]

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
            random_card = random.choice(Card.possible_suit) + random.choice(Card.possible_cards)
            if random_card not in player_hand and random_card not in self.hand_cache:
                player_hand.append(random_card)
        self.hand_cache.append(player_hand)
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
        self.score = 0

    def player_turn(self,opp, deck):
        turn_over = False
        while not turn_over:
            print("Your current hand {}".format(" ".join(self.hand)))
            card_count = len(self.hand)
            card_arr = [i for i in range(1,card_count+1)]
            do_you_have = input("Please chose a card between 1 and {}:".format(card_count))
            if do_you_have.isnumeric():
                if int(do_you_have) not in card_arr:
                    print('Invalid entry!')
                else:
                    # create a list of each players hand, card only suit is ignored
                    opp_hand = [card[1:] for card in opp.hand]
                    self_hand = [card[1:] for card in self.hand]
                    # assign the compartive card vaue
                    comp_card = self.hand[int(do_you_have)-1][1:]
                    # if we find a match in the opposite hand then we can take both cards and put them in our pair_deck
                    if comp_card in opp_hand:
                        self.score+=1
                        opp.hand.pop(opp_hand.index(comp_card))
                        self.hand.pop(self_hand.index(comp_card))
                    else:
                        deck.draw_card(self)
                        print("Go fish!")
                        print("_____________________________________________________________")
                        print("You now have {} cards in your hand!".format(len(self.hand)))
                        print("There are {} cards left in the deck".format(len(deck.new_deck)))
                        print("_____________________________________________________________")
                        turn_over = True
            else:
                print('invalid entry')



fresh_deck = Deck()
first_player = Player(fresh_deck, "Player 1")
second_player = Player(fresh_deck, "PLayer 2")

def game():
    while len(fresh_deck.new_deck) > 0:
        print("{}'s turn".format(first_player.name))
        first_player.player_turn(second_player,fresh_deck)
        print("{}'s turn".format(second_player.name))
        second_player.player_turn(first_player,fresh_deck)


    if first_player.score > second_player.score:
        print("{} WINS!".format(first_player.name))
        print("{} to {}".format(first_player.score,second_player.score))
    elif first_player.score == second_player.score:
        print("Tie!")
        print("{} to {}".format(second_player.score,first_player.score))
    else:
        print("{} WINS!".format(second_player.name))
        print("{} to {}".format(second_player.score,first_player.score))

game()
