from tournament_phase1 import *
from tournament_phase2 import *
from sorters import *

def simulator():
    Stage1_winners, Stage1_losers = phase1Knockout(phase1Generator())
    TopLosers = loserBracketQualification(Stage1_losers)
    Stage2_winners, Stage2_losers = phase2Knockout(Stage1_winners, TopLosers)



simulator()