#!/usr/bin/python3
# -*- coding: utf-8 -*-


def make_game():
    """
    return a tictactoe game of size 3*3 cells and with two player

    :return: a game
    :rtype: a tuple
    """

    return {"player1": "", "player2": "", "grid": make_grid(), "nb_plays": 0}


def make_grid():
    """
    return a tictactoe grid of size 3*3 cells

    :return: a grid with 3*3 cells
    :rtype: llist of list of cells
    """
    return [[make_cell(x, y) for y in range(3)] for x in range(3)]


def make_cell(x, y):
    """
    return a tictactoe cell

    :param x: x position
    :type x: int
    :param y: y position
    :type y: int
    :return: a cell with his color
    :rtype: a cell
    """
    return {"color": None, "position": (x, y)}
