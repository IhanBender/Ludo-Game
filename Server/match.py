from state import State
import coordinates as c
import random

RED = 0
GREEN = 1
BLUE = 2
YELLOW = 3

class Match():
    def __init__(self, players, identifier):
        self.identifier = identifier
        self.players = players
        self.state = State(
            redInitials = c.redInitials,
            greenInitials = c.greenInitials,
            blueInitials = c.blueInitials,
            yellowInitials = c.yellowInitials
        )
        # First player
        self.currentTurn = random.randint(0,3)
        # 'dice' or 'piece'
        self.currentPlay = 'dice'

    def nextPlayer(self):
        if self.currentTurn == 3:
            self.currentTurn = 0
        else:
            self.currentTurn += 1


    def alternatePlay(self):
        if self.currentPlay == 'dice':
            self.currentPlay = 'piece'
        else:
            self.currentPlay = 'dice'