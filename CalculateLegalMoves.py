import sys
from riskRewardPath import *

def validKing(Colour, KingSpace, Board):
    currentKingX = KingSpace[0]
    currentKingY = KingSpace[1]
    kingMoves = []
    #X+1
    tempX = currentKingX+1
    tempY = currentKingY

    currentSpace = Board[tempX][tempY]
    if currentSpace == ".":
        possibleMove = []
        possibleMove.append(tempX)
        possibleMove.append(tempY)
        kingMoves.append(possibleMove)

    #X-1
    tempX = currentKingX-1
    tempY = currentKingY
    currentSpace = Board[tempX][tempY]
    if currentSpace == ".":
        possibleMove = []
        possibleMove.append(tempX)
        possibleMove.append(tempY)
        kingMoves.append(possibleMove)

    #Y+1
    tempX = currentKingX
    tempY = currentKingY+1
    currentSpace = Board[tempX][tempY]
    if currentSpace == ".":
        possibleMove = []
        possibleMove.append(tempX)
        possibleMove.append(tempY)
        kingMoves.append(possibleMove)

    #Y-1
    tempX = currentKingX
    tempY = currentKingY - 1
    currentSpace = Board[tempX][tempY]
    if currentSpace == ".":
        possibleMove = []
        possibleMove.append(tempX)
        possibleMove.append(tempY)
        kingMoves.append(possibleMove)


    #X+1 Y+1
    tempX = currentKingX + 1
    tempY = currentKingY + 1
    currentSpace = Board[tempX][tempY]
    if currentSpace == ".":
        possibleMove = []
        possibleMove.append(tempX)
        possibleMove.append(tempY)
        kingMoves.append(possibleMove)

    #X+1 Y-1
    tempX = currentKingX + 1
    tempY = currentKingY - 1
    currentSpace = Board[tempX][tempY]
    if currentSpace == ".":
        possibleMove = []
        possibleMove.append(tempX)
        possibleMove.append(tempY)
        kingMoves.append(possibleMove)

    #X-1 Y+1
    tempX = currentKingX-1
    tempY = currentKingY+1
    currentSpace = Board[tempX][tempY]
    if currentSpace == ".":
        possibleMove =  []
        possibleMove.append(tempX)
        possibleMove.append(tempY)
        kingMoves.append(possibleMove)



    #X-1 Y-1
    tempX = currentKingX-1
    tempY = currentKingY-1
    currentSpace = Board[tempX][tempY]
    if currentSpace == ".":
        possibleMove = []
        possibleMove.append(tempX)
        possibleMove.append(tempY)
        possibleMove.append(possibleMove)
    #Code King
    return currentSpace

