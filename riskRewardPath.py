



#Creating a risk reward system
#Creating an evaluation Function








#King is worth 100
#Queen is worth 9
#Rook is worth 5
#Knight is worth 3
#Bishop is worth 3
#Pawn is worth 1



#Perform a move a find out next likely moves based off the move
def performTree(Colour, piece, currentScore, validMoveList,board):
    pass





#Simple decision AI
#Based off just the current state of the board
def evaluateBoardState(Colour,piece,currentScore,validMoveList,board):
    bestX = -1
    bestY = -1
    currentScore = -1
    bestMove = []
    for moveList in validMoveList:
        xMoveList = moveList[0]
        yMoveList = moveList[1]
        isPiece = board[xMoveList][yMoveList]

        if isPiece == "Pawn" and 1<currentScore:
            currentScore=1
            bestX = xMoveList
            bestY = yMoveList

        elif isPiece == "Bishop" and 3<currentScore:
            currentScore = 3
            bestX = xMoveList
            bestY = yMoveList

        elif isPiece == "Knight" and 3<currentScore:
            currentScore = 3
            bestX = xMoveList
            bestY = yMoveList

        elif isPiece == "Queen" and 9<currentScore:
            currentScore = 9
            bestX = xMoveList
            bestY = yMoveList

        elif isPiece == "King" and 100<currentScore:
            currentScore = 100
            bestX = xMoveList
            bestY = yMoveList

    bestMove.append(bestX)
    bestMove.append(bestY)
    bestMove.append(currentScore)
    return bestMove
