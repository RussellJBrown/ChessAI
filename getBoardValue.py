import ast
import chess
import sys
def createDictionaryList():
    piecesValueWhite = []
    piecesValueBlack = []

    piecesValueBlack.append(readDictionary("pawnBlack.txt"))
    piecesValueBlack.append(readDictionary("knightBlack.txt"))
    piecesValueBlack.append(readDictionary("bishopBlack.txt"))
    piecesValueBlack.append(readDictionary("rookBlack.txt"))
    piecesValueBlack.append(readDictionary("queenBlack.txt"))
    piecesValueBlack.append(readDictionary("kingEarlyBlack.txt"))
    piecesValueBlack.append(readDictionary("kingLateBlack.txt"))

    piecesValueWhite.append(readDictionary("pawnWhite.txt"))
    piecesValueWhite.append(readDictionary("knightWhite.txt"))
    piecesValueWhite.append(readDictionary("bishopWhite.txt"))
    piecesValueWhite.append(readDictionary("rookWhite.txt"))
    piecesValueWhite.append(readDictionary("queenWhite.txt"))
    piecesValueWhite.append(readDictionary("kingEarlyWhite.txt"))
    piecesValueWhite.append(readDictionary("kingLateWhite.txt"))

    return piecesValueBlack, piecesValueWhite



def readDictionary(file):
    file = open(file,"r")
    contents = file.read()
    moveValues=ast.literal_eval(contents)
    file.close()
    return moveValues


def getValuePosition(piece,piecesValueBlack,piecesValueWhite,move,lateGame):
    piece_type=""
    piece_colour=""
    value = 0
    pieceValue=0
    try:
        piece_type = piece.piece_type
        piece_colour = piece.color

        if piece_colour==False:
            if piece_type==1:
                pawnValues = piecesValueBlack[0]
                value = pawnValues[move]
                pieceValue = -1

            if piece_type==2:
                knightValues = piecesValueBlack[1]
                value = knightValues[move]
                pieceValue = -3

            if piece_type==3:
                bishopValues = piecesValueBlack[2]
                value = bishopValues[move]
                pieceValue = -3

            if piece_type==4:
                rookValues = piecesValueBlack[3]
                value = rookValues[move]
                pieceValue = -5

            if piece_type==5:
                queenValues = piecesValueBlack[4]
                value = queenValues[move]
                pieceValue = -9

            if piece_type==6 and lateGame==False:
                kingValues = piecesValueBlack[5]
                value = kingValues[move]

            if piece_type==6 and lateGame:
                kingValues = piecesValueBlack[6]
                value = kingValues[move]

        else:
            if piece_type==1:
                pawnValues = piecesValueWhite[0]
                value = pawnValues[move]
                pieceValue = 1

            if piece_type==2:
                knightValues = piecesValueWhite[1]
                value = knightValues[move]
                pieceValue = 3

            if piece_type==3:
                bishopValues = piecesValueWhite[2]
                value = bishopValues[move]
                pieceValue = 3

            if piece_type==4:
                rookValues = piecesValueWhite[3]
                value = rookValues[move]
                pieceValue = 5

            if piece_type==5:
                queenValues = piecesValueWhite[4]
                value = queenValues[move]
                pieceValue = 9

            if piece_type==6 and lateGame==False:
                kingValues = piecesValueWhite[5]
                value = kingValues[move]

            if piece_type==6 and lateGame:
                kingValues = piecesValueWhite[6]
                value = kingValues[move]

        return value, pieceValue
    except:
        return 0

def addValue(value, piece_value, valueT, piece_valueT):
    value+=valueT
    piece_value+=piece_valueT
    return value, piece_value

