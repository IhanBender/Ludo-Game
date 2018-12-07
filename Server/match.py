from state import State
from coordinates import Coordinates
import random
import json

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
            turn = random.randint(1,len(self.players))
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
        players = {}
        for player in self.players:
            players[player.username] = len(players) + 1

        # Current turn
        currentTurn = str(self.state.currentTurn)
        # Current play
        self.currentPlay

        # Positions:
        #red
        red = []
        green = []
        yellow = []
        blue = []
        for i in range(0,4):
            red.append((str(self.state.redPositions[i][0]), str(self.state.redPositions[i][1])))
            green.append((str(self.state.greenPositions[i][0]), str(self.state.greenPositions[i][1])))
            blue.append((str(self.state.bluePositions[i][0]), str(self.state.bluePositions[i][1])))
            yellow.append((str(self.state.yellowPositions[i][0]), str(self.state.yellowPositions[i][1])))

        description = {
            'players': players,
            'currentTurn': currentTurn,
            'red': red,
            'green': green,
            'blue': blue,
            'yellow': yellow
        }
        description = json.dumps(description).replace(" ", "")
        return description
