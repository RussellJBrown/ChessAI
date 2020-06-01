

def validKing(KingSpace,Board):
    #Code King
    return

def validQueen(QueenSpace,Board):
    #Code Queen
    return False

def validBishop(BishopSpace,Board):
    #Code Bishop
    return False

def validKnight(KnightSpace,Board):
    #Code Knight Rules
    return False

def validRook(Colour, RookSpace,Board):
    #Code Rook Rules

     #Can Move any space Vertically
     ValidRookMoves = []
     currentRookX = RookSpace[0]
     currentRookX2 = RookSpace[0]

     currentRookY = RookSpace[1]
     currentRookY2 = RookSpace[1]

     #Move Up White
    while currentRookX >7:
        currentRookX+=1
        if BoardSpace[currentRookX][currentRookY]!=".":
            print("")
        else:
            break

    while currentRookX2 < 0:
        currentRookX2-=1
        if BoardSpace[currentRookX2][currentRookY]!=".":
            print("")
        else:
            break

    while currentRookY > 7:
        currentRookY+=1
        if BoardSpace[currentRookX][currentRookY]!=".":
            print("")
        else:
            break

    while currentRookY2 < 0:
        print("")




    #Can Move any space Horizontally
    ValidRookMoves = []



    return False

def validPawn(Colour,PawnSpace,Board):
    #Code Pawn Rules
    ValidPawnMoves = []
    pawnCaptureXM1 = PawnSpace[0] - 1
    pawnCaptureXP1 = PawnSpace[0] + 1
    pawnCaptureY1 = PawnSpace[1] + 1


    #Normal Capture
    if Board[pawnCaptureXP1][pawnCaptureY1] != "." and pawnCaptureXP1>7:
        subMoves = []
        subMoves.append(pawnCaptureXP1)
        subMoves.append(pawnCaptureY1)
        ValidPawnMoves.append(subMoves)

    if Board[pawnCaptureXM1][pawnCaptureY1] != "." and pawnCaptureXM1<0:
        subMoves = []
        subMoves.append(pawnCaptureXM1)
        subMoves.append(pawnCaptureY1)
        ValidPawnMoves.append(subMoves)

    #Normal Movement
    if PawnSpace[1] != 1 and Colour == "White":
        subMoves = []
        subMoves.append(PawnSpace[0])
        subMoves.append(PawnSpace[1]+1)


    #Starting Movement White Pawn
    if PawnSpace[1] == 1 and Colour == "White":
        subMoves = []
        subMoves.append(PawnSpace[0])
        subMoves.append(PawnSpace[1]+1)
        ValidPawnMoves.append(subMoves)

        subMoves = []
        subMoves.append(PawnSpace[0])
        subMoves.append(PawnSpace[1]+2)
        ValidPawnMoves.append(subMoves)

    #En Passant
    if PawnSpace[1] = 5 and Colour == "White":
        xMinus1 = PawnSpace[0] + 1
        xPlus1 = PawnSpace[0] + 1
        ySpace = PawnSpace[1] + 1

        IsPawnP = BoardSpace[xMinus1][ySpace]
        IsPawnM = BoardSpace[xPlus1][ySpace]

        if IsPawnP.contains("BPawn"):
            subMoves = []
            subMoves.append(xPlus1)
            subMoves.append(ySpace)
            ValidPawnMoves.append(subMoves)

        if IsPawnM.contains("BPawn"):
            subMoves = []
            subMoves.append(xMinus1)
            subMoves.append(ySpace)
            ValidPawnMoves.append(subMoves)











    return False





def legalMoves(currentTurn,currentBoard):
    for j in range(8):
          for i in range(8):
              print (currentBoard[i][j])

def initialBoardStat():
    print("")
    w, h = 8, 8;
    chessBoard = [[0 for x in range(w)] for y in range(h)]
    chessBoard[0][0] = "WRook"
    chessBoard[1][0] = "WKnight"
    chessBoard[2][0] = "WBishop"
    chessBoard[3][0] = "WQueen"
    chessBoard[4][0] = "WKing"
    chessBoard[5][0] = "WBishop2"
    chessBoard[6][0] = "WKnight2"
    chessBoard[7][0] = "WRook2"

    chessBoard[0][1] = "WPawn"
    chessBoard[1][1] = "WPawn2"
    chessBoard[2][1] = "WPawn3"
    chessBoard[3][1] = "WPawn4"
    chessBoard[4][1] = "WPawn5"
    chessBoard[5][1] = "WPawn6"
    chessBoard[6][1] = "WPawn7"
    chessBoard[7][1] = "WPawn8"

    chessBoard[0][7] = "BRook"
    chessBoard[1][7] = "BKnight"
    chessBoard[2][7] = "BBishop"
    chessBoard[3][7] = "BQueen"
    chessBoard[4][7] = "BKing"
    chessBoard[5][7] = "BBishop2"
    chessBoard[6][7] = "BKnight2"
    chessBoard[7][7] = "BRook2"

    chessBoard[0][1] = "WPawn"
    chessBoard[1][1] = "WPawn2"
    chessBoard[2][1] = "WPawn3"
    chessBoard[3][1] = "WPawn4"
    chessBoard[4][1] = "WPawn5"
    chessBoard[5][1] = "WPawn6"
    chessBoard[6][1] = "WPawn7"
    chessBoard[7][1] = "WPawn8"

    chessBoard[0][6] = "BPawn"
    chessBoard[1][6] = "BPawn2"
    chessBoard[2][6] = "BPawn3"
    chessBoard[3][6] = "BPawn4"
    chessBoard[4][6] = "BPawn5"
    chessBoard[5][6] = "BPawn6"
    chessBoard[6][6] = "BPawn7"
    chessBoard[7][6] = "BPawn8"

    return chessBoard




def checkmate():
    if kingCheck == True:
        if noMoves == "True":
            return "Check Mate Game Over"

        if noMoves == "False":
            print("Do Best Move")



if __name__ == '__main__':
    startingBoard = initialBoardStat()
    legalMoves("White",startingBoard)
