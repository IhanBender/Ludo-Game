import socket
import thread
import mutex
import threading
from user import User

HOST = '192.168.0.8'      # Endereco IP do Servidor
PORT = 4000              # Porta que o Servidor esta

userMutex = threading.Lock()
matchesMutex = threading.Lock()
connectedUsers = []
currentMatches = []

def messageType(msg):
    return msg.split(' ')[0]

def conectado(con, cliente):
    global connectedUsers
    currentUser = User(cliente, '')
    print 'Conectado por', cliente

    while True:
        msg = con.recv(1024)
        if not msg: break
        print msg
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

