from state import State
from coordinates import Coordinates
import random
import movement
import random
import json
import time

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
        self.winner = -1
        # 'dice' or 'piece'
        self.currentPlay = 'dice'
        self.state = State(
            redInitials = self.coords.redInitials,
            greenInitials = self.coords.greenInitials,
            blueInitials = self.coords.blueInitials,
            yellowInitials = self.coords.yellowInitials,
        )

        # Inicially, all players are active,
        # exept the ones that didnt connect
        for i in range(0, len(self.players)):
            self.isActive.append(True)
        for i in range(len(self.players) -1, 4):
            self.isActive.append(False)


    def hasWon(self, player):
        if player == 0:
            positions = self.state.redPositions
            finals = self.coords.redFinals
        elif player == 1:
            positions = self.state.greenPositions
            finals = self.coords.greenFinals
        elif player == 2:
            positions = self.state.bluePositions
            finals = self.coords.blueFinals
        else:
            positions = self.state.yellowPositions
            finals = self.coords.yellowFinals

        print positions
        print finals
        if positions == finals:
            print 'infinals'
            return True

        return False
        
    def checkWinner(self):
        for i in range(0, 4):
            if self.isActive[i]:
                if self.hasWon(i):
                    print i
                    self.winner = i
                    return True
        
        return False

    def handleCollision(self, nextPosition, color):
        position = [
            self.coords.xValues[nextPosition],
            self.coords.yValues[nextPosition]
        ]

        if color != 'red':
            for i in range(0,4):
                if position == self.state.redPositions[i]:
                    self.state.redPositions[i] = self.coords.redInitials[i]
                    return

        if color != 'green':
            for i in range(0,4):
                if position == self.state.greenPositions[i]:
                    self.state.greenPositions[i] = self.coords.greenInitials[i]
                    return

        if color != 'blue':
            for i in range(0,4):
                if position == self.state.bluePositions[i]:
                    self.state.bluePositions[i] = self.coords.blueInitials[i]
                    return

        if color != 'yellow':
            for i in range(0,4):
                if position == self.state.yellowPositions[i]:
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
            position = self.state.redPositions[piece]
            finals = self.coords.redFinals
        elif user == 1:
            color = 'green'
            positions = self.state.greenPositions
            position = self.state.greenPositions[piece]
            finals = self.coords.greenFinals
        elif user == 2:
            color = 'blue'
            positions = self.state.bluePositions
            position = self.state.bluePositions[piece]
            finals = self.coords.blueFinals
        else:
            color = 'yellow'
            positions = self.state.yellowPositions
            position = self.state.yellowPositions[piece]
            finals = self.coords.yellowFinals

        # Verifica se esta em uma das posicoes finais
        if position in finals:
            return False

        nextPosition = movement.movePiece(
            position,
            self.diceValue, 
            color, 
            self.coords
        )

        # handle final position of piece
        if nextPosition >= 76:
            print ("Finals")
            self.state.updatePosition(
                color,
                piece,
                finals[piece][0],
                finals[piece][1],
            )
            self.nextPlayer()
            self.alternatePlay()
            return True
            

        # Checks if another piece from the same color is there
        for i in range(0, 4):
            if int(i) != int(pieceIndex):
                if positions[i][0] == self.coords.xValues[nextPosition] and positions[i][1] == self.coords.yValues[nextPosition]:
                    return False

        # Checks if another piece from another color is there
        self.handleCollision(nextPosition, color)
        
        # Updates value on state
        self.state.updatePosition(
            color, 
            piece,
            self.coords.xValues[nextPosition],
            self.coords.yValues[nextPosition]
        )
        
        # Check winner
        if self.checkWinner():
            self.ended = True
        
        
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
        inGame = []
        for i in range(0,4):
            if self.isActive[i]:
                inGame.append(i)
        if len(inGame) == 1:
            if self.winner == -1:
                self.winner = inGame[0]
            self.turn = inGame[0]
        elif len(inGame) == 0:
            return
        else:
            if not self.isActive[self.turn]:
                self.nextPlayer()

    def quit(self, user):
        if self.turn == user:
            self.currentPlay = 'dice'

        self.isActive[user] = False
        self.nextPlayer()


    # String to send as a message
    def toString(self, playerIndex):
        # Players first
        splayerIndex = str(playerIndex)
        players = {}
        for player in self.players:
            players[player] = len(players)

        dice = str(self.diceValue)
        winner = str(self.winner)

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
            'playerIndex': splayerIndex,
            'players': players,
            'currentTurn': currentTurn,
            'currentPlay': currentPlay,
            'dice': dice,
            'winner': winner,
            'red': red,
            'green': green,
            'blue': blue,
            'yellow': yellow
        }
        description = json.dumps(description).replace(" ", "")
        return description
