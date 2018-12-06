import socket
import thread
import mutex
from multiprocessing import Queue
import threading
import random
from state import State
from user import User
from match import Match

HOST = '172.27.44.177'         # Endereco IP do Servidor
PORT = 10000       # Porta que o Servidor esta

MATCH_ID = 0
MAX_QUEUE_SIZE = 4

userMutex = threading.Lock()
matchesMutex = threading.Lock()
queueMutex = threading.Lock()
readyMutex = threading.Lock()
connectedUsers = []
currentMatches = []
readyToPlay = []
userQueue = Queue(maxsize=MAX_QUEUE_SIZE)

def isMatch(identifier):
    for match in currentMatches:
        if match.identifier == identifier:
            return True

    return False

def getState(identifier):
    for match in currentMatches:
        if match.identifier == identifier:
            return match.state

    return False

def messageType(msg):
    return msg.split(' ')[0]

def updateUser(user):
    connectedUsers[user.username] = user

def createMatch(nickname):
    global MATCH_ID
    players = []
    for i in range(0, MAX_QUEUE_SIZE):
        players.append(connectedUsers[userQueue.get().username])
    matchId = MATCH_ID
    MATCH_ID += 1

    for player in players:
        readyToPlay.append([player, matchId])

    players.append(connectedUsers[nickname])
    currentMatches[MATCH_ID] = Match(players, matchId)


def conectado(con, cliente):
    global connectedUsers
    currentUser = User(cliente, '')
    print 'Conectado por', cliente

    while True:
        # Allways check:
        # If inqueue, if found match
        if currentUser.inqueue:
            readyMutex.acquire()
            for tupla in readyToPlay:
                if tupla[0].username == currentUser.username:
                    con.send('BEGIN' + ' ' + str(tupla[1]))
                    currentUser.inqueue = False
                    currentUser.ingame = True
                    break
            readyMutex.release()
            # Update user
            userMutex.acquire()
            updateUser(currentUser)
            userMutex.release()

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
                    if user.username == username:
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
                if userQueue.qsize == MAX_QUEUE_SIZE - 1:
                    con.send('/BEGIN' + ' ' + str(createMatch(currentUser.username)))
                    queueMutex.release()
                    # Mutex is released only after match is set
                    currentUser.ingame = True

                else:
                    userQueue.put(currentUser.username)
                    queueMutex.release()
                    con.send('/CONFIRM')
                    currentUser.inqueue = True

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
                    state = getState(currentMatch)
                    matchesMutex.release()
                    con.send('/UPDATE' + ' ' + state.toString())
                else:
                    matchesMutex.release()
                    # There is no such match
                    con.send('/DENY')

        # Dice message
        elif messageType(msg) == '/DICE':
            print 'DICE'
            con.send('/DICE ' + str(random.randint(1, 6)))

        # Move message
        #elif messageType(msg) == '/MOVE':

        # Exit message
        #elif messageType(msg) == '/EXIT':



    print 'Finalizando conexao do cliente', cliente
    userMutex.acquire()
    connectedUsers.remove(currentUser)
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
    print("coe")
    thread.start_new_thread(conectado, tuple([con, cliente]))

tcp.close()

