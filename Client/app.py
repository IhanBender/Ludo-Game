import socket
HOST = '0.0.0.0'     # Endereco IP do Servidor
PORT = 5000            # Porta que o Servidor esta
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
dest = (HOST, PORT)
print ("Trying to connect")
tcp.connect(dest)
print 'Para sair use CTRL+X\n'
msg = raw_input()
while msg <> '\x18':
    tcp.send (msg)
    msg = raw_input()
tcp.close()