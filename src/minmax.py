def min_max(game_name, game, situation, player, depth=-1):
    """
    Return the best situation for a player thanks to the minimax algorithm
    Minmax is a decision rule used in decision theory, game theory, statistics and philosophy for minimizing the possible loss for a worst case (maximum loss) scenario.
    
    :param game: The game
    :type game: game
    :param situation: The current situation
    :type situation: situation:
    :param players: The player list
    :type players: list<players>
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
    :param players: The player list
    :type players: list<players>
    :param depth: The recursivity depth for the minimax algorithm (Upper is the depth, better is the decision)
                  * If depth = -1 , the depth will be based on the difficulty score
    :type depth: int
    :return: A tuple with two elements: the first is the best situation score, the second is the best situation
    :rtype: tuple<int, situation>
    """
    if game_name == "nim":
        import nim_game as Game
        mod = __import__("nim_game")

    elif game_name == "othello":
        import othello as Game
        mod = __import__("othello")

    else:
        import tictactoe as Game
        mod = __import__("tictactoe")
    
    if(Game.isFinished(situation) or depth == 0):
        score = Game.evalFunction(situation, player)
        print(score)
        return (score, situation)
    else:
        currentPlayer = player
        nextSituations = Game.nextSituations(situation, currentPlayer)
         
        if(Game.coef(player) == 1):
            return max([(__min_max(game_name, game, nextSit, Game.get_inv_player(player), depth-1)[0], nextSit) for nextSit in nextSituations])
        else:
            return min([(__min_max(game_name, game, nextSit, Game.get_inv_player(player), depth-1)[0], nextSit) for nextSit in nextSituations])
