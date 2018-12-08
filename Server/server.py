import socket
import thread
import mutex
from multiprocessing import Queue
import threading
import random
from state import State
from user import User
from match import Match

HOST = '192.168.0.102'         # Endereco IP do Servidor
PORT = 5000      # Porta que o Servidor esta

MATCH_ID = 0
MAX_QUEUE_SIZE = 2

userMutex = threading.Lock()
matchesMutex = threading.Lock()
queueMutex = threading.Lock()
readyMutex = threading.Lock()
connectedUsers = {}
currentMatches = []
readyToPlay = []
userQueue = Queue(maxsize=MAX_QUEUE_SIZE)

def isMatch(identifier):
    for match in currentMatches:
        if str(match.identifier) == str(identifier):
            return True

    return False

def getState(identifier):
    for match in currentMatches:
        if str(match.identifier) == str(identifier):
            return match

    return False

def messageType(msg):
    return msg.split(' ')[0]

def updateUser(user):
    connectedUsers[user.username] = user

def createMatch(nickname):
    global MATCH_ID
    players = {}
    for i in range(0, MAX_QUEUE_SIZE):
        players[connectedUsers[userQueue.get()]] = len(players) + 1
    matchId = MATCH_ID
    MATCH_ID += 1

    i = 0
    for player in players:
        readyToPlay.append([player, matchId, i])
        i += 1
    players[connectedUsers[nickname]] = len(players) + 1
    currentMatches.append(Match(players, matchId))

    return [matchId, i]

def conectado(con, cliente):
    global connectedUsers
    currentUser = User(cliente, '')
    print 'Conectado por', cliente

    while True:

        # handle message
        msg = con.recv(1024)
        if not msg: break

        # Receiving messages
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
                currentUser = User(cliente, username)
                userMutex.acquire()
                connectedUsers[username] = currentUser
                userMutex.release()

        # Queue message
        elif messageType(msg) == '/QUEUE':
            if currentUser.inqueue or currentUser.ingame or currentUser.username == '':
                con.send('/DENY')
            else:
                queueMutex.acquire()
                if userQueue.qsize() == MAX_QUEUE_SIZE - 1:
                    userQueue.put(currentUser.username)
                    con.send('/BEGIN ' + str(createMatch(currentUser.username)))
                    queueMutex.release()
                    # Mutex is released only after match is set
                    currentUser.ingame = True

                else:
                    userQueue.put(currentUser.username)
                    queueMutex.release()
                    con.send('/CONFIRM')
                    currentUser.inqueue = True
                    # Update user
                    userMutex.acquire()
                    updateUser(currentUser)
                    userMutex.release()
                    # Waits for game start
                    while currentUser.inqueue:
                        readyMutex.acquire()
                        for tupla in readyToPlay:
                            if tupla[0].username == currentUser.username:
                                con.send('/BEGIN' + ' ' + str(tupla[1]))
                                currentUser.inqueue = False
                                currentUser.ingame = True
                                currentUser.playerIndex = tupla[2]
                                break
                        readyMutex.release()

                userMutex.acquire()
                updateUser(currentUser)
                userMutex.release()

        # State message
        elif messageType(msg) == '/STATE':
            if currentUser.username == '':
                con.send('/DENY')
            else:
                # Get parameter
                currentMatch = msg.split(' ')[1]
                matchesMutex.acquire()
                if isMatch(currentMatch):
                    stat = getState(currentMatch)
                    matchesMutex.release()
                    con.send('/UPDATE ' + stat.toString())
                else:
                    matchesMutex.release()
                    # There is no such match
                    con.send('/DENY')

        # Dice message
        elif messageType(msg) == '/DICE':
            if(currentUser.username == '' or (not currentUser.ingame)):
                con.send('/DENY')
            else:
                if currentMatches[currentUser.match_id].currentPlay == 'dice' \
                and currentMatches[currentUser.match_id].state.turn ==  \
                currentUser.playerIndex:
                    currentMatches[currentUser.match_id].alternatePlay()
                    con.send('/DICE ' + str(random.randint(1, 6)))
                else:
                    con.send('/DENY')

        # Move message
        # /MOVE piece dice
        elif messageType(msg) == '/MOVE':
            if(currentUser.username == '' or (not currentUser.ingame) \
            or currentMatches[currentUser.playerIndex].currentPlay !='piece' \
            or currentMatches[currentUser.playerIndex].turn != \
            currentUser.playerIndex):
                con.send('/DENY')
            else:
                movement = msg.split(' ')[1:]
                if (currentMatches[currentUser.match_id].movePiece(
                movement, currentUser.playerIndex
                )):
                    currentMatches[currentUser.playerIndex].alternatePlay()
                    currentMatches[currentUser.playerIndex].nextPlayer()
                    con.send("/CONFIRM")
                else:
                    con.send('/DENY')


        # Exit message
        elif messageType(msg) == '/EXIT':
            break


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

