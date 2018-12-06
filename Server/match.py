from state import State
from coordinates import Coordinates
import random

RED = 0
GREEN = 1
BLUE = 2
YELLOW = 3

class Match():
    def __init__(self, players, identifier):
        self.coords = Coordinates()
        self.identifier = identifier
        self.players = players
        self.state = State(
            redInitials = self.coords.redInitials,
            greenInitials = self.coords.greenInitials,
            blueInitials = self.coords.blueInitials,
            yellowInitials = self.coords.yellowInitials,
            turn = random.randint(0,len(self.players))
        )
        # 'dice' or 'piece'
        self.currentPlay = 'dice'

    def nextPlayer(self):
        self.state.nextPlayer(len(self.players))

    def alternatePlay(self):
        if self.currentPlay == 'dice':
            self.currentPlay = 'piece'
        else:
            self.currentPlay = 'dice'

    # String to send as a message
    def toString(self):
        # Players first
        description = '/PLAYERS'
        for player in self.players:
            description += ' ' + player.username
        description += ' ' + '\PLAYERS'

        # Current turn
        description += ' ' + str(self.state.currentTurn)
        # Current play
        self.currentPlay

        # Positions:
        #red
        for i in range(0,4):
            description += ' ' + str(self.state.redPositions[i][0])     # x
            description += ' ' + str(self.state.redPositions[i][1])     # y
        #green
        for i in range(0,4):
            description += ' ' + str(self.state.greenPositions[i][0])     # x
            description += ' ' + str(self.state.greenPositions[i][1])     # y
        #blue
        for i in range(0,4):
                    description += ' ' + str(self.state.bluePositions[i][0])     # x
                    description += ' ' + str(self.state.bluePositions[i][1])     # y
        #yellow
        for i in range(0,4):
                    description += ' ' + str(self.state.yellowPositions[i][0])     # x
                    description += ' ' + str(self.state.yellowPositions[i][1])     # y

        return description
