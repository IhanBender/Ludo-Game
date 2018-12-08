from state import State
from coordinates import Coordinates
import random
import movement
import random
import json

#RED = 0
#GREEN = 1
#BLUE = 2
#YELLOW = 3

class Match():
    def __init__(self, players):

        self.ended = False
        self.coords = Coordinates()
        self.diceValue = 0
        self.players = players
        self.isActive = []
        self.turn = random.randint(0,len(self.players) - 1)
        # 'dice' or 'piece'
        self.currentPlay = 'dice'
        self.state = State(
            redInitials = self.coords.redInitials,
            greenInitials = self.coords.greenInitials,
            blueInitials = self.coords.blueInitials,
            yellowInitials = self.coords.yellowInitials,
        )

        # Inicially, all players are active
        for i in range(0, len(self.players)):
            self.isActive.append(True)


    # Not the fastest way, but the cleanest way
    def handleCollision(self, nextPosition, color):
        for p in self.state.redPositions:
            for i in range(0,4):
                if p == self.state.redPositions[i]:
                    self.state.redPositions[i] = self.coords.redInitials[i]
                    return
        for p in self.state.greenPositions:
            for i in range(0,4):
                if p == self.state.greenPositions[i]:
                    self.state.greenPositions[i] = self.coords.greenInitials[i]
                    return
        for p in self.state.bluePositions:
            for i in range(0,4):
                if p == self.state.bluePositions[i]:
                    self.state.bluePositions[i] = self.coords.blueInitials[i]
                    return
        for p in self.state.yellowPositions:
            for i in range(0,4):
                if p == self.state.yellowPositions[i]:
                    self.state.yellowPositions[i] = self.coords.yellowInitials[i]
                    return

    def alternatePlay(self):
        if self.currentPlay == 'dice':
            self.currentPlay = 'piece'
        else:
            self.currentPlay = 'dice'

    def movePiece(self, pieceIndex, user):
        piece = int(pieceIndex)

        # Getting info based on user
        if user == 0:
            color = 'red'
            positions = self.state.redPositions
            others = [
                self.state.greenPositions,
                self.state.bluePositions,
                self.state.yellowPositions
            ]
            position = self.state.redPositions[piece]
        elif user == 1:
            color = 'green'
            positions = self.state.greenPositions
            others = [
                self.state.redPositions,
                self.state.bluePositions,
                self.state.yellowPositions
            ]
            position = self.state.greenPositions[piece]

        elif user == 2:
            color = 'blue'
            positions = self.state.bluePositions
            others = [
                self.state.redPositions,
                self.state.greenPositions,
                self.state.yellowPositions
            ]
            position = self.state.bluePositions[piece]
        else:
            color = 'yellow'
            positions = self.state.yellowPositions
            others = [
                self.state.redPositions,
                self.state.greenPositions,
                self.state.bluePositions
            ]
            position = self.state.yellowPositions[piece]

        nextPosition = movement.movePiece(position, self.diceValue, color)

        # Checks if another piece from the same color is there
        for pos in positions:
            if pos[0] == nextPosition[0]    \
            and pos[1] == nextPosition[1]:
                return False

        # Checks if another piece from another color is there
        self.handleCollision(nextPosition, color)

        # Updates state
        if color == 'red':
            self.state.redPositions[piece] = nextPosition
        elif color == 'green':
            self.state.greenPositions[piece] = nextPosition
        elif color == 'blue':
            self.state.bluePositions[piece] = nextPosition
        elif color == 'yellow':
            self.state.yellowPositions[piece] = nextPosition

        # Since movement is valid, can update some important values
        self.nextPlayer()
        self.alternatePlay()

        return True

    def generateDice(self):
        self.diceValue = random.randint(1,6)

    def nextPlayer(self):
        if self.turn == len(self.players) - 1:
            self.turn = 0
        else:
            self.turn += 1

        # Deals with afk/disconnected players
        if not self.isActive[self.turn]:
            self.nextPlayer()

    def quit(self, user):
        if self.turn == user:
            self.currentPlay = 'dice'

        self.isActive[user] = False
        self.nextPlayer()


    # String to send as a message
    def toString(self):
        # Players first
        players = {}
        for player in self.players:
            players[player.username] = len(players)

        # Current turn
        currentTurn = str(self.turn)
        # Current play
        currentPlay = self.currentPlay
        # Positions:
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
            'currentPlay': currentPlay,
            'red': red,
            'green': green,
            'blue': blue,
            'yellow': yellow
        }
        description = json.dumps(description).replace(" ", "")
        return description
