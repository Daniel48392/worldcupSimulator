def winnerCalculator(matchStats):
    '''
    Calculates odds of a winner
    TODO random number generator to make it truly random
    :param matchStats:
    :return:
    '''
    odds = 1 / ( 1 + (10 ** ( (float(matchStats[1])-float(matchStats[0]))/400)) )
    if odds >= 0.5:
        return 0
    else:
        return 1
