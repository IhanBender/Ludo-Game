def redStart():
    return 0

def greenStart():
    return 14

def blueStart():
    return 28

def yellowStart():
    return 42

redMax = 55
redFst = 56
redFinal = 76

grnMax = 13
grnFst = 61
grnFinal = 77

bluMax = 27
bluFst = 66
bluFinal = 78

yelMax = 41
yelFst = 71
yelFinal = 79


def movePiece(position, moves, color):
    if color == "green":
        cmax = grnMax
        fst = grnFst
        final = grnFinal
    elif color == "red":
        cmax = redMax
        fst = redFst
        final = redFinal
    elif color == "blue":
        cmax = bluMax
        fst = bluFst
        final = bluFinal
    elif color == "yellow":
        cmax = yelMax
        fst = yelFst
        final = yelFinal
    # Error
    else return -1

    # Zona Critica de Entrada
    if position <= cmax and >= cmax - 5:
        if moves == 6 and position = cmax:
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
