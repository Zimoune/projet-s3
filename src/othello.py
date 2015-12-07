# -*- coding: utf-8 -*-

import player as Player
import copy
import othelloGame as Game
import copy

#### default_game ####
game = Game.make_game()

color = ["white", "black"]


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


def get_player_name(player):
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


def get_position_cell(cell):
    """
    Get the position of cell

    :param cell: cell of game
    :type cell: a cell
    :return: a position cell
    :rtype: a tuple
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
        for position in extremity_pos(get_grid(game)):
            if catch_play(position, player):
                return False
    return True


def catch_play(position, player):
    """
    Get True if a position is a catch play for a player

    :param position: a position
    :type position: a tuple
    :param player: a game player
    :type player: a player
    :return: *(Boolean)* --True if the position is a catch play
    """
    global game
    x = position[0]
    y = position[1]
    neighbors = [(x + 1, y), (x + 1, y + 1), (x + 1, y - 1), (x, y + 1), (x, y - 1), (x - 1, y - 1), (x - 1, y),
                 (x - 1, y + 1)]

    for neighbor in neighbors:
        x_neigh = neighbor[0]
        y_neigh = neighbor[1]
        delta_x = x_neigh - x
        delta_y = y_neigh - y
        while is_in_grid((x_neigh, y_neigh)) and get_color(game['grid'], x_neigh, y_neigh) != player['color'] \
                and get_color(game['grid'], x_neigh, y_neigh) != None:
            x_neigh += delta_x
            y_neigh += delta_y
            if is_in_grid((x_neigh, y_neigh)):
                if get_color(game['grid'], x_neigh, y_neigh) == player['color']:
                    return True
    return False


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
            if cell['color'] == None:
                pass
            else:
                position_list = position_list + available_neighbors(cell)
    return list(set(position_list))


def available_neighbors(cell):
    """
    Get a position list of available neighbor of cell

    :param cell: cell of game
    :type cell: a cell
    :return: a list of available neighbors
    :rtype: a list
    """
    position_list = []
    x = get_position_cell(cell)[0]
    y = get_position_cell(cell)[1]
    neighbors = [(x + 1, y), (x + 1, y + 1), (x + 1, y - 1), (x, y + 1), (x, y - 1), (x - 1, y - 1), (x - 1, y),
                 (x - 1, y + 1)]
    for neighbor in neighbors:
        global game
        x = neighbor[0]
        y = neighbor[1]
        grid = get_grid(game)
        if not is_in_grid(neighbor) or get_color(grid, x, y) != None:
            pass
        else:
            position_list = position_list + [get_position(grid, x, y)]
    return position_list


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
            for position in extremity_pos(situation):
                if catch_play(position, player):
                    set_color(copy_situation, x_cell, y_cell, player['color'])
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
        print(7-i,'|{:^3}|{:^3}|{:^3}|{:^3}|{:^3}|{:^3}|{:^3}|{:^3}|'.format(WorB(situation, 0, 7 - i),
                                                                         WorB(situation, 1, 7 - i),
                                                                         WorB(situation, 2, 7 - i),
                                                                         WorB(situation, 3, 7 - i)
                                                                         , WorB(situation, 4, 7 - i),
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
    if get_color(situation, x, y) == None:
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
    :returns: *(game situtation)* -- the game situation reached afte the human player play
    """
    coord = input("Where would you play? x, y ")

    try:
        x, y = coord.split(',')

        if not get_color(situation, int(x), int(y)) == None:
            print("Case already used")
            situation = humanPlayerPlays(game, player, situation)
        elif not catch_play((int(x), int(y)), player):
            print("cell is not a catch play")
            situation = humanPlayerPlays(game, player, situation)
        else:
            set_color(situation, int(x), int(y), Player.get_color(player))
            reverse_pawn((int(x), int(y)), player)
            return situation

    except KeyboardInterrupt:
        raise KeyboardInterrupt

    except Exception:
        print("input must be 2 seperated with a coma x,y . (x = width , y = height) and values must be in [0,7]")
        humanPlayerPlays(game, player, situation)
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

            if get_color(situation, cell['position'][0], cell['position'][1]) == player['color']:
                cells_pts += dic_pts[get_position(situation, cell['position'][0], cell['position'][1])]

    if isFinished(situation) == True:
        return 5 * cells_pts * coef(player)

    else:
        return 1 * cells_pts * coef(player)


def reverse_pawn(position, player):
    global game
    x = position[0]
    y = position[1]
    neighbors = [(x + 1, y), (x + 1, y + 1), (x + 1, y - 1), (x, y + 1), (x, y - 1), (x - 1, y - 1), (x - 1, y),
                 (x - 1, y + 1)]

    for neighbor in neighbors:
        x_neigh = neighbor[0]
        y_neigh = neighbor[1]
        delta_x = x_neigh - x
        delta_y = y_neigh - y
        list_pawn = []
        list_pawn.append((x_neigh, y_neigh))
        while is_in_grid((x_neigh, y_neigh)) and get_color(game['grid'], x_neigh, y_neigh) != player['color'] \
                and get_color(game['grid'], x_neigh, y_neigh) != None:
            x_neigh += delta_x
            y_neigh += delta_y
            list_pawn.append((x_neigh, y_neigh))
            if is_in_grid((x_neigh, y_neigh)):
                if get_color(game['grid'], x_neigh, y_neigh) == player['color']:
                    list_pawn.pop()
                    for pos in list_pawn:
                        set_color(get_grid(game), pos[0], pos[1], Player.get_color(player))


##### Predicates #####



def is_in_grid(position):
    """"
    Return True if the position is in the grid

    :param position: a cell position
    :type postion: a tuple
    :return: *(Boolean)* -- True if position is in grid
    """
    if position[0] >= 0 and position[0] < 8 and position[1] >= 0 and position[1] < 8:
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
    :returns: (boolean) -- True iff player can play in situation
    """
    for position in extremity_pos(situation):
        if catch_play(position, player):
            return True
    return False