def validQueen(Colour,QueenSpace,Board):
    SpaceX = QueenSpace[0]
    SpaceX2 = QueenSpace[0]
    SpaceY = QueenSpace[1]
    SpaceY2 = QueenSpace[1]
    validQueenMoves = []
    #Moving Vertically
    while SpaceX>0:
        possibleMoves = []
        SpaceX -= 1
        whatIsOnSquare = Board[SpaceX][SpaceY]
        if whatIsOnSquare == ".":
                possibleMoves.append(SpaceX)
                possibleMoves.append(SpaceY)
                validQueenMoves.append(possibleMoves)
        else:
            #Add test to capture or invalid move
            pass

    while SpaceX<7:
        possibleMoves = []
        SpaceX += 1
        whatIsOnSquare = Board[SpaceX][SpaceY]
        if whatIsOnSquare == ".":
            possibleMoves.append(SpaceX)
            possibleMoves.append(SpaceY)
            validQueenMoves.append(possibleMoves)
        else:
            #Add test to capture or invalid
            pass

    #Moving Horizontally
    while SpaceY>0:
        possibleMoves = []
        SpaceY -= 1
        whatIsOnSquare = Board[SpaceX][SpaceY]
        if whatIsOnSquare == ".":
            possibleMoves.append(SpaceX)
            possibleMoves.append(SpaceY)
            validQueenMoves.append(possibleMoves)
        else:
            #Add test to capture or invalid
            pass

    while SpaceY<7:
        possibleMoves = []
        SpaceY += 1
        whatIsOnSquare = Board[SpaceX][SpaceY]
        if whatIsOnSquare == ".":
            possibleMoves.append(SpaceX)
            possibleMoves.append(SpaceY)
            validQueenMoves.append(possibleMoves)
        else:
            #Add test to capture
            pass

    #Moving Diagonal
        while SpaceX<8 and SpaceY>0:
            validMove = []
            possibleBX = SpaceX+1
            possibleBY = SpaceY-1
            whatIsOnSquare = Board[possibleBX][possibleBY]
            if whatIsOnSquare == ".":
                validMove.append(possibleBX)
                validMove.append(possibleBY)
                validQueenMoves.append(validMove)
            else:
                #If Black Possible Movement
                #If White No Movement
                break

            print("")
        while SpaceX>0 and SpaceY<8:
            validMove = []
            possibleX = SpaceX-1
            possibleY = SpaceY+1
            whatIsOnSquare = Board[possibleX][possibleY]
            if whatIsOnSquare == ".":
                validMove.append(possibleX)
                validMove.append(possibleY)
                validQueenMoves.append(validMove)
            else:
                #If Black Possible Movement
                #If White Possible No Movement
                break

        while SpaceX<8 and SpaceY<8:
            validMove = []
            possibleX = SpaceX+1
            possibleY = SpaceY+1
            whatIsOnSquare = Board[possibleX][possibleY]
            if whatIsOnSquare == ".":
                validMove.append(possibleX)
                validMove.append(possibleY)
                validQueenMoves.append(validMove)
            else:
                #If Black Possible Movement
                #If White Possible No Movement
                break

        while SpaceX>0 and SpaceY>0:
            validMove = []
            possibleX = SpaceX-1
            possibleY = SpaceY-1
            whatIsOnSquare = Board[possibleBX][possibleBY]
            if whatIsOnSquare == ".":
                validMove.append(possibleBX)
                validMove.append(possibleBY)
                validQueenMoves.append(validMove)
            else:
                    #If Black Possible Movement
                    #If White Possible No Movement
                break

    return validQueenMoves

def validBishop(Colour, BishopSpace, Board):
    #Code Bishop
    validBishopMoves = []
    currentBishopX = BishopSpace[0]
    currentBishopX2 = BishopSpace[0]
    currentBishopY = BishopSpace[1]
    currentBishopY2 = BishopSpace[1]

    while currentBishopX<8 and currentBishopY>0:
        validMove = []
        possibleBX = currentBishopX+1
        possibleBY = currentBishopY-1
        whatIsOnSquare = Board[possibleBX][possibleBY]
        if whatIsOnSquare == ".":
            validMove.append(possibleBX)
            validMove.append(possibleBY)
            validBishopMoves.append(validMove)
        else:
            #If Black Possible Movement
            #If White No Movement
            break

        print("")

    while currentBishopX>0 and currentBishopY<8:
        validMove = []
        possibleBX = currentBishopX-1
        possibleBY = currentBishopY+1
        whatIsOnSquare = Board[possibleBX][possibleBY]
        if whatIsOnSquare == ".":
            validMove.append(possibleBX)
            validMove.append(possibleBY)
            validBishopMoves.append(validMove)
        else:
            #If Black Possible Movement
            #If White Possible No Movement
            break

    while currentBishopX<8 and currentBishopY<8:
        validMove = []
        possibleBX = currentBishopX+1
        possibleBY = currentBishopY+1
        whatIsOnSquare = Board[possibleBX][possibleBY]
        if whatIsOnSquare == ".":
            validMove.append(possibleBX)
            validMove.append(possibleBY)
            validBishopMoves.append(validMove)
        else:
            #If Black Possible Movement
            #If White Possible No Movement
            break

    while currentBishopX>0 and currentBishopY>0:
        validMove = []
        possibleBX = currentBishopX-1
        possibleBY = currentBishopY-1
        whatIsOnSquare = Board[possibleBX][possibleBY]
        if whatIsOnSquare == ".":
            validMove.append(possibleBX)
            validMove.append(possibleBY)
            validBishopMoves.append(validMove)
        else:
            break

    return validBishopMoves

