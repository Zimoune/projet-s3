import tictactoe as Game

def min_max1(situation, player):
    if Game.isFinished(situation):
        print(situation)
        score = Game.evalFunction(situation , player)*Game.coef(player)
        return (score , situation)
    else:
        nextSituations = Game.nextSituations(situation, player)
        print(nextSituations)
        if Game.:
            return max([(min_max1(nextSit, Game.get_player1(Game.game))[0], nextSit) for nextSit in nextSituations])
        else:

            return min([(min_max1(nextSit, Game.get_player2(Game.game))[1], nextSit) for nextSit in nextSituations])
            
