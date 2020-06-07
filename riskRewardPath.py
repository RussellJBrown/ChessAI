



#Creating a risk reward system
#Creating an evaluation Function



#King is worth 100
#Queen is worth 9
#Rook is worth 5
#Knight is worth 3
#Bishop is worth 3
#Pawn is worth 1
def evaluateBoardState(Colour,piece,currentScore,validMoveList,board):
    for moveList in validMoveList:
        xMoveList = moveList[0]
        yMoveList = moveList[1]
        isPiece = board[xMoveList][yMoveList]
        if isPiece == "Pawn":
            currentScore+=1
        elif isPiece == "Bishop":
            currentScore+=3
        elif isPiece == "Knight":
            currentScore+=3
        elif isPiece == "Queen":
            currentScore+=9
        elif isPiece == "King":
            currentScore+=100
        
