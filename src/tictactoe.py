#!/usr/bin/python3
# -*- coding: utf-8 -*-

import player as Player
import copy
import tictactoeGame as Game

#### default_game ####

game = Game.make_game()

color = ["cross", "circle"]

######################



##### Getters #####

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

def get_player_name(player):
    """
    Get the name of a player

    :param player: a game player
    :type player: a player
    :return: the player name
    :rtype: a string
    """
    return player['name']

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

def get_color_cell(cell):
    """
    get the color of a cell

    :param cell: a cell of game
    :type cell: a cell
    :return: the cell's color
    :rtype: string
    """
    global game
    pos = cell['position']
    return get_color(get_grid(game), pos[0], pos[1])

def get_cell(situation, x, y):
    """
    Get the postion of a cell of the game
    
    :param situation: the grid situation
    :type situation: list of lists
    :param x: the x's codinate of a cell
    :type x: a integer
    :param y: the y's codinate of a cell
    :type y: a integer
    :return: a cell of game
    :rtype: a cell
    """
    return situation[x][y]

def get_position_cell(cell):
    return cell['position']


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

##### Setters #####

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
    return get_grid(game)


def nextSituations(situation, player):
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
    for x_list in situation:

        for cell in x_list:
            x_cell = get_position_cell(cell)[0]
            y_cell = get_position_cell(cell)[1]
            copy_situation = copy.deepcopy(situation)

            if get_color_cell(cell) == None:
                set_color(copy_situation, x_cell, y_cell, player['color'])
                l_situations.append(copy_situation)


    return l_situations


def XorO(situation, x, y):
    """
    Return the symbol of the cell

    :param situation: the situation to display
    :type situation: a game situation
        :param x: the x's codinate of a cell
    :type x: a integer
    :param y: the y's codinate of a cell
    :type y: a integer
    :return: the cell symbol
    :rtype: a string
    """
    if get_color(situation, x, y)== None:
        return ''

    elif get_color(situation, x, y)=='cross':
        return 'X'

    else:
        return 'O'

def displaySituation(situation):
    """
    displays the situation

    :param situation: the situation to display
    :type situation: a game situation
    """
    for i in range(3):
        j = 0
        print(" --- --- --- ")
        print('|{:^3}|{:^3}|{:^3}|'.format(XorO(situation, j, 2-i),XorO(situation, j+1, 2-i),XorO(situation, j+2, 2-i)))

    print(" --- --- --- ")

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

        if not get_color(situation, int(x), int(y)) == None:
            print("Cell already used")
            humanPlayerPlays(game, player, situation)

        else:
            set_color(situation, int(x), int(y), Player.get_color(player))
            return situation

    except KeyboardInterrupt:
        raise KeyboardInterrupt

    except:
        print("input must be 2 seperated with a coma x,y . (x = width , y = height) and values must be in [0,2]")
        humanPlayerPlays(game,player,situation)
    return situation

def coef(player):
    """
    Get a coeficient for the player

    :param player: a game player
    :type player: a player
    :return: the coeficient player
    :rtype: an integer
    """
    global game

    if get_player_name(player) == "Minmax":
        return 1

    else:
        return -1


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
    dic_pts = {(0,0) : 0.75 , (0,1) : 0.1 , (0,2) : 0.75 ,
               (1,0) : 0.1    , (1,1) : 1 , (1,2) : 0.1 ,
               (2,0) : 0.75 , (2,1) : 0.1 , (2,2) : 0.75 }
    o_player = get_inv_player(player)

    for x_list in situation:

        for cell in x_list:

            if get_color(situation, cell['position'][0] , cell['position'][1]) == player['color']:
                cells_pts += dic_pts[get_position(situation, cell['position'][0] , cell['position'][1])]

            elif get_color(situation, cell['position'][0] , cell['position'][1]) == o_player['color']:
                cells_pts = cells_pts - dic_pts[get_position(situation, cell['position'][0] , cell['position'][1])]

    if is_winner(situation) == True:
        return 5*cells_pts*coef(player)

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
    global game
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
    return True
