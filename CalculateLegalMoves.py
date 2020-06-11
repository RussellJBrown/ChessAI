import sys

def canKingMoveHere(Colour,KingSpace,OtherMoves):
    print("")
    for i in KingSpace:
        for x in i:
            print("")

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
        possible.append(tempX)
        possible.append(tempY)
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
        kingMove.append(possibleMove)
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
            possibleMoves.append(spaceY)
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
                validMove.append(possibleBy)
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
    while BishopX>0 and BishopY<8:
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

    while BishopX<8 and BishopY<8:
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

    while BishopX>0 and BishopY>0:
        validMove = []
        possibleBX = currentBishopX-1
        possibleBY = currentBishopY-1
        whatIsOnSquare = Board[possibleBX][possibleBY]
        if whatIsOnSquare == ".":
            validMove.append(possibleBX)
            validMove.append(possibleBy)
            validBishopMoves.append(validMove)
        else:
            break

    return validBishopMoves

def validKnight(KnightSpace,Board):
    #Code Knight Rules
    return False

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
        if BoardSpace[currentRookX][currentRookY]!=".":
            checkMove.append(currentRookX)
            checkMove.append(currentRookY)
            ValidRookMoves.append(checkMove)
        else:
            break

    while currentRookX2 < 0:
        currentRookX2-=1
        checkMove = []
        if BoardSpace[currentRookX2][currentRookY]!=".":
            checkMove.append(currentRookX2)
            checkMove.append(currentRookY)
            ValidRookMoves.append(checkMove)
        else:
            break

    while currentRookY > 7:
        currentRookY+=1
        checkMove = []
        if BoardSpace[currentRookX][currentRookY]!=".":
            checkMove.append(currentRookX)
            checkMove.append(currentRookY2)
            ValidRookMoves.append(checkMove)
            print("")
        else:
            break

    while currentRookY2 < 0:
        currentRookY2-=1
        if BoardSpace[currentRookX][currentRookY2]!="."
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



def check(Colour,recentMove,recentPiece,KingPosition,Board):

    if recentPiece == "Pawn":
        possiblePositions = validPawn(Colour,recentMove,Board)

    elif recentPiece == "Rook":
        possiblePositions = validRook(Colour,recentMove,Board)

    elif recentPiece == "Queen":
        possiblePositions = validQueen(Colour,recentMove,Board)

    elif recentPiece == "Bishop":
        possiblePositions = validBishop(Colour,recentMove,Board)

    possibleKingMoves = validKing(Colour,recentMove,Board)
    kingX = KingPosition[0]
    kingY = KingPosition[1]
    for positions in possiblePositions:
        possibleX = positions[0]
        possibleY = possibles[1]
        if possibleX == kingX and possibleY == kingY:
            final = checkmate()
            if final == True:
                print("Game is Finished")
                sys.exit()
            else:
                newBoard = movePiece()

    return newBoard




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



if __name__ == '__main__':
    Board = initialBoardStat()
    Colour = "White"
    validMoves = []
    whiteKing = []
    blackKing = []

    while(gameIsOn):
        for x in range(8):
            for y in range(8):
                currentSpace = Board[x][y]
                if currentSpace == "Pawn":
                    currentPawn = []
                    currentPawn.append(x)
                    currentPawn.append(y)
                    pawns = validPawn(Colour,currentPawn,Board)
                    validMoves.append(pawns)

                elif currentSpace == "Rook":
                    currentRook = []
                    currentRook.append(x)
                    currentRook.append(y)
                    rooks = validRook(Colour, currentRook,Board)
                    validMoves.append(rooks)

                elif currentSpace == "Bishop":
                    currentBishop = []
                    currentBishop.append(x)
                    currentBishop.append(y)
                    bishop = validBishop(Colour,currentBishop,Board)
                    validMoves.append(bishop)

                elif currentSpace == "Queen":
                    currentQueen = []
                    currentQueen.append(x)
                    currentQueen.append(y)
                    queen = validQueen(Colour,currentQueen,Board)
                    validMoves.append(queen)

                elif currentSpace == "Knight":
                    currentKnight = []
                    currentKnight.append(x)
                    currentKnight.append(y)
                    knight = validKnight(Colour,currentKnight,Board)
                    validMoves.append(knight)

                elif currentSpace == "WKing":
                    currentWKing = []
                    currentKing.append(x)
                    currentKing.append(y)
                    kingMoves = validKing(Colour,currentKing,Board)
                    whiteKing.append(kingMoves)

                elif currentSpace == "BKing":
                    currentKing = []
                    currentKing.append(x)
                    currentKing.append(y)
                    kingMoves = validKing(Colour, currentKing, Board)
                    blackKing.append(kingMoves)


        if Colour == "White":
            possibleMove = canKingMoveHere(Colour,whiteKing,validMoves)
            validMoves.append(possibleMove)
            Colour = "Black"

        elif Colour == "Black":
            possibleMove = canKingMoveHere(Colour,blackKing,validMoves)
            validMoves.append(possibleMove)
            Colour = "White"
