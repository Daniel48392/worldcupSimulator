import random

def winnerCalculator(matchStats):
    '''
    Calculates odds of a winner
    The odds number refers to the chances of the matchStats[0] team winning
    :param matchStats: stats of each team facing each other
    :return: the winner of the match
    '''
    randomNum = random.randint(1, 100)/100 # Random number generated
    odds = 1 / ( 1 + (10 ** ( (float(matchStats[1])-float(matchStats[0]))/400)) )
    if randomNum <= odds: # if the random number is less than or equal to matchStats[0] teams chance of winning return them
        return 0 # Selects first team in matchStats
    else: # return matchStats[1] if the randomNum is out of range of matchStats[0] chances of winning
        return 1 # Selects second team in matchStats
