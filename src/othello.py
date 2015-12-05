# -*- coding: utf-8 -*-

import player as Player

import othelloGame as Game

#### default_game ####

game = Game.make_game()
color = ["white","black"]

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
    set_color(get_grid(game), 4, 4 , 'white')
    set_color(get_grid(game), 5, 5 , 'white')
    set_color(get_grid(game), 4, 5 , 'black')
    set_color(get_grid(game), 5, 4 , 'black')

    return get_grid(game)


def isFinished(situation):
    """
    tells if the game is finished when in given situation

    :param situation: the tested situation
    :type situation: a game situation
    :returns: *(boolean)* -- True if the given situation ends the game
    """
    raise NotImplementedError( "isFinished must be defined as a function to test end of game" )


def catch_play(position, player):
#Non testé il me semble
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
    neighbors = [(x+1,y), (x+1,y+1), (x+1,y-1), (x,y+1), (x,y-1), (x-1,y-1), (x-1,y),(x-1, y+1)]

    for neighbor in neighbors:
        x_neigh = neighbor[0]
        y_neigh = neighbor[1]
        delta_x = x_neigh - x
        delta_y = y_neigh - y
        print((delta_x, delta_y))

        if get_color(game['grid'], x_neigh, y_neigh) == is_opposite_pawn(position):
            print(y_neigh + delta_y)
            print(game['grid'][x_neigh + delta_x][y_neigh + delta_y]['color'])

            while game['grid'][x_neigh + delta_x][y_neigh + delta_y]['color'] == is_opposite_pawn(position):
                print("test")
                x_neigh += delta_x
                y_neigh += delta_y
                position = (x_neigh, y_neigh)

                if get_color(game['grid'], x_neigh + delta_x, y_neigh + delta_y ) == is_opposite_pawn(position):
                    return True

    return False

def is_opposite_pawn(position):
    """
    Get the opposite color of a position cell

    :param position: a position
    :type position: a tuple
    :return: a color
    :rtype: a string
    """
    global game
    color = get_color(get_grid(game), position[0], position[1])
    if color == color[0]:
        return color[1]
    else:
        return color[0]


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
    neighbors = [(x+1,y), (x+1,y+1), (x+1,y-1), (x,y+1), (x,y-1), (x-1,y-1), (x-1,y),(x-1, y+1)]
    for neighbor in neighbors:
        global game
        x = neighbor[0]
        y = neighbor[1]
        grid = get_grid(game)
        if not is_in_grid(neighbor) or get_color(grid, x, y) != None:
            pass
        else:
            position_list = position_list+[get_position(grid, x, y)]
    return position_list


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
    pass


def displaySituation(situation):
    """
    displays the situation

    :param situation: the situation to display
    :type situation: a game situation
    """
    for i in range(8):
        print(" --- --- --- ")
        print('|{:^3}|{:^3}|{:^3}|{:^3}|{:^3}|{:^3}|{:^3}|{:^3}|'.format(WorB(situation, 0, 7-i),WorB(situation, 1, 7-i),WorB(situation, 2, 7-i)WorB(situation, 3, 7-i)
                                                                        ,WorB(situation, 4, 7-i),WorB(situation, 5, 7-i),WorB(situation, 6, 7-i),WorB(situation, 7, 7-i)))

    print(" --- --- --- ")


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

    if get_player_name(player) == "Minmax":
        return 1

    else:
        return 1

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
    :returns: *(boolean)* -- True iff player can play in situation
    """
    for x in range(8):

        for y in range(8):

            if get_grid_color(game, x, y) != get_color(situation, x, y):

                if get_position(situation, x, y) in extremity_pos(situation):

                    if catch_play(get_position(situation, x, y), player):

                        return True

    return False

