from random import randint
from pathlib import Path
import csv

BASE_DIR = Path(__file__).parent.parent
path = BASE_DIR / "data" / "fifa_mens_rank.csv"

def phaseGenerator(phase):
    '''
    Takes in list of teams and organises them into matches
    :param phase: array of teams
    :return: array of matches
    '''
    teams = []
    while phase!=[]:
        team1 = [phase[randint(0, len(phase)-1)]]
        phase.remove(team1[0])
        team2 = [phase[randint(0, len(phase)-1)]]
        phase.remove(team2[0])
        match = [team1, team2]
        teams.append(match)

    return teams



def quick_sort(rank):
    '''
    Sorts loser teams by their fifa ranking
    :param rank: fifa rankings and their teams
    :return: sorted rankings
    '''
    if len(rank)<=1:
        return rank
    pivot = rank[0]
    left = [x for x in rank[1:] if x[0] < pivot[0]]
    right = [x for x in rank[1:] if x[0] >= pivot[0]]
    return quick_sort(left) + [pivot] + quick_sort(right)



def loserBracketQualification(losers):  # Need to make a 128 team knockout stage
    '''
    Top 23 teams with the highest fifa ranking progress to phase2
    :param losers: losers of phase1
    :return: top 23 teams in losers bracket
    '''
    rank = [] # 2D array of integer fifa ranking and string name in an array in the array
    for loser in losers:
        with open(path, "r", newline="") as file:  # Reads file
            reader = csv.reader(file)
            next(reader)  # Skip the header
            for row in reader:  # Goes through data file
                if loser == row[3]:
                    rank.append([int(row[2]), loser]) # Adds fifa ranking and team name to the rank array


    return(quick_sort(rank)[0:23]) # returns the top 23 teams