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
        return init + moves

    # Zona Critica de Entrada
    if position <= cmax and position >= cmax - 5:
        if moves == 6 and position == cmax:
            return final
        return fst + ((position + moves) % cmax)
    # Acerto
    if position + moves == fst + 5:
        return final
    # Move back
    if position + moves > fst + 5:
        return (fst + 5) - (position + moves) % (fst + 5)
    # Zona Critica de Map Loop
    if position + moves > 55:
        return (position + moves) %  55
    # Default
    return position + moves
