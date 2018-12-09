import socket
import thread
import mutex
from multiprocessing import Queue
import threading
from state import State
from user import User
from match import Match

HOST = '192.168.0.111'         # Endereco IP do Servidor
PORT = 7000      # Porta que o Servidor esta

MATCH_ID_COUNT = 0
MATCH_ID_REUSABLE = []

MATCH_SIZE = 2

userMutex = threading.Lock()
matchesMutex = threading.Lock()
connectedUsers = {}
currentMatches = []
userQueue = Queue(maxsize=0)

def checkMatchExistance(match_id):
    return (True in currentMatches[match_id].isActive)

def getNewMatchId():
    global MATCH_ID_COUNT
    global MATCH_ID_REUSABLE

    if len(MATCH_ID_REUSABLE) != 0:
        value = MATCH_ID_REUSABLE[-1]
        del MATCH_ID_REUSABLE[-1]
    else:
        value = MATCH_ID_COUNT
        MATCH_ID_COUNT += 1

    return value

def endMatch(value):
    global MATCH_ID_REUSABLE
    MATCH_ID_REUSABLE.append(value)
    currentMatches.pop(value)

def messageType(msg):
    return msg.split(' ')[0]

def updateUser(user):
    connectedUsers[user.username] = user

def createMatch():

    matchId = getNewMatchId()

    # Define match players
    players = {}
    for i in range(0, MATCH_SIZE):
        player = userQueue.get()
        # Add to match list
        players[player] = i
        userMutex.acquire()
        # Inform match id and players index
        connectedUsers[player].match_id = matchId
        connectedUsers[player].playerIndex = i
        # Inform that is ingame
        connectedUsers[player].ingame = True
        connectedUsers[player].inqueue = False
        userMutex.release()

    if len(currentMatches) > matchId:
        currentMatches[matchId] = Match(players)
    else:
        currentMatches.append(Match(players))


def conectado(con, cliente):
    global connectedUsers
    currentUser = User('')
    print 'Conectado por', cliente

    while True:
        msg = con.recv(1024)
        if not msg: break

        # Username message
        if messageType(msg) == '/USERNAME':
            username = msg.split(' ')[1]
            if username == '':
                con.send('/DENY')
            else:
                for user in connectedUsers:
                    if user == username:
                        con.send('/DENY')
                        print ("Username denied")
                        break
                con.send('/CONFIRM')
                currentUser = User(username)
                userMutex.acquire()
                connectedUsers[username] = currentUser
                userMutex.release()

        # Queue message
        elif messageType(msg) == '/QUEUE':
            if currentUser.inqueue or currentUser.ingame or currentUser.username == '':
                con.send('/DENY')
            else:
                userQueue.put(currentUser.username)
                if userQueue.qsize() == MATCH_SIZE:
                    createMatch()
                else:
                    currentUser.inqueue = True
                    # Update user
                    userMutex.acquire()
                    updateUser(currentUser)
                    userMutex.release()
                    con.send('/CONFIRM')
                    # Waits for game start
                    while currentUser.inqueue:
                        pass

                print 'Sending begin to ', cliente
                userMutex.acquire()
                currentUser = connectedUsers[currentUser.username]
                userMutex.release()
                con.send('/BEGIN ' + str(currentUser.match_id))

        # State message
        elif messageType(msg) == '/STATE':
            if currentUser.username == '' or \
            not currentUser.ingame:
                con.send('/DENY')
            else:
                matchesMutex.acquire()
                description = currentMatches[currentUser.match_id].toString()
                matchesMutex.release()
                con.send('/UPDATE ' + description)

        # Dice message
        elif messageType(msg) == '/DICE':
            if(currentUser.username == '' or (not currentUser.ingame)):
                con.send('/DENY')
            else:
                matchesMutex.acquire()
                if currentMatches[currentUser.match_id].currentPlay == 'dice' \
                and currentMatches[currentUser.match_id].turn ==  \
                currentUser.playerIndex:
                    currentMatches[currentUser.match_id].alternatePlay()
                    currentMatches[currentUser.match_id].generateDice()
                    matchesMutex.release()
                    con.send('/CONFIRM')
                else:
                    matchesMutex.release()
                    con.send('/DENY')

        # Move message
        elif messageType(msg) == '/MOVE':
            matchesMutex.acquire()
            if(currentUser.username == '' or (not currentUser.ingame) \
            or currentMatches[currentUser.playerIndex].currentPlay !='piece' \
            or currentMatches[currentUser.playerIndex].turn != \
            currentUser.playerIndex):
                matchesMutex.release()
                con.send('/DENY')
            else:
                matchesMutex.release()
                pieceIndex = msg.split(' ')[1]
                matchesMutex.acquire()
                if (currentMatches[currentUser.match_id].movePiece(
                    pieceIndex, currentUser.playerIndex
                )):
                    matchesMutex.release()
                    con.send("/CONFIRM")
                else:
                    matchesMutex.release()
                    con.send('/DENY')

        # Exit game message
        elif messageType(msg) == '/EXIT':
            if currentUser.username == '' or (not currentUser.ingame):
                con.send('/DENY')
            else:
                matchesMutex.acquire()
                currentMatches[currentUser.match_id].quit()
                if checkMatchExistance(currentUser.match_id):
                    endMatch(currentUser.match_id)
                matchesMutex.release()

                currentUser.ingame = False
                currentUser.match_id = -1
                updateUser(currentUser)



    print 'Finalizando conexao do cliente', cliente
    userMutex.acquire()
    del connectedUsers[currentUser.username]
    userMutex.release()

    con.close()
    thread.exit()

tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

orig = (HOST, PORT)
tcp.bind(orig)
tcp.listen(1)

print ("Server on")
while True:
    print("listening")
    (con, cliente) = tcp.accept()
    thread.start_new_thread(conectado, tuple([con, cliente]))

tcp.close()

