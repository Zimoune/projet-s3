#!/usr/bin/python3
# -*- coding: utf-8 -*-

import player as Player
import othelloGame as Game
import copy

# default_game
game = Game.make_game()

color = ["white", "black"]


######################


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


def get_player_name(player):
    """
    Get the name of a player

    :param player: a game player
    :type player: a player
    :return: the player name
    :rtype: a string
    """
    return player['name']


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
    :param x: the x's coordinate of a cell
    :type x: a integer
    :param y: the y's coordinate of a cell
    :type y: a integer
    :return: the cell color
    :rtype: a string
    """
    return situation[x][y]['color']


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


def get_cell_color(cell):
    """
    Get the color of a cell
    :param cell: the cell
    :return: a color
    """
    return cell['color']


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

    :param x: the x's coordinate of a cell
    :type x: a integer
    :param y: the y's coordinate of a cell
    :type y: a integer
    :return: the cell color
    :rtype: a string
    """
    return game['grid'][x][y]['color']


def get_position_cell(cell):
    """
    Get the position of cell

    :param cell: cell of game
    :type cell: a cell
    :return: a position cell
    :rtype: a tuple
    """
    return cell['position']


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
    nmb1 = 0
    nmb2 = 0
    for x in range(8):

        for y in range(8):

            if get_color(situation, x, y) == color[0]:
                nmb1 += 1

            elif get_color(situation, x, y) == color[1]:
                nmb2 += 1

    if nmb1 > nmb2:
        return get_player1(game)

    elif nmb1 == nmb2:
        return None

    else:
        return get_player2(game)


# Setters

def set_color(situation, x, y, color):
    """
    Set the color for a cell of the game
    
    :param situation: the grid situation
    :type situation: list of lists
    :param x: the x's codinate of a cell
    :type x: a integer
    :param y: the y's codinate of a cell
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
    :side grid effect: set the player 2 of the game
    """
    game['player2'] = player


# Game Management

def initSituation(game_name):
    """builds the initial situation for the game. 

    :param game_name: the game for which the initial situation is created
    :type game_name: game
    :returns: *(situation)* the situation at the beginning of the game
    """
    global game
    set_color(get_grid(game), 3, 3, 'white')
    set_color(get_grid(game), 4, 4, 'white')
    set_color(get_grid(game), 3, 4, 'black')
    set_color(get_grid(game), 4, 3, 'black')

    return get_grid(game)


def isFinished(situation):
    """
    tells if the game is finished when in given situation

    :param situation: the tested situation
    :type situation: a game situation
    :returns: *(boolean)* -- True if the given situation ends the game
    """
    global game
    if get_nb_plays(game) == 60:
        return True
    players = [get_player1(game), get_player2(game)]
    for player in players:
        for position in extremity_pos(situation):
            if catch_play(situation, position, player):
                return False
    return True


def catch_play(situation, position, player):
    """
    Get True if a position is a catch play for a player

    :param situation: a situation
    :type situation: list of list
    :param position: a position
    :type position: a tuple
    :param player: a game player
    :type player: a player
    :return: *(Boolean)* --True if the position is a catch play
    """
    x = get_pos_x(position)
    y = get_pos_y(position)
    neighbors = [(x + 1, y), (x + 1, y + 1), (x + 1, y - 1), (x, y + 1), (x, y - 1), (x - 1, y - 1), (x - 1, y),
                 (x - 1, y + 1)]
    for neighbor in neighbors:
        x_neigh = get_pos_x(neighbor)
        y_neigh = get_pos_y(neighbor)
        delta_x = x_neigh - x
        delta_y = y_neigh - y
        while is_in_grid((x_neigh, y_neigh)) and get_color(situation, x_neigh, y_neigh) != Player.get_color(player) \
                and get_color(situation, x_neigh, y_neigh) is not None:
            x_neigh += delta_x
            y_neigh += delta_y
            if is_in_grid((x_neigh, y_neigh)):
                if get_color(situation, x_neigh, y_neigh) == Player.get_color(player):
                    return True
    return False