def BoardValue(board,lateGame):

    piecesValueBlack, pieceValueWhite = createDictionaryList()
    value = 0
    piece_value = 0
    #A
    valueT,piece_valueT=getValuePosition(board.piece_at(chess.A1),piecesValueBlack,pieceValueWhite,"a1",lateGame)
    value, piece_value = addValue(value,piece_value,valueT,piece_valueT)

    valueT,piece_valueT+=getValuePosition(board.piece_at(chess.A2),piecesValueBlack,pieceValueWhite,"a2",lateGame)
    value, piece_value = addValue(value,piece_value,valueT,piece_valueT)

    valueT,piece_valueT=getValuePosition(board.piece_at(chess.A3),piecesValueBlack,pieceValueWhite,"a3",lateGame)
    value, piece_value = addValue(value,piece_value,valueT,piece_valueT)

    valueT,piece_valueT=getValuePosition(board.piece_at(chess.A4),piecesValueBlack,pieceValueWhite,"a4",lateGame)
    value, piece_value = addValue(value,piece_value,valueT,piece_valueT)

    valueT,piece_valueT=getValuePosition(board.piece_at(chess.A5),piecesValueBlack,pieceValueWhite,"a5",lateGame)
    value, piece_value = addValue(value,piece_value,valueT,piece_valueT)

    valueT,piece_valueT=getValuePosition(board.piece_at(chess.A6),piecesValueBlack,pieceValueWhite,"a6",lateGame)
    value, piece_value = addValue(value,piece_value,valueT,piece_valueT)

    valueT,piece_valueT=getValuePosition(board.piece_at(chess.A7),piecesValueBlack,pieceValueWhite,"a7",lateGame)
    value, piece_value = addValue(value,piece_value,valueT,piece_valueT)

    valueT,piece_valueT=getValuePosition(board.piece_at(chess.A8),piecesValueBlack,pieceValueWhite,"a8",lateGame)
    value, piece_value = addValue(value,piece_value,valueT,piece_valueT)

    #B
    valueT,piece_valueT=getValuePosition(board.piece_at(chess.B1),piecesValueBlack,pieceValueWhite,"b1",lateGame)
    value, piece_value = addValue(value,piece_value,valueT,piece_valueT)

    valueT,piece_valueT=getValuePosition(board.piece_at(chess.B2),piecesValueBlack,pieceValueWhite,"b2",lateGame)
    value, piece_value = addValue(value,piece_value,valueT,piece_valueT)

    valueT,piece_valueT=getValuePosition(board.piece_at(chess.B3),piecesValueBlack,pieceValueWhite,"b3",lateGame)
    value, piece_value = addValue(value,piece_value,valueT,piece_valueT)

    valueT,piece_valueT=getValuePosition(board.piece_at(chess.B4),piecesValueBlack,pieceValueWhite,"b4",lateGame)
    value, piece_value = addValue(value,piece_value,valueT,piece_valueT)

    valueT,piece_valueT=getValuePosition(board.piece_at(chess.B5),piecesValueBlack,pieceValueWhite,"b5",lateGame)
    value, piece_value = addValue(value,piece_value,valueT,piece_valueT)

    valueT,piece_valueT=getValuePosition(board.piece_at(chess.B6),piecesValueBlack,pieceValueWhite,"b6",lateGame)
    value, piece_value = addValue(value,piece_value,valueT,piece_valueT)

    valueT,piece_valueT=getValuePosition(board.piece_at(chess.B7),piecesValueBlack,pieceValueWhite,"b7",lateGame)
    value, piece_value = addValue(value,piece_value,valueT,piece_valueT)

    valueT,piece_valueT=getValuePosition(board.piece_at(chess.B8),piecesValueBlack,pieceValueWhite,"b8",lateGame)
    value, piece_value = addValue(value,piece_value,valueT,piece_valueT)

    #C
    valueT,piece_valueT=getValuePosition(board.piece_at(chess.C1),piecesValueBlack,pieceValueWhite,"c1",lateGame)
    value, piece_value = addValue(value,piece_value,valueT,piece_valueT)

    valueT,piece_valueT=getValuePosition(board.piece_at(chess.C2),piecesValueBlack,pieceValueWhite,"c2",lateGame)
    value, piece_value = addValue(value,piece_value,valueT,piece_valueT)

    valueT,piece_valueT=getValuePosition(board.piece_at(chess.C3),piecesValueBlack,pieceValueWhite,"c3",lateGame)
    value, piece_value = addValue(value,piece_value,valueT,piece_valueT)

    valueT,piece_valueT=getValuePosition(board.piece_at(chess.C4),piecesValueBlack,pieceValueWhite,"c4",lateGame)
    value, piece_value = addValue(value,piece_value,valueT,piece_valueT)

    valueT,piece_valueT=getValuePosition(board.piece_at(chess.C5),piecesValueBlack,pieceValueWhite,"c5",lateGame)
    value, piece_value = addValue(value,piece_value,valueT,piece_valueT)

    valueT,piece_valueT=getValuePosition(board.piece_at(chess.C6),piecesValueBlack,pieceValueWhite,"c6",lateGame)
    value, piece_value = addValue(value,piece_value,valueT,piece_valueT)

    valueT,piece_valueT=getValuePosition(board.piece_at(chess.C7),piecesValueBlack,pieceValueWhite,"c7",lateGame)
    value, piece_value = addValue(value,piece_value,valueT,piece_valueT)

    valueT,piece_valueT=getValuePosition(board.piece_at(chess.C8),piecesValueBlack,pieceValueWhite,"c8",lateGame)
    value, piece_value = addValue(value,piece_value,valueT,piece_valueT)

    #D
    valueT,piece_valueT=getValuePosition(board.piece_at(chess.D1),piecesValueBlack,pieceValueWhite,"d1",lateGame)
    value, piece_value = addValue(value,piece_value,valueT,piece_valueT)

    valueT,piece_valueT=getValuePosition(board.piece_at(chess.D2),piecesValueBlack,pieceValueWhite,"d2",lateGame)
    value, piece_value = addValue(value,piece_value,valueT,piece_valueT)

    valueT,piece_valueT=getValuePosition(board.piece_at(chess.D3),piecesValueBlack,pieceValueWhite,"d3",lateGame)
    value, piece_value = addValue(value,piece_value,valueT,piece_valueT)

    valueT,piece_valueT=getValuePosition(board.piece_at(chess.D4),piecesValueBlack,pieceValueWhite,"d4",lateGame)
    value, piece_value = addValue(value,piece_value,valueT,piece_valueT)

    valueT,piece_valueT=getValuePosition(board.piece_at(chess.D5),piecesValueBlack,pieceValueWhite,"d5",lateGame)
    value, piece_value = addValue(value,piece_value,valueT,piece_valueT)

    valueT,piece_valueT=getValuePosition(board.piece_at(chess.D6),piecesValueBlack,pieceValueWhite,"d6",lateGame)
    value, piece_value = addValue(value,piece_value,valueT,piece_valueT)

    valueT,piece_valueT=getValuePosition(board.piece_at(chess.D7),piecesValueBlack,pieceValueWhite,"d7",lateGame)
    value, piece_value = addValue(value,piece_value,valueT,piece_valueT)

    valueT,piece_valueT=getValuePosition(board.piece_at(chess.D8),piecesValueBlack,pieceValueWhite,"d8",lateGame)
    value, piece_value = addValue(value,piece_value,valueT,piece_valueT)

    #E
    valueT,piece_valueT=getValuePosition(board.piece_at(chess.E1),piecesValueBlack,pieceValueWhite,"e1",lateGame)
    value, piece_value = addValue(value,piece_value,valueT,piece_valueT)

    valueT,piece_valueT=getValuePosition(board.piece_at(chess.E2),piecesValueBlack,pieceValueWhite,"e2",lateGame)
    value, piece_value = addValue(value,piece_value,valueT,piece_valueT)

    valueT,piece_valueT=getValuePosition(board.piece_at(chess.E3),piecesValueBlack,pieceValueWhite,"e3",lateGame)
    value, piece_value = addValue(value,piece_value,valueT,piece_valueT)

    valueT,piece_valueT=getValuePosition(board.piece_at(chess.E4),piecesValueBlack,pieceValueWhite,"e4",lateGame)
    value, piece_value = addValue(value,piece_value,valueT,piece_valueT)

    valueT,piece_valueT=getValuePosition(board.piece_at(chess.E5),piecesValueBlack,pieceValueWhite,"e5",lateGame)
    value, piece_value = addValue(value,piece_value,valueT,piece_valueT)

    valueT,piece_valueT=getValuePosition(board.piece_at(chess.E6),piecesValueBlack,pieceValueWhite,"e6",lateGame)
    value, piece_value = addValue(value,piece_value,valueT,piece_valueT)

    valueT,piece_valueT=getValuePosition(board.piece_at(chess.E7),piecesValueBlack,pieceValueWhite,"e7",lateGame)
    value, piece_value = addValue(value,piece_value,valueT,piece_valueT)

    valueT,piece_valueT=getValuePosition(board.piece_at(chess.E8),piecesValueBlack,pieceValueWhite,"e8",lateGame)
    value, piece_value = addValue(value,piece_value,valueT,piece_valueT)


    #F
    valueT,piece_valueT=getValuePosition(board.piece_at(chess.F1),piecesValueBlack,pieceValueWhite,"f1",lateGame)
    value, piece_value = addValue(value,piece_value,valueT,piece_valueT)

    valueT,piece_valueT=getValuePosition(board.piece_at(chess.F2),piecesValueBlack,pieceValueWhite,"f2",lateGame)
    value, piece_value = addValue(value,piece_value,valueT,piece_valueT)

    valueT,piece_valueT=getValuePosition(board.piece_at(chess.F3),piecesValueBlack,pieceValueWhite,"f3",lateGame)
    value, piece_value = addValue(value,piece_value,valueT,piece_valueT)

    valueT,piece_valueT=getValuePosition(board.piece_at(chess.F4),piecesValueBlack,pieceValueWhite,"f4",lateGame)
    value, piece_value = addValue(value,piece_value,valueT,piece_valueT)

    valueT,piece_valueT=getValuePosition(board.piece_at(chess.F5),piecesValueBlack,pieceValueWhite,"f5",lateGame)
    value, piece_value = addValue(value,piece_value,valueT,piece_valueT)

    valueT,piece_valueT=getValuePosition(board.piece_at(chess.F6),piecesValueBlack,pieceValueWhite,"f6",lateGame)
    value, piece_value = addValue(value,piece_value,valueT,piece_valueT)

    valueT,piece_valueT=getValuePosition(board.piece_at(chess.F7),piecesValueBlack,pieceValueWhite,"f7",lateGame)
    value, piece_value = addValue(value,piece_value,valueT,piece_valueT)

    valueT,piece_valueT=getValuePosition(board.piece_at(chess.F8),piecesValueBlack,pieceValueWhite,"f8",lateGame)
    value, piece_value = addValue(value,piece_value,valueT,piece_valueT)

    #G
    valueT, piece_valueT = getValuePosition(board.piece_at(chess.G1),piecesValueBlack,pieceValueWhite,"g1",lateGame)
    value, piece_value = addValue(value,piece_value,valueT,piece_valueT)

    valueT,piece_valueT=getValuePosition(board.piece_at(chess.G2),piecesValueBlack,pieceValueWhite,"g2",lateGame)
    value, piece_value = addValue(value,piece_value,valueT,piece_valueT)

    valueT,piece_valueT=getValuePosition(board.piece_at(chess.G3),piecesValueBlack,pieceValueWhite,"g3",lateGame)
    value, piece_value = addValue(value,piece_value,valueT,piece_valueT)

    valueT,piece_valueT=getValuePosition(board.piece_at(chess.G4),piecesValueBlack,pieceValueWhite,"g4",lateGame)
    value, piece_value = addValue(value,piece_value,valueT,piece_valueT)

    valueT,piece_valueT=getValuePosition(board.piece_at(chess.G5),piecesValueBlack,pieceValueWhite,"g5",lateGame)
    value, piece_value = addValue(value,piece_value,valueT,piece_valueT)

    valueT,piece_valueT=getValuePosition(board.piece_at(chess.G6),piecesValueBlack,pieceValueWhite,"g6",lateGame)
    value, piece_value = addValue(value,piece_value,valueT,piece_valueT)

    valueT,piece_valueT=getValuePosition(board.piece_at(chess.G7),piecesValueBlack,pieceValueWhite,"g7",lateGame)
    value, piece_value = addValue(value,piece_value,valueT,piece_valueT)

    valueT,piece_valueT=getValuePosition(board.piece_at(chess.G8),piecesValueBlack,pieceValueWhite,"g8",lateGame)
    value, piece_value = addValue(value,piece_value,valueT,piece_valueT)

    #H
    valueT,piece_valueT=getValuePosition(board.piece_at(chess.H1),piecesValueBlack,pieceValueWhite,"h1",lateGame)
    value, piece_value = addValue(value,piece_value,valueT,piece_valueT)

    valueT,piece_valueT=getValuePosition(board.piece_at(chess.H2),piecesValueBlack,pieceValueWhite,"h2",lateGame)
    value, piece_value = addValue(value,piece_value,valueT,piece_valueT)

    valueT,piece_valueT=getValuePosition(board.piece_at(chess.H3),piecesValueBlack,pieceValueWhite,"h3",lateGame)
    value, piece_value = addValue(value,piece_value,valueT,piece_valueT)

    valueT,piece_valueT=getValuePosition(board.piece_at(chess.H4),piecesValueBlack,pieceValueWhite,"h4",lateGame)
    value, piece_value = addValue(value,piece_value,valueT,piece_valueT)

    valueT,piece_valueT=getValuePosition(board.piece_at(chess.H5),piecesValueBlack,pieceValueWhite,"h5",lateGame)
    value, piece_value = addValue(value,piece_value,valueT,piece_valueT)

    valueT,piece_valueT=getValuePosition(board.piece_at(chess.H6),piecesValueBlack,pieceValueWhite,"h6",lateGame)
    value, piece_value = addValue(value,piece_value,valueT,piece_valueT)

    valueT,piece_valueT=getValuePosition(board.piece_at(chess.H7),piecesValueBlack,pieceValueWhite,"h7",lateGame)
    value, piece_value = addValue(value,piece_value,valueT,piece_valueT)

    valueT,piece_valueT=getValuePosition(board.piece_at(chess.H8),piecesValueBlack,pieceValueWhite,"h8",lateGame)
    value, piece_value = addValue(value,piece_value,valueT,piece_valueT)

    return value,piece_value
