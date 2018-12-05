#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket
import pygame
from board import Board
from pieceDrawer import PieceDrawer
from coordinates import Coordinates
import protocol
import datetime
import time

def insideStartGame((x,y)):
    if x >= 0 and y >= 0:
        return True
    return False


name = raw_input('Por favor, digite o seu nome de usuário: ')
# Conecta ao servidor
HOST = '192.168.0.8'     # Endereco IP do Servidor
PORT = 4000            # Porta que o Servidor esta
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
dest = (HOST, PORT)
# Tenta conectar ao servidor
print ("Trying to connect")
tcp.connect(dest)

# Verifica o nome
while True:
    print ("Verifying username")
    tcp.send('/USERNAME ' + name)
    print ("Waiting answer")
    msg = tcp.recv(1024)
    if not msg: break
    if msg.split(' ')[0] == '/DENY':
        name = raw_input('Nome de usuário já utilizado, digite um novo: ')
    elif msg.split(' ')[0] == '/CONFIRM':
        print("Bem vindo ao jogo " + name) 
        break

# Inicializa jogo
pygame.init()
inicialScreen = pygame.image.load("images/main_menu.jpg")
screen = pygame.display.set_mode((800, 600))

coords = Coordinates()
board = Board()
piecedrawer = PieceDrawer()

startTime = 0.0

state = {
    'inqueue' : False,
    'ingame' : False,
    #'screen' : inicialScreen,
    'screen' : board.BACKGROUND_IMAGE,
    'gamestate' : []
}

done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if  (pygame.mouse.get_pressed()[0] == 1) and \
        (insideStartGame(pygame.mouse.get_pos())) and \
        state['screen'] == inicialScreen:
            startTime = time.time()
            state['inqueue'] = True
            tcp.send(protocol.QueueMessage())
            print "Buscando Partida"
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                done = True

    screen.fill([255, 255, 255])
    screen.blit(state['screen'], state['screen'].get_rect())

    piecedrawer.drawRedPiece(screen, 360, 272, 15)
    piecedrawer.drawRedPiece(screen, 360, 292, 15)
    piecedrawer.drawRedPiece(screen, 360, 312, 15)
    piecedrawer.drawRedPiece(screen, 375, 292, 15)
    
    pygame.display.flip()

#msg = raw_input()
#while msg <> '\x18':
#    tcp.send (msg)
#    msg = raw_input()
tcp.close()