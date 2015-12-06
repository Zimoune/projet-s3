#!/usr/bin/python3
# -*- coding: utf-8 -*-

import player as Player
import minmax as IA

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
    ask_players_names(Game.color)
    situation = Game.initSituation(game_name)

    while not Game.isFinished(situation):

        if currentPlayer == None:
            currentPlayer = Game.get_player1(Game.game)

        elif currentPlayer == Game.get_player1(Game.game):
            currentPlayer = Game.get_player2(Game.game)

        else:
            currentPlayer = Game.get_player1(Game.game)

        Game.displaySituation(situation)
        print(Player.get_name(currentPlayer)," turn")

        if currentPlayer['name'] == "Minmax":
            situation = IA.min_max1(situation, currentPlayer)

        else:
            situation = Game.humanPlayerPlays(Game.game, currentPlayer, situation)

        Game.game['nb_plays'] += 1
    winner = Game.getWinner(Game.game, situation, currentPlayer)

    if winner == None:
        print("equality !")

    else:
        print(winner['name'], "won")


def ask_players_names(color):
    try:
        mod.set_player1(Player.create(input("name player 1: "), color[0]))
        mod.set_player2(Player.create(input("name player 2: "), color[1]))

    except KeyboardInterrupt:
        raise KeyboardInterrupt

    except:
        ask_players_names()
          
if __name__ == '__main__':
    play()
