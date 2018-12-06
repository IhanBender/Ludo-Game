import socket
import thread
import mutex
from multiprocessing import Queue
import threading
import random
from state import State
from user import User
import netifaces as ni

interfaces = ni.interfaces()
if 'wlp3s0' in interfaces:
    ip = ni.ifaddresses('wlp3s0')[ni.AF_INET][0]['addr']
else:
    ip = '192.168.0.8'

HOST = ip         # Endereco IP do Servidor
PORT = 4000       # Porta que o Servidor esta

userMutex = threading.Lock()
matchesMutex = threading.Lock()
queueMutex = threading.Lock()
connectedUsers = []
currentMatches = []
userQueue = Queue(maxsize=4)

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
    userMutex.acquire()
    for i in range(0, len(connectedUsers)):
        if user.username == connectedUsers[i].username:
            connectedUsers[i] = user

####
# def createMatch(nickname):
    # This function has to:
        # Create Match
        # Empty queue
        # Notify other 3 players (somehow)

def conectado(con, cliente):
    global connectedUsers
    currentUser = User(cliente, '')
    print 'Conectado por', cliente

    while True:
        msg = con.recv(1024)
        if not msg: break

        # Allways check:
        # if

        # Receiving messages
        # Username message
        if messageType(msg) == '/USERNAME':
            username = msg.split(' ')[1]
            for user in connectedUsers:
                if user.username == username:
                    con.send('/DENY')
                    print ("Username denied")
                    break
            con.send('/CONFIRM')
            currentUser = User(cliente, username)
            userMutex.acquire()
            connectedUsers.append(currentUser)
            userMutex.release()
        
        elif messageType(msg) == '/QUEUE':
            if currentUser.inqueue or currentUser.ingame:
                con.send('/DENY')
            else:
                queueMutex.acquire()
                if userQueue.size() == 3:
                    queueMutex.release()
                    con.send('/BEGIN' + ' ' + str(createMatch(currentUser.username)))
                    currentUser.ingame = True

                else:
                    userQueue.put(currentUser.username)
                    queueMutex.release()
                    con.send('/CONFIRM')
                    currentUser.inqueue = True
                
                updateUser(currentUser)


        elif messageType(msg) == '/STATE':
            # Get parameter
            currentMatch = msg.split(' ')[1]
            matchesMutex.acquire()
            if isMatch(currentMatch):
                state = getState(currentMatch)
                matchesMutex.release()
                con.send('/UPDATE' + ' ' + stateToString(state))
            else:
                matchesMutex.release()
                # There is no such match
                con.send('/DENY')

        elif messageType(msg) == '/DICE':
            print 'DICE'
            con.send('/DICE ' + str(random.randint(1, 6)))
        #elif messageType(msg) == '/MOVE':
            
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

