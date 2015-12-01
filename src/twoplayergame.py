#!/usr/bin/python3
# -*- coding: utf-8 -*-

import tictactoe as Game
import player

currentPlayer = None

def play():
    global currentPlayer
    situation = Game.initSituation("tictactoe")
    while not Game.isFinished(situation):
        if currentPlayer == None:
            currentPlayer = Game.get_player1(Game.game)
        elif currentPlayer == Game.get_player1(Game.game):
            currentPlayer = Game.get_player2(Game.game)
        else:
            currentPlayer = Game.get_player1(Game.game)
        Game.displaySituation(situation)
        print(player.get_name(currentPlayer)," turn")
        Game.humanPlayerPlays(Game.game, currentPlayer, situation)
    winner = Game.getWinner(Game.game, situation, currentPlayer)
    print(winner['name'], "won")
          
if __name__ == '__main__':
    play()
