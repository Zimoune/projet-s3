#!/usr/bin/python3
# -*- coding: utf-8 -*-

import player as Player
import copy
import tictactoeGame as Game

# default_game

game = Game.make_game()

color = ["cross", "circle"]


# Getters
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
    :return: the second player
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


def get_pos_x(pos):
    """
    return the x position of pos
    :param pos: the position
    :return: the x position
    """
    return pos[0]


def get_pos_y(pos):
    """
    return the x position of pos
    :param pos: the position
    :return: the x position
    """
    return pos[1]


def get_cell_x(cell):
    """
    Get the x position of the cell
    :param cell: a cell
    :return: x position
    """
    return get_position_cell(cell)[0]


def get_cell_y(cell):
    """
    Get the y position of the cell
    :param cell: a cell
    :return: y position
    """
    return get_position_cell(cell)[1]


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
    :param x: the x's coordinate of a cell
    :type x: a integer
    :param y: the y's coordinate of a cell
    :type y: a integer
    :return: the cell color
    :rtype: a string
    """
    return situation[x][y]['color']


def get_position(situation, x, y):
    """
    Get the position of a cell of the game
    
    :param situation: the grid situation
    :type situation: list of lists
    :param x: the x's coordinate of a cell
    :type x: a integer
    :param y: the y's coordinate of a cell
    :type y: a integer
    :return: a position
    :rtype: a tuple
    """
    return situation[x][y]['position']


def get_grid_color(game, x, y):
    """
    Get the color of a cell of the game

    :param game: the game
    :type game: a game
    :param x: the x's coordinate of a cell
    :type x: a integer
    :param y: the y's coordinate of a cell
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
    Get the position of a cell of the game
    
    :param situation: the grid situation
    :type situation: list of lists
    :param x: the x's coordinate of a cell
    :type x: a integer
    :param y: the y's coordinate of a cell
    :type y: a integer
    :return: a cell of game
    :rtype: a cell
    """
    return situation[x][y]


def get_position_cell(cell):
    """
    return the x and y position of the cell
    :param cell: the cell
    :type cell: a cell
    :return: the x and y position of the cell
    :rtype: tuple
    """
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


# Setters
def set_color(situation, x, y, color):
    """
    Set the color for a cell of the game
    
    :param situation: the grid situation
    :type situation: list of lists
    :param x: the x's coordinate of a cell
    :type x: a integer
    :param y: the y's coordinate of a cell
    :type y: a integer
    :param color: the color to set
    :type color: a color
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


# Game Management
def initSituation(game_name):
    """builds the initial situation for the game. 

    :param game_name: the game for which the initial situation is created
    :type game_name: game
    :returns: *(situation)* the situation at the beginning of the game
    """
    return get_grid(game)


def nextSituations(situation, player):
    """
    returns the list of situations that can be reached from given situation by the player in the game

    :param situation: the current situation
    :type situation: a game situation
    :param player: the current player
    :type player: player
    :returns: *(list<situation>)* -- the list of situations that can be reached from given situation when player plays
    one round in the game
    """
    l_situation = []
    for position in available_position(situation, player):
        copy_situation = copy.deepcopy(situation)
        set_color(copy_situation, position[0], position[1], Player.get_color(player))
        l_situation.append(copy_situation)

    return l_situation


