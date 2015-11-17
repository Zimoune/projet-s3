#!/usr/bin/python3
# -*- coding: utf-8 -*-

import player as Player

import tictactoeGame as Game

#### default_game ####

game = Game.make_game()

######################



def initSituation(game):
    """builds the initial situation for the game. 

    :param game: the game for which the initial situation is created
    :type game: game
    :returns: *(situation)* the situation at the beginning of the game
    """
    data = input("names player?  ")
    try:
        l_name = data.split(",")
        name1 =  l_name[0]
        name2 = l_name[1]
        game['player1'] == Player.create(name1, "cross")
        game['player2'] == Player.create(name2, "circle")
    except KeyboardInterrupt:
        raise KeyboardInterrupt
    except:
        initSituation(game)
    
    return game['grid']



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
        if situation[0][0]['color'] == situation[0][1]['color'] and situation[0][0]['color'] == situation[0][3]['color']:
            return True
        if situation[1][0]['color'] == situation[1][1]['color'] and situation[1][0]['color'] == situation[1][3]['color']:
            return True
        if situation[2][0]['color'] == situation[2][1]['color'] and situation[2][0]['color'] == situation[2][3]['color']:
            return True

        if situation[0][0]['color'] == situation[1][0]['color'] and situation[0][0]['color'] == situation[2][0]['color']:
            return True
        if situation[0][1]['color'] == situation[1][1]['color'] and situation[2][1]['color'] == situation[2][1]['color']:
            return True
        if situation[0][2]['color'] == situation[1][2]['color'] and situation[0][2]['color'] == situation[2][2]['color']:
            return True

        
        if situation[0][0]['color'] == situation[1][1]['color'] and situation[0][0]['color'] == situation[2][2]['color']:
            return True
        if situation[0][2]['color'] == situation[1][1]['color'] and situation[0][2]['color'] == situation[2][0]['color']:
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
            if game['grid'][x][y]['color'] != situation[x][y]['color']:
                if game['grid'][x][y]['color'] == None:
                    return True
                else:
                    return False
    return False


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
            if situation[x][y]['color'] == None:
                l_situations += [situation[x][y]['position']]
    return l_situations
    



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
    
    if game['nb_plays'] == 9:
        return None
    else:
        return player





def displaySituation(situation):
    """
    displays the situation

    :param situation: the situation to display
    :type situation: a game situation
    """

    game['grid'] == situation


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
    coord = input("Where would you play?  ")
    try:
        x,y = coord.split(',')
        situation[int(x)][int(y)]["color"] = player["color"]
        return game
    except KeyboardInterrupt:
        raise KeyboardInterrupt
    except:
        print("input must be 2 seperated with a coma x,y . (x = width , y = height)")
        humanPlayerPlays(game,player,situation)




            
