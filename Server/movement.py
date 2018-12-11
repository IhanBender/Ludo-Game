#!/usr/bin/env python
# -*- coding: utf-8 -*-import socket
from coordinates import Coordinates

def redStart():
    return 0

def greenStart():
    return 14

def blueStart():
    return 28

def yellowStart():
    return 42

redInit = 0
redMax = 55
redFst = 56
redFinal = 76

grnInit = 14
grnMax = 13
grnFst = 61
grnFinal = 77

bluInit = 28
bluMax = 27
bluFst = 66
bluFinal = 78

yelInit = 42
yelMax = 41
yelFst = 71
yelFinal = 79


def movePiece(position, moves, color, coords):
    # Identifica a cor
    if color == "green":
        cmax = grnMax
        fst = grnFst
        final = grnFinal
        init = grnInit
        initials = coords.greenInitials
    elif color == "red":
        cmax = redMax
        fst = redFst
        final = redFinal
        init = redInit
        initials = coords.redInitials
    elif color == "blue":
        cmax = bluMax
        fst = bluFst
        final = bluFinal
        init = bluInit
        initials = coords.blueInitials
    elif color == "yellow":
        cmax = yelMax
        fst = yelFst
        final = yelFinal
        init = yelInit
        initials = coords.yellowInitials
    # Error
    else:
        return -1

    # Verifica se esta em uma das posições iniciais
    if position in initials:
        print 'at initials'
        return init + moves - 1

    # Encontra o indice correspondente
    index = 0
    for i in range(0, len(coords.xValues)):
        if position[0] == coords.xValues[i] \
        and position[1] == coords.yValues[i]:
            index = int(i)
            break
    print 'index: ',index

    # Zona Critica de Entrada
    if index <= cmax and index >= cmax - 5:
        print 'in zona critica'
        if moves == 6 and index == cmax:
            print 'Direto pro final'
            return final
        elif moves + index <= cmax:
            print 'keep on critic'
            return moves + index
        print 'entering the realm'
        return fst + ((index + moves) % cmax) - 1
    # Acerto
    if index + moves == fst + 5:
        print 'pro final'
        return final
    # Move back
    if index + moves > fst + 5:
        print 'move back'
        return (fst + 5) - (index + moves) % (fst + 5)
    # Zona Critica de Map Loop
    if index + moves > 55 and index <= 55:
        print 'loop'
        return (index + moves) % 55 - 1
    # Default
    print 'default case: ', index, moves, index+moves
    return index + moves
