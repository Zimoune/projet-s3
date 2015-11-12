#!/usr/bin/python3
# -*- coding: utf-8 -*-

import player as Player


#------Color-----#

cross=""
circle=""

#----------------#

def initSituation(game):
    """builds the initial situation for the game. 

    :param game: the game for which the initial situation is created
    :type game: game
    :returns: *(situation)* the situation at the beginning of the game
    """
    return make_game()



def isFinished(situation):
    """
    tells if the game is finished when in given situation

    :param situation: the tested situation
    :type situation: a game situation
    :returns: *(boolean)* -- True if the given situation ends the game
    """
    raise NotImplementedError( "isFinished must be defined as a function to test end of game" )



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
    raise NotImplementedError( "playerCanPlay must be defined to determine whether player can play")


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
    raise NotImplementedError( "nextSituations must be defined as a function that provides successor situations" )



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
    raise NotImplementedError( "getWinner function must be defined to tell who win the game" )    




def displaySituation(situation):
    """
    displays the situation

    :param situation: the situation to display
    :type situation: a game situation
    """
    raise NotImplementedError( "displaySituation must be defined to display the situation on the screen" )


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
        game[2][int(x)][int(y)]["color"] = player["color"]
        return game
    except KeyboardInterrupt:
        raise KeyboardInterrupt
    except:
        print("input must be 2 seperated with a coma x,y . (x = width , y = height)")
        humanPlayerPlays(game,player,situation)
    raise NotImplementedError( "humanPlayerPlays must be defined to make the human player plays one round, the reached new situation must be returned" )




def make_game(name1, name2, grid):
    """
    return a tictactoe game of size 3*3 cells and with two player

    :param name1: a name
    :type name1: a string
    :param name2: a name
    :type name2: a string
    :return: a game
    :rtype: a tuple
    """
    player1 = Player.create(name1 , cross)
    player2 = Player.create(name2 , circle)
    return(player1, player2, grid)



def make_grid():
    """
    return a tictactoe grid of size 3*3 cells

    :return: a grid with 3*3 cells
    :rtype: llist of list of cells
    """
    return [[make_cell() for x in range(3)] for y in range(3)]
    



def make_cell():
    """
    return a tictactoe cell

    :return: a cell with his color
    :rtype: a cell
    """
    return {"color" : None}
            