def validKnight(Colour,KnightSpace,Board):

    cKX = KnightSpace[0]
    cKY = KnightSpace[1]
    possibleKnightMoves = []

    #Move More Up and Down
    tempX = cKX+1
    tempY = cKY+2
    if tempX<8 and tempX>0 and tempY>0 and tempY<8:
        pMove = []
        pMove.append(tempX)
        pMove.append(tempY)
        possibleKnightMoves.append(possibleKnightMoves)

    tempX = cKX-1
    tempY = cKY+2
    if tempX<8 and tempX>0 and tempY>0 and tempY<8:
        pMove = []
        pMove.append(tempX)
        pMove.append(tempY)
        possibleKnightMoves.append(pMove)

    tempX = cKX + 1
    tempY = cKY - 2
    if tempX<8 and tempX>0 and tempY>0 and tempY<8:
        pMove = []
        pMove.append(tempX)
        pMove.append(tempY)
        possibleKnightMoves.append(pMove)

    tempX = cKX  - 1
    tempY = cKY - 2
    if tempX<8 and tempX>0 and tempY>0 and tempY<8:
        pMove = []
        pMove.append(tempX)
        pMove.append(tempY)
        possibleKnightMoves.append(pMove)

    #Move more Horizontally
    tempX = cKX+2
    tempY = cKY+1
    if tempX<8 and tempX>0 and tempY>0 and tempY<8:
        pMove = []
        pMove.append(tempX)
        pMove.append(tempY)
        possibleKnightMoves.append(pMove)

    tempX = cKX + 2
    tempY = cKX - 1
    if tempX<8 and tempX>0 and tempY>0 and tempY<8:
        pMove = []
        pMove.append(tempX)
        pMove.append(tempY)
        possibleKnightMoves.append(pMove)

    tempX = cKX - 2
    tempY = cKY + 1
    if tempX<8 and tempX>0 and tempY>0 and tempY<8:
        pMove = []
        pMove.append(tempX)
        pMove.append(tempY)
        possibleKnightMoves.append(pMove)

    tempX = cKX - 2
    tempY = cKY - 1
    if tempX<8 and tempX>0 and tempY>0 and tempY<8:
        pMove = []
        pMove.append(tempX)
        pMove.append(tempY)
        possibleKnightMoves.append(pMove)
    return possibleKnightMoves

def validRook(Colour, RookSpace,Board):
 #Can Move any space Vertically
    ValidRookMoves = []
    currentRookX = RookSpace[0]
    currentRookX2 = RookSpace[0]
    currentRookY = RookSpace[1]
    currentRookY2 = RookSpace[1]
     #Move Up White
    while currentRookX >7:
        currentRookX+=1
        checkMove = []
        if Board[currentRookX][currentRookY]!=".":
            checkMove.append(currentRookX)
            checkMove.append(currentRookY)
            ValidRookMoves.append(checkMove)
        else:
            break

    while currentRookX2 < 0:
        currentRookX2-=1
        checkMove = []
        if Board[currentRookX2][currentRookY]!=".":
            checkMove.append(currentRookX2)
            checkMove.append(currentRookY)
            ValidRookMoves.append(checkMove)
        else:
            break

    while currentRookY > 7:
        currentRookY+=1
        checkMove = []
        if Board[currentRookX][currentRookY]!=".":
            checkMove.append(currentRookX)
            checkMove.append(currentRookY2)
            ValidRookMoves.append(checkMove)
            print("")
        else:
            break

    while currentRookY2 < 0:
        currentRookY2-=1
        if Board[currentRookX][currentRookY2]!=".":
            checkMove.append(currentRookX)
            checkMove.append(currentRookY2)
            ValidRookMoves.append(checkMove)
        else:
            break

    return ValidRookMoves

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
    if PawnSpace[1] == 5 and Colour == "White":
        xMinus1 = PawnSpace[0] + 1
        xPlus1 = PawnSpace[0] + 1
        ySpace = PawnSpace[1] + 1

        IsPawnP = Board[xMinus1][ySpace]
        IsPawnM = Board[xPlus1][ySpace]

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

    return ValidPawnMoves

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

