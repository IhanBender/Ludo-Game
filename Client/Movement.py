redMin = 0
redMax = 55

grenMin = 14
grnMax = 13

bluMin = 28
bluMax = 27

yelMin = 42
yelMax = 41


def moveRedPiece(position, moves):
    if position + moves >= 56:
        if position + moves >= 61:
            if position + moves == 61:
                return 76
            else:
                return 61 - ((position + moves) % 61)

    return position + moves
