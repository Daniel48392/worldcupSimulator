import csv
from pathlib import Path
from random import randint
from winner_calculator import winnerCalculator

BASE_DIR = Path(__file__).parent.parent
path = BASE_DIR / "data" / "fifa_mens_rank.csv"

def phase1Generator():
    '''
    Generates the games played in phase 1 of the tournament
    :return: games for phase 1 of the tournament
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
    :param phase1: games for phase 1 of the tournament
    :return: winner, loser - winners and losers of the first stage
    '''

    winners = [] # winners
    losers = [] # losers

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

            winLose = winnerCalculator(matchStats) # Determines which team will win
            winners.append(match[winLose][0]) # Winner gets append to winners array
            match.pop(winLose) # Winner gets removed from match array
            losers.append(match[0][0]) # Remaining team in match array gets added to loser array

    return winners, losers



