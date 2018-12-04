import socket
import thread

HOST = '192.168.0.8'      # Endereco IP do Servidor
PORT = 5000              # Porta que o Servidor esta

connectedUsers = []

def conectado(con, cliente):
    print 'Conectado por', cliente

    while True:
        msg = con.recv(1024)
        if not msg: break
        print cliente, msg
 
    print 'Finalizando conexao do cliente', cliente
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

