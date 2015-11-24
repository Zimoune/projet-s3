import tictactoe as Tictactoe

def tictactoeEval(situation, player):
    pass

def TictactoeCoef(player):
    if player == Tictactoe.get_player1(Tictactoe.game):
        return -1
    else:
        return 1

def min_max1(situation , player):
    if Tictactoe.isFinished(situation):
        return (evalu(situation , player)*coef(player) , situation)
    else:
        nextSituations = Tictactoe.nextSituations(Tictactoe.game , situation , player)
        if coef(player) == 1:
            return max(min_max(nextSit, Tictactoe.get_player1(Tictactoe.game)) for nextSit in nextSituations)
        else:
            return min(min_max(nextSit, Tictactoe.get_player1(Tictactoe.game)) for nextSit in nextSituations)
            



