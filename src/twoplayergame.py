#!/usr/bin/python3
# -*- coding: utf-8 -*-

import player as Player
import minmax as IA

currentPlayer = None


def play(game_name, difficulty):
    """
    Main game function process

    :param game_name: the game's name
    :type game_name: str
    :return: None
    """
    global currentPlayer
    global mod

    if game_name == "nim":
        import nim_game as Game
        mod = __import__("nim_game")

    elif game_name == "othello":
        import othello as Game
        mod = __import__("othello")

    else:
        import tictactoe as Game
        mod = __import__("tictactoe")
    ask_players_names(Game.color)
    situation = Game.initSituation(game_name)

    while not Game.isFinished(situation):

        if currentPlayer is None:
            currentPlayer = Game.get_player1(Game.game)
        else:
            currentPlayer = swap_player_turn(currentPlayer, mod)

        if not Game.playerCanPlay(Game.game, situation, currentPlayer):
            print(currentPlayer, " can't play")
            currentPlayer = swap_player_turn(currentPlayer, Game)
        Game.displaySituation(situation)
        print(Player.get_name(currentPlayer), " turn")

        if Player.get_name(currentPlayer) == "Minmax":
            situation = IA.min_max(game_name, Game.game, situation, currentPlayer, difficulty)
        else:
            situation = Game.humanPlayerPlays(Game.game, currentPlayer, situation)
        Game.game['nb_plays'] += 1
    winner = Game.getWinner(Game.game, situation, currentPlayer)

    if winner is None:
        Game.displaySituation(situation)
        print("equality !")

    else:
        Game.displaySituation(situation)
        print(Player.get_name(winner), "won")


def swap_player_turn(player, game):
    """
    swap players turn

    :param player: the current player
    :type player: a player
    :param game: the game
    :type game: a game
    :return:
    """
    if player == game.get_player1(game.game):
        return game.get_player2(game.game)
    else:
        return game.get_player1(game.game)


def ask_players_names(color):
    """
    Ask players's names

    :param color: colors
    :type color: color list
    :return:
    """
    try:
        mod.set_player1(Player.create(input("name player 1: "), color[0]))
        mod.set_player2(Player.create(input("name player 2: "), color[1]))

    except KeyboardInterrupt:
        raise KeyboardInterrupt

    except:
        ask_players_names(color)

def play_graphique(game_name, difficulty):
    if game_name == "tictactoe":
        import tictactoeGraph as Game
        mod = __import__("nim_game")

    elif game_name == "othello":
        import othello as Game
        mod = __import__("othello")

    Game.play()

if __name__ == '__main__':
    game_name = "tictactoe"
    play_graphique(game_name, 3)
