QUEUE = '/QUEUE'
STATE = '/STATE'
DICE = '/DICE'
MOVE = '/MOVE'
EXIT = '/EXIT'

BEGIN = '/BEGIN'
UPDATE = '/UPDATE'
CONFIRM = '/CONFIRM'
DENY = '/DENY'
END = '/END'

def QueueMessage():
    return QUEUE

def StateMessage(gameid):
    return STATE + ' ' + gameid

def DiceMessage():
    return DICE

def MoveMessage(pieceNum):
    return MOVE + ' ' + pieceNum

def ExitMessage():
    return EXIT

def ReadMessage(message):
    return message.split(' ')


def HandleDice():
    return DICE + ' ' +str(rand.randint(1, 6))

#def HandleQueue