def available_position(situation, player):
    """
    check all available positions
    :param situation: the situation
    :type situation: a situation
    :param player: the current player:
    :type player: a player
    :return:
    """
    l_position = []
    for x_cell in situation:
        for cell in x_cell:
            position = get_position_cell(cell)
            if get_color(situation, position[0], position[1]) is None:
                l_position.append(position)
    return l_position


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
    if get_color(situation, x, y) is None:
        return ''

    elif get_color(situation, x, y) == 'cross':
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
        print('|{:^3}|{:^3}|{:^3}|'.format(XorO(situation, j, 2 - i), XorO(situation, j + 1, 2 - i),
                                           XorO(situation, j + 2, 2 - i)))

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
    :returns: *(game situation)* -- the game situation reached afte the human player play
    """
    coord = input("Where would you play? x, y ")

    try:
        x, y = coord.split(',')

        if not get_color(situation, int(x), int(y)) is None:
            print("Cell already used")
            humanPlayerPlays(game, player, situation)

        else:
            set_color(situation, int(x), int(y), Player.get_color(player))
            return situation

    except KeyboardInterrupt:
        raise KeyboardInterrupt

    except:
        print("input must be 2 separated with a coma x,y . (x = width , y = height) and values must be in [0,2]")
        humanPlayerPlays(game, player, situation)
    return situation


def coef(player):
    """
    Get a coefficient for the player

    :param player: a game player
    :type player: a player
    :return: the coefficient player
    :rtype: an integer
    """
    global game

    if get_player_name(player) == "Minmax":
        return 1

    else:
        return -1


def evalFunction(situation, player):
    """
    the evaluation function for the min-max algorithm. It evaluates the given situation, the evaluation function
    increases with the quality of the situation for the player
         
    :param situation: the current situation
    :type situation: a game situation
    :param player: the current player
    :type player: player
    :returns: *(number)* -- the score of the given situation for the given player.
        The better the situation for the minmax player, the higher the score. The opposite for human player.
    """
    cells_pts = 0
    dic_pts = make_dic(situation, player)
    o_player = get_inv_player(player)

    for x_list in situation:

        for cell in x_list:

            if get_color(situation, cell['position'][0], cell['position'][1]) == player['color']:
                cells_pts += dic_pts[get_position(situation, cell['position'][0], cell['position'][1])]

            elif get_color(situation, cell['position'][0], cell['position'][1]) == o_player['color']:
                cells_pts = cells_pts - dic_pts[get_position(situation, cell['position'][0], cell['position'][1])]

    if is_winner(situation):
        return 5*cells_pts*coef(player)

    else:
        return 1*cells_pts*coef(player)


def make_dic(situation, player):
    o_player = get_inv_player(player)
    dic_pts = {(0, 0): 0.75, (0, 1): 0.1, (0, 2): 0.75,
               (1, 0): 0.1, (1, 1): 1, (1, 2): 0.1,
               (2, 0): 0.75, (2, 1): 0.1, (2, 2): 0.75}
    for x_list in situation:

        for cell in x_list:
            x = get_cell_x(cell)
            y = get_cell_y(cell)

            if get_color(situation, x, y) is not None:
                color = get_color(situation, x, y)
                neighbors = available_neighbors(situation, cell)

                for neighbor in neighbors:
                    x_neigh = neighbor[0]
                    y_neigh = neighbor[1]
                    delta_x = x_neigh - x
                    delta_y = y_neigh - y
                    if get_color(situation, x_neigh, y_neigh) == color:

                        try:
                            dic_pts[(x_neigh + delta_x, y_neigh + delta_y)] += 1

                        except KeyError:
                            pass
    return dic_pts


def available_neighbors(situation, cell):
    """
    Get a position list of available neighbor of cell

    :param situation: the situation
    :type situation: a list of list
    :param cell: cell of game
    :type cell: a cell
    :return: a list of available neighbors
    :rtype: a list
    """
    position_list = []
    x = get_cell_x(cell)
    y = get_cell_y(cell)
    neighbors = [(x + 1, y), (x + 1, y + 1), (x + 1, y - 1), (x, y + 1), (x, y - 1), (x - 1, y - 1), (x - 1, y),
                 (x - 1, y + 1)]
    for neighbor in neighbors:
        x = get_pos_x(neighbor)
        y = get_pos_y(neighbor)
        if not is_in_grid(neighbor) or get_color(situation, x, y) is None:
            pass
        else:
            position_list = position_list + [get_position(situation, x, y)]
    return position_list


# Predicates
def isFinished(situation):
    """
    tells if the game is finished when in given situation

    :param situation: the tested situation
    :type situation: a game situation
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
    finish_position = [[(0, 0), (0, 1), (0, 2)],
                       [(0, 0), (1, 1), (2, 2)],
                       [(0, 1), (1, 1), (2, 1)],
                       [(0, 2), (1, 1), (2, 0)],
                       [(1, 0), (1, 1), (1, 2)],
                       [(2, 0), (2, 1), (2, 2)],
                       [(0, 0), (1, 0), (2, 0)],
                       [(0, 2), (1, 2), (2, 2)]]

    for position in finish_position:

        if get_color(situation, position[0][0], position[0][1]) == get_color(situation, position[1][0], position[1][1])\
                and get_color(situation, position[1][0], position[1][1]) == get_color(situation, position[2][0],
                                                                                      position[2][1]) \
                and get_color(situation, position[1][0], position[1][1]) is not None:
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


def is_in_grid(position):
    """"
    Return True if the position is in the grid

    :param position: a cell position
    :type position: a tuple
    :return: *(Boolean)* -- True if position is in grid
    """
    if 0 <= get_pos_x(position) <= 2 and 0 <= get_pos_y(position) <= 2:
        return True
    else:
        return False
