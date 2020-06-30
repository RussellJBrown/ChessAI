



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
    currentListOfMoves = []
    bestMove = []
    i = 0
    Pawn = 1
    Knight = 3
    Bishop = 3
    Queen = 9
    King = 100

    while i!=5:
        for listofMoves in currentListOfMoves:
            xposition = listofMoves[0]
            yposition = listofMoves[1]
            position = board[xposition][yposition]
        i+=1

    bestMove.append(xposition)
    bestMove.append(yposition)
    bestMove.append(piece)

    return bestMove

#Simple decision AI
#Based off just the current state of the board
def evaluateBoardState(move,Board):

        currentScore = 0
        evalScore = 0
        bestMove = []
        moveX = move[0]
        moveY = move[1]

        currentPosition = Board[moveX][moveY]

        if currentPosition == "." and evalScore<currentScore:
            currentScore = 0


        elif currentPosition == "Pawn" and evalScore<currentScore:
            currentScore = 1

        elif currentPosition == "Knight" and evalScore<currentScore:
            currentScore = 3

        elif currentPosition == "Bishop" and evalScore<currentScore:
            currentScore = 3

        elif currentPosition == "Rook" and evalScore<currentScore:
            currentScore = 5

        elif currentPosition == "Queen" and evalScore<currentScore:
            currentScore = 9

        elif currentPosition == "King" and evalScore<currentScore:
            currentScore = 100


        return bestMove


def calculateBestMove(validPawns,validRooks,validKnights,validBishops,validQueen,validKing):

    bestMove = []
    bestMovePercentage = 0

    for move in range(validPawns):
        print(move)
    for move in range(validRooks):
        print(move)
    for move in range(validKnights):
        print(move)
    for move in range(validBishops):
        print(move)
    for move in range(validQueen):
        print(move)
    for move in range(validKing):
        print(move)

    return bestMove
