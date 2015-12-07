

def min_max1(game_name, situation, player):

    if game_name == "nim":
        import nim_game as Game
        mod = __import__("nim_game")

    elif game_name == "othello":
        import othello as Game
        mod = __import__("othello")

    else:
        import tictactoe as Game
        mod = __import__("tictactoe")

    if Game.isFinished(situation):
        score = Game.evalFunction(situation , player)*Game.coef(player)
        return score, situation
    else:
        nextSituations = Game.nextSituations(situation, player)
        if Game.coef(player) == 1:
            return max([(min_max1(game_name, nextSit, Game.get_inv_player(player))[1], nextSit) for nextSit in nextSituations])
        else:
            return min([(min_max1(game_name, nextSit, Game.get_inv_player(player))[1], nextSit) for nextSit in nextSituations])


def min_max2(situation, player, depht):
    game_name = "nim"

    if game_name == "nim":
        import nim_game as Game
        mod = __import__("nim_game")

    elif game_name == "othello":
        import othello as Game
        mod = __import__("othello")

    else:
        import tictactoe as Game
        mod = __import__("tictactoe")
    if Game.isFinished(situation) or depht == 0:
        score = Game.evalFunction(situation, player)*Game.coef(player)
        return score, situation
    else:
        nextSituations = Game.nextSituations(situation, player)
        if Game.coef(player) == 1:
            return max([(min_max1(nextSit, Game.get_inv_player(player), depht -1)[1], nextSit) for nextSit in nextSituations])
        else:

            return min([(min_max1(nextSit, Game.get_inv_player(player))[1], nextSit) for nextSit in nextSituations])