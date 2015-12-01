#!/usr/bin/python3
# -*- coding: utf-8 -*-

import player

currentPlayer = None

def play():

    global currentPlayer
    global mod
    game_name = "tictactoe"
    if game_name == "nim":
        import nim_game as Game
        mod = __import__("nim_game")
    elif game_name == "othello":
        import othello as Game
        mod = __import__("othello")
    else:
        import tictactoe as Game
        mod = __import__("tictactoe")

    ask_players_names()
    situation = Game.initSituation(game_name)
    while not Game.isFinished(situation):
        if currentPlayer == None:
            currentPlayer = Game.get_player1(Game.game)
        elif currentPlayer == Game.get_player1(Game.game):
            currentPlayer = Game.get_player2(Game.game)
        else:
            currentPlayer = Game.get_player1(Game.game)
        Game.displaySituation(situation)
        print(player.get_name(currentPlayer)," turn")
        situation = Game.humanPlayerPlays(Game.game, currentPlayer, situation)
    winner = Game.getWinner(Game.game, situation, currentPlayer)
    if winner == None:
        print("equality !")
    else:
        print(winner['name'], "won")


def ask_players_names():
    try:
        mod.set_player1(player.create(input("name player 1: "), "cross"))
        mod.set_player2(player.create(input("name player 2: "), "circle"))
    except KeyboardInterrupt:
        raise KeyboardInterrupt
    except:
        ask_players_names()
          
if __name__ == '__main__':
    play()
