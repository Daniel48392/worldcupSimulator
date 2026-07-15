import csv
from pathlib import Path
from random import randint

BASE_DIR = Path(__file__).parent.parent
path = BASE_DIR / "data" / "fifa_mens_rank.csv"


def winnerCalculator(matchStats):
    '''
    Calculates odds of a winner
    TODO random number generator to make it truly random
    :param matchStats:
    :return:
    '''
    odds = 1 / ( 1 + (10 ** ( (float(matchStats[1])-float(matchStats[0]))/400)) )
    print(odds)
    if odds >= 0.5:
        return 0
    else:
        return 1

def phase1Generator():
    '''
    Generates the games played in phase 1 of the tournament
    '''
    phase1 = []

    #Collects team names
    teams = []
    with open(path, "r", newline="") as file:
        reader = csv.reader(file)
        next(reader)  # Skip the header
        for row in reader:
            teams.append(row[3])  # First column

    #Randomly Organises Phase 1 matches
    while teams!=[]:
        team1 = [teams[randint(0, len(teams)-1)]]
        teams.remove(team1[0])
        team2 = [teams[randint(0, len(teams)-1)]]
        teams.remove(team2[0])
        match = [team1, team2]
        phase1.append(match)

    return phase1


def phase1Knockout(phase1):
    '''
    Organises the phase 1 matches into winners and losers

    :param phase1:
    :return:
    '''

    winners = [] # winners
    losers = [] # losers

    testcount = 0  # test #########################

    for match in phase1:
        matchStats = [] # Fifa world ranking points for each team

        with open(path, "r", newline="") as file: # Reads file
            reader = csv.reader(file)
            next(reader)  # Skip the header
            for row in reader:  # Goes through data file
                if row[3] == match[0][0]: # Checks if the current row is the current match team
                    matchStats.insert(0, row[5]) # Adds first teams statistic to first index in the array
                if row[3] == match[1][0]: # Checks if the current row is the current match team
                    matchStats.insert(1,row[5]) # Adds second teams statistic to second index in the array

            winLose = winnerCalculator(matchStats) # Determines which team will in
            print(match) ##### test ##########
            winners.append(match[winLose][0]) # Winner gets append to winners array
            match.pop(winLose) # Winner gets removed from match array
            losers.append(match[0][0]) # Remaining team in match array gets added to loser array



            print(f'winner: {winners[testcount]}, loser: {losers[testcount]}')   ##### test ##########
            testcount += 1   ##### test ##########

def loserBracketQualification(losers): # Need to make a 128 team knockout stage
    '''
    Top 23 teams with the highest fifa ranking progress to phase2
    :param losers:
    :return: top 23 teams in losers bracket
    '''

    ## TODO sort losers bracket by fifa point ranking, then return top 23 losers bracket teams


def phase2Knockout(winners, topLosers):
    '''
    Organises the phase 2 matches into winners and losers
    :param winners:
    :param topLosers:
    :return:
    '''

    ## TODO add winners and losers to one list and repeat the phase1 process repeat until final




phase1Knockout(phase1Generator())