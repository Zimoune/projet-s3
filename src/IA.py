

def min_max1(situation , player):
    if Tictactoe.isFinished(situation):
        return (tictactoeEval(situation , player)*coef(player) , situation)
    else:
        nextSituations = Tictactoe.nextSituations(game , situation , player)
        if coef(player) == 1:
            return max(min_max(nextSit, Tictactoe.get_player1(Tictactoe.game)) for nextSit in nextSituations)
        else:
            return min(min_max(nextSit, Tictactoe.get_player2(Tictactoe.game)) for nextSit in nextSituations)
            



