from tournament_phase1 import *
from tournament_phase2 import *
from sorters import *
from tournament_repeat import *

def simulator():
    '''
    Runs simulation of tournament and prints out the top 4
    '''
    Stage1_winners, Stage1_losers = phase1Knockout(phase1Generator())
    TopLosers = loserBracketQualification(Stage1_losers)
    Stage2_winners, Stage2_losers = phase2Knockout(Stage1_winners, TopLosers)
    Stage3_winners, Stage3_losers = phaseRepeatKnockout(Stage2_winners)
    Stage4_winners, Stage4_losers = phaseRepeatKnockout(Stage3_winners)
    Stage5_winners, Stage5_losers = phaseRepeatKnockout(Stage4_winners)
    Stage6_winners, Stage6_losers = phaseRepeatKnockout(Stage5_winners)
    Stage7_winners, ThirdPlacePlayoff = phaseRepeatKnockout(Stage6_winners)
    ThirdPlace, FourthPlace = phaseRepeatKnockout(ThirdPlacePlayoff)
    Winner, SecondPlace = phaseRepeatKnockout(Stage7_winners)

    print(f"Winners: {Winner[0]} \nSecond: {SecondPlace[0]} \nThird: {ThirdPlace[0]} \nFourth: {FourthPlace[0]}")

simulator()