def checkmate(validKingMoves,KingSpace,Board):
    for kMoves in validKingMoves:
        kX = kMoves[0]
        kY = kMoves[1]
        validMoves = legalMoves()
        for valMove in validMoves:
            vX = valMove[0]
            vY = valMove[1]

            #Not CheckMate
            if vX != kX and vY != kY:
                break

        return True


def check(Colour,WKing,BKing,Board):
    check = False

    WKingX = WKing[0]
    WKingY = WKing[1]

    BKingX = BKing[0]
    BKingY = BKing[1]

    xW = WKingX
    xB = BKingX

    #Rook Comparison
    while xW!=8 and check==False:
       xW += 1
       space = Board[xW][WKingY]
       if space == "BRook" or space == "BQueen":
            check = True
            break

    while xB!=8 and check==False:
        xB += 1
        space = Board[xB][BKingY]
        if space == "WRook" or space == "WQueen":
            check = True
            break

    xW = WKingX
    xB = BKingX
    while xW!=0 and check==False:
        xW-=1
        space = Board[xW][WKingY]
        if space == "BRook" or space == "BQueen":
            check = True
            break

    while xB!=0 and check==False:
        xB -= 1
        space = Board[xW][WKingY]
        if space == "BRook" or space == "BQueen":
            check = True
            break

    yW = WKingY
    yB = BKingY
    while yW!=8 and check==False:
            yW += 1
            space = Board[WKingX][yW]
            if space == "WRook" or space == "WQueen":
                check = True
                break

    while yB!=8 and check==False:
        yB += 1
        space = Board[BKingY][yB]
        if space == "WRook" or space == "WQueen":
            check = True
            break


    yW = WKingY
    yB = BKingY
    while yB!=0 and check==False:
        yB -= 1
        space = Board[WKingY][yB]
        if space == "WRook" and space == "WQueen":
            check = True
            break

    while yW!=0 and check==False:
        yB -= 1
        space = Board[BKingX][yB]
        if space == "BRook" and space == "BQueen":
            check = True
            break


    #Checks if Whites Move is invalid and puts white into Check
    if Colour == "W" and whiteCheck == True:
        return False

    elif Colour == "B" and blackCheck == True:
        return False

    elif Colour == "W" and blackCheck == True:
        return True

    elif Colour == "B" and whiteCheck == True:
        return False



def movePiece(Board,bestMove):
    pX = bestMove[0]
    pY = bestMove[1]
    cX = bestMove[0]
    cY = bestMove[1]

    Piece = Board[pX][pY]
    Colour = Piece[0]
    if Colour == "W":
        Board[cX][cY] = "."
        Board[pX][pY] = Piece
    else:
        Board[cX][cY] = "."
        Board[pX][pY] = Piece

def promote(Colour,pawnPosition,Board):
    if Colour == "White":
        xP = pawnPosition[0]
        yP = pawnPosition[1]
        Board[xP][yP] = "WQueen"

    else:
        xP = pawnPosition[0]
        yP = pawnPosition[1]
        Board[xP][yP] = "BQueen"

    return Board

