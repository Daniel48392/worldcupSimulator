from sorters import phaseGenerator
from pathlib import Path
import csv
from winner_calculator import winnerCalculator

BASE_DIR = Path(__file__).parent.parent
path = BASE_DIR / "data" / "fifa_mens_rank.csv"

def phase2Knockout(stage1_winners, topLosers):
    '''
    Organises the phase 2 matches into winners and losers
    :param winners:
    :param topLosers:
    :return:
    '''
    phase2 = []
    for topLoser in topLosers:
        phase2.append(topLoser[1])
    phase2 += stage1_winners

    winners = []  # winners
    losers = []  # losers



    for match in phaseGenerator(phase2):
        matchStats = []  # Fifa world ranking points for each remaining team
        with open(path, "r", newline="") as file:  # Reads file
            reader = csv.reader(file)
            next(reader)  # Skip the header
            for row in reader:  # Goes through data file
                if row[3] == match[0][0]:  # Checks if the current row is the current match team
                    matchStats.insert(0, row[5])  # Adds first teams statistic to first index in the array
                if row[3] == match[1][0]:  # Checks if the current row is the current match team
                    matchStats.insert(1, row[5])  # Adds second teams statistic to second index in the array
        winLose = winnerCalculator(matchStats)  # Determines which team will win
        winners.append(match[winLose][0])  # Winner gets append to winners array
        match.pop(winLose)  # Winner gets removed from match array
        losers.append(match[0][0])  # Remaining team in match array gets added to loser array


    return winners, losers
    ## TODO add winners and losers to one list and repeat the phase1 process repeat until final






