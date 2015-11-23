#!/usr/bin/python3
# -*- coding: utf-8 -*-

import tictactoe as Game
import player

currentPlayer = None

def play():
    global currentPlayer
    situation = Game.initSituation("tictactoe")
    if currentPlayer == None:
        currentPlayer = Game.get_player1(Game.game)
    elif currentPlayer == Game.get_player1(Game.game):
        currentPlayer = Game.get_player2(Game.game)
    print(player.get_name(currentPlayer)," turn")
    #while not Game.isFinished(Game.game):   
        
    
if __name__ == '__main__':
    play()
