from go_fish.go_fish import Deck, Player
from go_fish import app
from flask import render_template, url_for, flash, redirect, request, abort


@app.route("/")
@app.route("/home")
def home():

    fresh_deck = Deck()
    first_player = Player(fresh_deck, "Player 1")
    second_player = Player(fresh_deck, "Player 2")
    # game(fresh_deck,first_player,second_player)
    deck_len = len(fresh_deck.new_deck)
    your_pair_len = len(first_player.pair_deck)
    opp_pair_len = len(second_player.pair_deck)

    return render_template('go_fish.html', title='Go Fish Game!'
                                        , first_player=first_player
                                        , opp=second_player
                                        , fresh_deck=fresh_deck
                                        , deck_len=deck_len
                                        , your_pair_len=your_pair_len
                                        , opp_pair_len=opp_pair_len)
