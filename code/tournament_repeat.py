from sorters import phaseGenerator
from pathlib import Path
import csv
from winner_calculator import winnerCalculator

BASE_DIR = Path(__file__).parent.parent
path = BASE_DIR / "data" / "fifa_mens_rank.csv"



def phaseRepeatKnockout(winners):
    '''
    Organises the last phases matches into winners and losers
    :param winners: winners of the last round
    :return: winners and losers of the round
    '''



    round_winners = []  # winners
    round_losers = []  # losers



    for match in phaseGenerator(winners):
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
        round_winners.append(match[winLose][0])  # Winner gets append to winners array
        match.pop(winLose)  # Winner gets removed from match array
        round_losers.append(match[0][0])  # Remaining team in match array gets added to loser array


    return round_winners, round_losers