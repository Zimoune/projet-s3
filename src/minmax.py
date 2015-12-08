#!/usr/bin/python3
# -*- coding: utf-8 -*-

import random as Random


def min_max(game_name, game, situation, player, depth=-1):
    """
    Return the best situation for a player thanks to the minimax algorithm
    Minmax is a decision rule used in decision theory, game theory, statistics and philosophy for minimizing the possible loss for a worst case (maximum loss) scenario.
    
    :param game: The game
    :type game: game
    :param situation: The current situation
    :type situation: situation:
    :param player: The player
    :type player: a player
    :param depth: The recursivity depth for the minimax algorithm (Upper is the depth, better is the decision) (facultative)
    :type depth: int
    :return: The best situation for a player thanks to the minimax algorithm
    :rtype: situation
    """
    return __min_max(game_name, game, situation, player, depth)[1]


def __min_max(game_name, game, situation, player, depth):
    """
    The minimax algorithm.
    
    :param game: The game
    :type game: game
    :param situation: The current situation
    :type situation: situation:
    :param player: The player
    :type player: a player
    :param depth: The recursivity depth for the minimax algorithm (Upper is the depth, better is the decision)
                  * If depth = -1 , the depth will be based on the difficulty score
    :type depth: int
    :return: A tuple with two elements: the first is the best situation score, the second is the best situation
    :rtype: tuple<int, situation>
    """
    if game_name == "nim":
        import nim_game as Game

    elif game_name == "othello":
        import othello as Game

    else:
        import tictactoe as Game

    if Game.isFinished(situation) or depth == 0:
        score = Game.evalFunction(situation, player)
        return score, situation
    else:
        nextSituations = Game.nextSituations(situation, player)

        if Game.coef(player) == 1:
            return max([(__min_max(game_name, game, nextSit, Game.get_inv_player(player), depth - 1)[0], nextSit)
                        for nextSit in nextSituations])
        else:
            return min([(__min_max(game_name, game, nextSit, Game.get_inv_player(player), depth - 1)[0], nextSit)
                        for nextSit in nextSituations])


def min(l):
    """
    Return the situation with the lowest score
    
    :param l: A list of tuple with two elements: the first is the best situation score, the second is the best situation
    :type l: list<tuple<int, situation>>
    :return: The situation with the lowest score
    :rtype: tuple<int, situation>
    """
    the_min = (2000000000, None)

    for couple in l:
        if the_min[0] > couple[0] or (the_min[0] > couple[0] and Random.randint(0, 101) % 2 == 0):
            the_min = couple

    return the_min


def max(l):
    """
    Return the situation with the best score
    
    :param l: A list of tuple with two elements: the first is the best situation score, the second is the best situation
    :type l: list<tuple<int, situation>>
    :return: The situation with the lowest score
    :rtype: tuple<int, situation>
    """
    the_max = (-2000000000, None)

    for couple in l:
        if the_max[0] < couple[0] or (the_max[0] < couple[0] and Random.randint(0, 101) % 2 == 0):
            the_max = couple

    return the_max
