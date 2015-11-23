#!/usr/bin/python3
# -*- coding: utf-8 -*-

import player as Player

import tictactoeGame as Game

#### default_game ####

game = Game.make_game()

######################



##### Selectors #####

def get_player1(game):
    return game['player1']

def get_player2(game):
    return game['player2']

def get_grid(game):
    return game['grid']

def get_nb_plays(game):
    return game['nb_plays']

def get_color(situation, x, y):
    return situation[x][y]['color']

def get_position(situation, x, y):
    return situation[x][y]['position']

def get_grid_color(game, x, y):
    return game['grid'][x][y]['color']

def getWinner(game, situation, player):
    """
    Gives the winner of the game that end in situation

    :param game: the game 
    :type game: game
    :param situation: the situation which is a final game situation
    :type situation: a game situation
    :param player: the player who should have played if situation was not final (then other player plays previous turn)
    :type player: player
    :returns: *(player)* -- the winner player or None in case of tie game

    :CU: situation is a final situation
    """
    
    if get_nb_plays(game) == 9:
        return None
    else:
        return player

##### Constructors #####

def set_color(situation, x, y, color):
    situation[x][y]['color'] = color

def set_player1(player):
    game['player1'] = player

def set_player2(player):
    game['player2'] = player

##### Game Management #####

def initSituation(game_name):
    """builds the initial situation for the game. 

    :param game: the game for which the initial situation is created
    :type game: game
    :returns: *(situation)* the situation at the beginning of the game
    """
    try:
        set_player1(Player.create(input("name player 1: "), "cross"))
        set_player2(Player.create(input("name player 2: "), "circle"))
    except KeyboardInterrupt:
        raise KeyboardInterrupt
    except:
        initSituation(game)
    
    return get_grid(game)



def nextSituations(game, situation, player):
    """
    returns the list of situations that can be reached from given situation by the player in the game

    :param game: the game
    :type game: a two players game
    :param situation: the current situation
    :type situation: a game situation
    :param player: the current player
    :type player: player
    :returns: *(list<situtation>)* -- the list of situations that can be reached from given situation when player plays one round in the game
    """
    l_situations = []
    for x in range(3):
        for y in range(3):
            if get_color(situation, x, y) == None:
                l_situations += [get_position(situation, x, y)]
    return l_situations



def displaySituation(situation):
    """
    displays the situation

    :param situation: the situation to display
    :type situation: a game situation
    """

    pass

def humanPlayerPlays(game, player, situation):
    """
    makes the human player plays for given situation in the game

    :param game: the game 
    :type game: game
    :param player: the human player
    :type player: player
    :param situation: the current situation
    :type situation: a game situation
    :returns: *(game situtation)* -- the game situation reached afte the human player play
    """
    coord = input("Where would you play? x, y ")
    try:
        x,y = coord.split(',')
        set_color(situation, int(x), int(y), Player.get_color(player))
        return game
    except KeyboardInterrupt:
        raise KeyboardInterrupt
    except:
        print("input must be 2 seperated with a coma x,y . (x = width , y = height)")
        humanPlayerPlays(game,player,situation)


##### Predicates #####


def isFinished(situation ,  nb_plays):
    """
    tells if the game is finished when in given situation

    :param situation: the tested situation
    :type situation: a game situation
    :param nb_plays: number of plays (How much cells not empty
    :type nb_plays: a integer
    :returns: *(boolean)* -- True if the given situation ends the game
    """

    if nb_plays == 9:
        return True
    elif nb_plays >= 5:
        if get_color(situation, 0, 0) == get_color(situation, 0, 1) and get_color(situation, 0, 0) == get_color(situation, 0, 2):
            return True
        elif get_color(situation, 0, 0) == get_color(situation, 1, 1) and get_color(situation, 0, 0) == get_color(situation, 2, 2):
            return True
        elif get_color(situation, 0, 1) == get_color(situation, 1, 1) and get_color(situation, 0, 1) == get_color(situation, 2, 1):
            return True
        elif get_color(situation, 0, 2) == get_color(situation, 1, 1) and get_color(situation, 0, 2) == get_color(situation, 2, 0):
            return True
        elif get_color(situation, 1, 0) == get_color(situation, 1, 1) and get_color(situation, 1, 0) == get_color(situation, 1, 2):
            return True
        elif get_color(situation, 2, 0) == get_color(situation, 2, 1) and get_color(situation, 2, 0)== get_color(situation, 2, 2):
            return True
        elif get_color(situation, 0, 0) == get_color(situation, 1, 0) and get_color(situation, 0, 0) == get_color(situation, 2, 0):
            return True
        elif get_color(situation, 0, 2) == get_color(situation, 1, 2) and get_color(situation, 0, 2) == get_color(situation, 2, 2):
            return True
        else:
            return False
    else:
        return False



def playerCanPlay(game, situation, player):
    """
    tells whether player can play in given situation

    :param game: the game 
    :type game: game
    :param situation: the situation to display
    :type situation: a game situation
    :param player: the player
    :type player: player
    :returns: *(boolean)* -- True iff player can play in situation
    """
    for x in range(3):
        for y in range(3):
            if get_grid_color(game, x, y) != get_color(situation, x, y):
                if get_grid_color(game, x, y) == None:
                    return True
                else:
                    return False
    return False



            
