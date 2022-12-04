#%%
from AoC import AoC

session = AoC()

#%% Load input
with open('inputs/input2.txt') as input_file:
    strategy_guide = [] # initialise strategy guide as list of tuples
    for line in input_file:
        choices = tuple(line.strip().split(' ')) # remove newline character and splits line
        strategy_guide.append(choices)


#%% Part 1
# Assuming X, Y, Z encode for rock paper scissors, calculate score of strat
class RpsRound:
    def __init__(self, choices):
        self.elfChoice = self.choiceEncoder(choices[0])
        self.playerChoice = self.choiceEncoder(choices[1])

    def choiceEncoder(self, choice):
        '''Returns the choice as 0, 1, or 2 for Rock, Paper, Scissors respectively'''
        intChoice = 0

        if choice in ['A', 'B', 'C']: 
            intChoice = ord(choice) - 65
        elif choice in ['X', 'Y', 'Z']: 
            intChoice = ord(choice) - 88
        
        return intChoice

    def rpsReferee(self):
        '''Decides if the player wins or not'''
        # Keys are the index of players choice from [Rock, Paper, Scissors] 
        # Values are score outcomes given index of elf's choice from same list.
        rpsLogic = {
            #   R, P, S
            0: [3, 0, 6], # R
            1: [6, 3, 0], # P
            2: [0, 6, 3]  # S
        }

        return rpsLogic[self.playerChoice][self.elfChoice]

    def rpsScore(self):
        score = 0

        score += self.playerChoice + 1 # score based on own choice
        score += self.rpsReferee() # score based on outcome

        return score


#%% Part 2

# Knowing that X, Y, Z encode for Lose, draw, win; calculate total score of strat.
def partTwoModifications():
    '''Makes adjustments to RpsRound class necessary for part 2'''

    def newInit(self, choices):
        self.elfChoice = self.choiceEncoder(choices[0])
        self.Outcome = choices[1]
        self.playerChoice = self.playerChoiceDecider() # Player choice now decided by other attributes

    def newChoiceEncoder(self, choice):
        '''Returns the choice as 0, 1, or 2 for Rock, Paper, Scissors respectively'''
        intChoice = 0
        if choice in ['A', 'B', 'C']: 
            intChoice = ord(choice) - 65
        return intChoice

    def playerChoiceDecider(self):
        '''outputs required player choice to meet desired outcome given elf choice.'''
        # Key is desired outcome, value is list of player moves given index of elf choice on [Rock, Paper, Scissors]
        choiceLogic = {
            #Elf:R, P, S
            'X':[2, 0, 1], # Lose
            'Y':[0, 1, 2], # Draw
            'Z':[1, 2, 0]  # Win
        }
        return choiceLogic[self.Outcome][self.elfChoice]
    
    RpsRound.choiceEncoder = newChoiceEncoder
    RpsRound.__init__ = newInit
    RpsRound.playerChoiceDecider = playerChoiceDecider


def getScore():
    """Calculates score from """
    scores = [RpsRound(choices).rpsScore() for choices in strategy_guide]
    return sum(scores)


if __name__ == '__main__':
    print(f'Part 1 total: {getScore()}')
    
    partTwoModifications()
    print(f'Part 2 total: {getScore()}')