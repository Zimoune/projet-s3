#!/usr/bin/python3
# -*- coding: utf-8 -*-


"""
 .. topic:: Module ``nim_game``

   :author: `FIL - IEEA - Univ. Lille1.fr <http://portail.fil.univ-lille1.fr>`_

   :date:  2015, october

   This module is an implementation of the :mod:`abstractgame` for the Nim game.

   The Nim game rules are the following :
   
     * initially there is a number of pebbles on the table
     * alternately each player takes 2 or 3 pebbles 
     * when one player takes the last pebble he loses
     * if only one pebble remains on the table, game is tie
   
   A game situation is then simply defined by a number : the number of pebbles on the table.

"""


import player as Player

_DEFAULT_PEBBLES = 25

game = {"player1": "", "player2": "", "nb_plays": 0}

color = ['', '']


def initSituation(game):
    """builds the initial situation for the game.  
    A Nim game situation is simply defined by a number : the number of pebbles on the table.
    Either a 'pebbles' field exist in game, the its value is used, or default number of pebbles (defined in _DEFAULT_PEBBLES constant) is used.

    :param game: the game for which the initial situation is created
    :type game: game
    :returns: *(situation)* the siutation at the beginning of the game, here just a number
    """
    if 'pebbles' in game:
        return game['pebbles']

    else:
        return _DEFAULT_PEBBLES
    

def isFinished(situation):
    """
    tells if the game is finished when in given situation. In Nim game, situation is final when it remains 0 or 1 pebble

    :param situation: the tested situation
    :type situation: a game situation
    :returns: *(boolean)* -- True if the given situation ends the game
    """
    print(situation)
    return situation <= 1 


def playerCanPlay(game, situation, player):
    """
    tells whether player can play in given situation, in Nim game, player can always play when game is not finished

    :param game: the game 
    :type game: game
    :param situation: the situation to display
    :type situation: a game situation
    :param player: the player
    :type player: player
    :returns: *(boolean)* -- True iff player can play in situation
    """
    return True


def nextSituations(situation, player):
    """
    returns the list of situations that can be reached from given situation by the player in the game

    In Nim game, the possible plays are taking 2 or 3 pebbles when possible, then next situations are situations with 2 or 3 pebbles less.

    :param situation: the current situation
    :type situation: a game situation
    :param player: the current player
    :type player: player
    :returns: *(list<situtation>)* -- the list of situations that can be reached from given situation when player plays one round in the game
    """
    result = []
    if situation >= 3:
        # taking 3 pebbles is possible
        result.append(situation-3)

    if situation >= 2:
        # taking 2 pebbles is possible
        result.append(situation-2)

    return result



def getWinner(game, situation, player):
    """
    Gives the winner of the game that end in situation. There is a tie game when 1 pebble remains, else the previous player has taken the last pebble, then the current player wins.

    
    :param game: the game 
    :type game: game
    :param situation: the situation which is a final game situation
    :type situation: a game situation
    :param player: the player who should have played if situation was not final (then other player plays previous turn)
    :type player: player
    :returns: *(player)* -- the winner player or None in case of tie game

    :CU: situation is a final situation
    """
    if situation == 1:
        # tie game
        return None

    else:
        # other player took last pebble, player wins
        return player

def evalFunction(situation, player):
    """
    the evaluation function for the min-max algorithm. It evaluates the given situation, the evaluation function increases with the quality of the situation for the player
         
    :param situation: the current situation
    :type situation: a game situation
    :param player: the current player
    :type player: player
    :returns: *(number)* -- the score of the given situation for the given player.
        The better the situation for the minmax player, the higher the score. The opposite for human player.
    """
    if situation == 1:
        return 0*coef(player)

    else:
        return 1*coef(player)




def displaySituation(situation):
    """
    displays the situation, here the number of pebbles on the table

    :param situation: the situation to display
    :type situation: a game situation
    """
    return print("there is "+str(situation)+" pebbles on the table")


def humanPlayerPlays(game, player, situation):
    """
    makes the human player plays for given situation in the game. Player can take 2 or 3 pebbles (if enough).

    :param game: the game 
    :type game: game
    :param player: the human player
    :type player: player
    :param situation: the current situation
    :type situation: a game situation
    :returns: *(game situtation)* -- the game situation reached afte the human player play
    """
    if situation >= 2:
        number_pebbles = [2,3]
        number_message = "2 or 3"

    else:
        number_pebbles = [3]
        number_message = "3"
    return (situation - _input_pebbles(player, number_pebbles, number_message))

def _input_pebbles(player, number_pebbles, number_message):
    """
    reads the number of pebbles taken by player
    :returns: *(int)* -- the number of taken pebbles
    """
    print(Player.get_name(player)+" it's your turn, you can take "+number_message+" pebbles.")
    nb_taken_pebbles = input("how many pebbles do you take ? ")

    try:
        if int(nb_taken_pebbles) in number_pebbles:
            return int(nb_taken_pebbles)
        # else : invalid input  : redo input

    except ValueError:
        # input is not an integer : redo input
        pass

    print("illegal play, you can only take "+number_message+" pebbles")
    return _input_pebbles(player,number_pebbles, number_message)


def coef(player):
    if player == get_player1(game):
        return -1

    else:
        return 1   

def get_player1(game):
    """
    Get the player one of the game

    :param game: the game
    :type game: a game
    :return: the first player
    :rtype: a player
    """
    return game['player1']

def get_player2(game):
    """
    Get the player two of the game

    :param game: the game
    :type game: a game
    :return: the seconde player
    :rtype: a player
    """
    return game['player2']

def set_player1(player):
    """
    Set the player 1 for the game

    :param player: the player 1 of the game
    :type player: a player
    :return: None
    :sidegrid effect: set the player 1 of the game
    """
    game['player1'] = player

def set_player2(player):
    """
    Set the player 2 for the game

    :param player: the player 2 of the game
    :type player: a player
    :return: None
    :sidegrid effect: set the player 2 of the game
    """
    game['player2'] = player

def get_inv_player(player):
    """
    Get the other player of the game

    :param player: a game player
    :type player: a player
    :return: a game player
    :rtype: a player
    """
    global game
    if player == get_player1(game):
        return get_player2(game)
    else:
        return get_player1(game)
