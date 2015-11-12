#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
:mod:`joueur` module

:author: `Simon Le Pallac & Lefebvre Ryan`

:data: November, 2015

Module for player representation
A Player
"""

def create(name, color):
    """

    :param name: name of the player
    :type name: str

    :return: a new record for this player
    :rtype: player
    """
    assert type(name) == str
    assert type(color) == str
    return {
        'name' : name,
        'color' : color
    }

def get_name(player):
    """

    :param player: a player
    :type player: player

    :return: name of player
    :rtype: str
    """
    return player['name']

def set_name(name, player):
    """
    set a new name to player

    :param name: the new name
    :type name: str
    :param player: the player
    :type player: player

    :return: None
    """
    player['name'] = name

def get_color(player):
    """

    :param player: a player
    :type player: player

    :return: color of player
    :rtype: str
    """
    return player['color']

def set_color(color, player):
    """
    set a new color to player

    :param color: the new color
    :type color: str
    :param player: the player
    :type player: player
    :return: None
    """
    player['color'] = color