def legalMoves(Colour,KingSpace,QueenSpace,BishopSpace,RookSpace,PawnSpace,Board):
    legalMoves = []
    vKing  = validKing(Colour,KingSpace,Board)
    vQueen = validQueen(Colour,QueenSpace,Board)
    vBishop = validBishop(Colour,BishopSpace,Board)
    vRook = validRook(Colour,RookSpace,Board)
    vPawn = validPawn(Colour,PawnSpace,Board)
    legalMoves.append("King")
    legalMoves.append(vKing)
    legalMoves.append("Queen")
    legalMoves.append(vQueen)
    legalMoves.append("Bishop")
    legalMoves.append(vBishop)
    legalMoves.append("Rook")
    legalMoves.append(vRook)
    legalMoves.append("Pawn")
    legalMoves.append(vPawn)

def whileGameIsOn(Colour,Board):
    validMoves = []
    validPawns = []
    validRooks = []
    validPawns = []
    validKnights = []
    validBishops = []
    validQueen = []
    validKing = []

    WKing = []
    BKing = []

    for x in range(8):
        for y in range(8):
            currentSpace = Board[x][y]
            currentSpace = Colour + currentSpace[1:]

            if currentSpace == "WPawn":
                currentPawn = []
                currentPawn.append(x)
                currentPawn.append(y)
                pawns = validPawn(Colour, currentPawn, Board)
                validPawns.append(pawns)

            elif currentSpace == "BPawn":
                currentPawn = []
                currentPawn.append(x)
                currentPawn.append(y)
                pawns = validPawn(Colour, currentPawn, Board)
                validPawns.append(pawns)

            elif currentSpace == "WRook":
                currentRook = []
                currentRook.append(x)
                currentRook.append(y)
                rooks = validRook(Colour, currentRook, Board)
                validRooks.append(rooks)

            elif currentSpace == "BRook":
                currentRook = []
                currentRook.append(x)
                currentRook.append(y)
                rooks = validRook(Colour, currentRook, Board)
                validRooks.append(rooks)

            if currentSpace == "WKnight":
                currentKnight.append(x)
                currentKnight.append(y)
                knight = validKnight(Colour, currentKnight, Board)
                validKnights.append(knight)

            elif currentSpace == "BKnight":
                currentKnight = []
                currentKnight.append(x)
                currentKnight.append(y)
                knight = validKnight(Colour, currentKnight, Board)
                validMoves.append(knight)

            elif currentSpace == "WBishop":
                bishop = []
                currentBishop.append(x)
                currentBishop.append(y)
                bishop = validBishop(Colour, currentBishop, Board)
                validBishops.append(bishop)

            elif currentSpace == "BBishop":
                currentBishop = []
                currentBishop.append(x)
                currentBishop.append(y)
                bishop = validBishop(Colour, currentBishop, Board)
                validBishops.append(bishop)

            elif currentSpace == "WQueen":
                currentQueen = []
                currentQueen.append(x)
                currentQueen.append(y)
                queen = validQueen(Colour, currentQueen, Board)
                validQueen.append(queen)

            elif currentSpace == "BQueen":
                currentQueen = []
                currentQueen.append(x)
                currentQueen.append(y)
                queen = validQueen(Colour, currentQueen, Board)
                validMoves.append(queen)

            elif currentSpace == "WKing":
               WKing.append(x)
               WKing.append(y)
               WKing = validKing(Colour,WKing,Board)
               validKing.append(WKing)

            elif currentSpace == "BKing":
               BKing.append(x)
               BKing.append(x)
               BKing = validKing(Colour,BKing,Board)
               validKing.append(BKing)


    bestMove = calculateBestMove(validPawns,validRooks,validKnights,validBishops,validQueen,validKing)
    Board = movePiece(Board,bestMove)

    if "W" == Colour:
        Colour = "B"

    elif "B" == Colour:
        Colour = "W"

    whileGameIsOn(Colour,Board)



if __name__ == '__main__':
    Board = initialBoardStat()
    Colour = "White"
    whileGameIsOn(Colour,Board)