def available_position(situation, player):
    extreme = extremity_pos(situation)
    list_position = []
    for position in extreme:
        if catch_play(situation, position, player):
            list_position.append(position)
    return list_position


def extremity_pos(situation):
    """
    Get the extremity position of the situation

    :param situation: a game situation
    :type situation: list of list
    :return: the extremity position
    :rtype: list of tuple
    """
    position_list = []
    for x_list in situation:
        for cell in x_list:
            if get_cell_color(cell) is None:
                pass
            else:
                position_list = position_list + available_neighbors(situation, cell)
    return list(set(position_list))


def available_neighbors(situation, cell):
    """
    Get a position list of available neighbor of cell

    :param situation: a situation
    :type situation: list of list
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
        if not is_in_grid(neighbor) or get_color(situation, x, y) is not None:
            pass
        else:
            position_list = position_list + [get_position(situation, x, y)]
    return position_list


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
    l_situations = []
    for position in available_position(situation, player):
        copy_situation = copy.deepcopy(situation)
        set_color(copy_situation, get_pos_x(position), get_pos_y(position), Player.get_color(player))
        reverse_pawn(copy_situation, (get_pos_x(position), get_pos_y(position)), player)
        l_situations.append(copy_situation)

    return l_situations


def displaySituation(situation):
    """
    displays the situation

    :param situation: the situation to display
    :type situation: a game situation
    """
    for i in range(8):
        print("   --- --- --- --- --- --- --- --- ")
        print(7 - i, '|{:^3}|{:^3}|{:^3}|{:^3}|{:^3}|{:^3}|{:^3}|{:^3}|'.format(WorB(situation, 0, 7 - i),
                                                                                WorB(situation, 1, 7 - i),
                                                                                WorB(situation, 2, 7 - i),
                                                                                WorB(situation, 3, 7 - i),
                                                                                WorB(situation, 4, 7 - i),
                                                                                WorB(situation, 5, 7 - i),
                                                                                WorB(situation, 6, 7 - i),
                                                                                WorB(situation, 7, 7 - i)))

    print("   --- --- --- --- --- --- --- --- ")
    print("    0   1   2   3   4   5   6   7  ")


def WorB(situation, x, y):
    """
    Return the color's abbreviations of a cell

    :param situation: the situation of the game
    :type situation: a situation
    :param x: x's coordinate
    :type x: a integer
    :param y: y's coordinate
    :type y: a integer
    """
    if get_color(situation, x, y) is None:
        return ''

    elif get_color(situation, x, y) == 'white':
        return 'W'

    else:
        return 'B'


def humanPlayerPlays(game, player, situation):
    """
    makes the human player plays for given situation in the game

    :param game: the game 
    :type game: game
    :param player: the human player
    :type player: player
    :param situation: the current situation
    :type situation: a game situation
    :returns: *(game situation)* -- the game situation reached after the human player play
    """
    coord = input("Where would you play? x, y ")

    try:
        x, y = coord.split(',')

        if not get_color(situation, int(x), int(y)) is None:
            print("Cell already used")
            situation = humanPlayerPlays(game, player, situation)
        elif not catch_play(situation, (int(x), int(y)), player):
            print("Cell is not a catch play")
            situation = humanPlayerPlays(game, player, situation)
        else:
            set_color(situation, int(x), int(y), Player.get_color(player))
            reverse_pawn(situation, (int(x), int(y)), player)
            return situation

    except KeyboardInterrupt:
        raise KeyboardInterrupt

    except Exception:
        print("input must be 2 separated with a coma x,y . (x = width , y = height) and values must be in [0,7]")
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
    dic_pts = {(0, 0): 2, (0, 1): 0.75, (0, 2): 0.75, (0, 3): 0.75, (0, 4): 0.75, (0, 5): 0.75, (0, 6): 0.75, (0, 7): 2,
               (1, 0): 0.75, (1, 1): 0, (1, 2): 0, (1, 3): 0, (1, 4): 0, (1, 5): 0, (1, 6): 0, (1, 7): 0.75,
               (2, 0): 0.75, (2, 1): 0, (2, 2): 0, (2, 3): 0, (2, 4): 0, (2, 5): 0, (2, 6): 0, (2, 7): 0.75,
               (3, 0): 0.75, (3, 1): 0, (3, 2): 0, (3, 3): 0, (3, 4): 0, (3, 5): 0, (3, 6): 0, (3, 7): 0.75,
               (4, 0): 0.75, (4, 1): 0, (4, 2): 0, (4, 3): 0, (4, 4): 0, (4, 5): 0, (4, 6): 0, (4, 7): 0.75,
               (5, 0): 0.75, (5, 1): 0, (5, 2): 0, (5, 3): 0, (5, 4): 0, (5, 5): 0, (5, 6): 0, (5, 7): 0.75,
               (6, 0): 0.75, (6, 1): 0, (6, 2): 0, (6, 3): 0, (6, 4): 0, (6, 5): 0, (6, 6): 0, (6, 7): 0.75,
               (7, 0): 2, (7, 1): 0.75, (7, 2): 0.75, (7, 3): 0.75, (7, 4): 0.75, (7, 5): 0.75, (7, 6): 0.75, (7, 7): 2,
               }

    for x_list in situation:

        for cell in x_list:

            if get_color(situation, get_cell_x(cell), get_cell_y(cell)) == Player.get_color(player):
                cells_pts += dic_pts[get_position(situation, get_cell_x(cell), get_cell_y(cell))]

    if isFinished(situation):
        return 5 * cells_pts * coef(player)

    else:
        return 1 * cells_pts * coef(player)

def coef_lines(situation, player):
    lines=[[(0,0)],
           [(0,7)],
           [(7,7)],
           [(7,0)],
           [(1,0), (0,1)],
           [(0,6), (1,7)],
           [(7,6), (6,7)],
           [(6,0), (7,1)],
           ]
    for diag in lines:
           for position in diag:
               if get_color(situation, position[0], position[1]):
                   

def reverse_pawn(situation, position, player):
    """
    Reverse the pawn of a catch play

    :param situation: a game situation
    :type situation: a situation
    :param position: a game position
    :type position: a tuple
    :param player: a game player
    :type player: a player
    :return: None
    :Side effect: reverse the color of the pawns catch
    """
    x = get_pos_x(position)
    y = get_pos_y(position)
    neighbors = [(x + 1, y), (x + 1, y + 1), (x + 1, y - 1), (x, y + 1), (x, y - 1), (x - 1, y - 1), (x - 1, y),
                 (x - 1, y + 1)]

    for neighbor in neighbors:
        x_neigh = get_pos_x(neighbor)
        y_neigh = get_pos_y(neighbor)
        delta_x = x_neigh - x
        delta_y = y_neigh - y
        list_pawn = [(x_neigh, y_neigh)]
        while is_in_grid((x_neigh, y_neigh)) and get_color(situation, x_neigh, y_neigh) != Player.get_color(
                player) and get_color(situation, x_neigh, y_neigh) is not None:
            x_neigh += delta_x
            y_neigh += delta_y
            list_pawn.append((x_neigh, y_neigh))
            if is_in_grid((x_neigh, y_neigh)):
                if get_color(situation, x_neigh, y_neigh) == Player.get_color(player):
                    list_pawn.pop()
                    for pos in list_pawn:
                        set_color(situation, get_pos_x(pos), get_pos_y(pos), Player.get_color(player))


# Predicates
def is_in_grid(position):
    """"
    Return True if the position is in the grid

    :param position: a cell position
    :type position: a tuple
    :return: *(Boolean)* -- True if position is in grid
    """
    if 0 <= get_pos_x(position) <= 7 and 0 <= get_pos_y(position) <= 7:
        return True
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
    :returns: (boolean) -- True if player can play in situation
    """
    for position in extremity_pos(situation):
        if catch_play(situation, position, player):
            return True
    return False
