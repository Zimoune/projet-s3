#!/usr/bin/python3
# -*- coding: utf-8 -*-

import player as Player

import tictactoeGame as Game

#### default_game ####

game = Game.make_game()

######################



##### Selectors #####

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

def get_grid(game):
    """
    Get the grid of the game
    
    :param game: the game
    :type game: a game
    :return: the grid game
    :rtype: a grid
    """
    return game['grid']

def get_nb_plays(game):
    """
    Get the number of plays of the game
    
    :param game: the game
    :type game: a game
    :return: the number of plays
    :rtype: a integer
    """
    return game['nb_plays']

def get_color(situation, x, y):
    """
    Get the color of a cell of the game
    
    :param situation: the grid situation
    :type situation: list of lists
    :param x: the x's codinate of a cell
    :type x: a integer
    :param y: the y's codinate of a cell
    :type y: a integer
    :return: the cell color
    :rtype: a string
    """
    return situation[x][y]['color']

def get_position(situation, x, y):
    """
    Get the postion of a cell of the game
    
    :param situation: the grid situation
    :type situation: list of lists
    :param x: the x's codinate of a cell
    :type x: a integer
    :param y: the y's codinate of a cell
    :type y: a integer
    :return: a position
    :rtype: a tuple
    """
    return situation[x][y]['position']

def get_grid_color(game, x, y):
    """
    Get the color of a cell of the game
    
    :param situation: the grid situation
    :type situation: list of lists
    :param x: the x's codinate of a cell
    :type x: a integer
    :param y: the y's codinate of a cell
    :type y: a integer
    :return: the cell color
    :rtype: a string
    """
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
    """
    Set the color for a cell of the game
    
    :param situation: the grid situation
    :type situation: list of lists
    :param x: the x's codinate of a cell
    :type x: a integer
    :param y: the y's codinate of a cell
    :type y: a integer
    :return: None
    :sidegrid effect: set the color of the cell
    """
    situation[x][y]['color'] = color

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


def coef(player):
    """
    Get a coeficient for the player

    :param player: a game player
    :type player: a player
    :return: the coeficient player
    :rtype: an integer
    """
    global game
    if player == get_player2(game):
        return -1
    else:
        return 1


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
    cells_pts = 0
    dic_pts = {(0,0) : 0.75 , (0,1) : 0 , (0,2) : 0.75 ,
               (1,0) : 0    , (1,1) : 1 , (1,2) : 0 ,
               (2,0) : 0.75 , (2,1) : 0 , (2,1) : 0.75 }

    for x_list in situation:
        for cell in x_list:
            print(cell)
            if get_color(situation, cell['position'][0] , cell['position'][1]) == player['color']:
                cells_pts += dic_pts[get_position(situation, cell['position'][0] , cell['position'][1])]
    if is_winner(situation) == True:
        return 5*cell_pts*coef(player)
    else:
        return 1*cells_pts*coef(player)


##### Predicates #####


def isFinished(situation):
    """
    tells if the game is finished when in given situation

    :param situation: the tested situation
    :type situation: a game situation
    :param nb_plays: number of plays (How much cells not empty
    :type nb_plays: a integer
    :returns: *(boolean)* -- True if the given situation ends the game
    """

    if get_nb_plays(game) == 9:
        return True
    else:
        return is_winner(situation)

def is_winner(situation):
    """
    Get true if the situation have a winner

    :param situation: the game situation
    :type situation: a game
    :return: *Boolean* True if the situation have a winner
    """
    finish_position = [[(0,0),(0,1),(0,2)],
                       [(0,0),(1,1),(2,2)],
                       [(0,1),(1,1),(2,1)],
                       [(0,2),(1,1),(2,0)],
                       [(1,0),(1,1),(1,2)],
                       [(2,0),(2,1),(2,2)],
                       [(0,0),(1,0),(2,0)],
                       [(0,2),(1,2),(2,2)]]
    for position in finish_position:
        if get_color(situation, position[0][0],position[0][1]) == get_color(situation, position[1][0],position[1][1]) and get_color(situation, position[1][0],position[1][1]) == get_color(situation, position[2][0],position[2][1]) and not get_color(situation, position[1][0],position[1][1]) == None:
            return True
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



            
