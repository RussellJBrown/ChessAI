import sys
import chess
import random

#Creating a risk reward system
#Creating an evaluation Function

#King is worth 100
#Queen is worth 9
#Rook is worth 5
#Knight is worth 3
#Bishop is worth 3
#Pawn is worth 1
#Perform a move a find out next likely moves based off the move
def calculateMoveValue(board,move,selectDiff,currentDepth):

    #Indicates that a capture has occured
    if "x" in move:
        #Determine what piece is being picked
        return 1

    #Indicates that check can occur
    if "+" in move:
        return 5

    #Indicates that checkmate can occur
    if "#" in move:
        return 10000000

    #Indicates that Castling on King Side
    if "0-0" == move:
        return 10

    #Indicates Castling on Queen Side
    if "0-0-0" == move:
        return 10

    else:
        if currentDepth < selectDiff:
            #Need to Update Move List Calculate Best Move for Player so it Could be Countered
            board.push_san(move)
            moveList = getMoveList(board)
            for move in moveList:
                return calculateMoveValue(board,move,selectDiff,currentDepth+1)


        else:
            #Currently returning 0 if no Captures or special move can occur.
            return 0

#Board is the Current Boards State
#allComputerMoves is the list of all valid moves in current state
#selectDiff int used to perform diff depth
def performTree(board,allComputerMoves,selectDiff):
    print("Perform Tree")
    futureBoard = board
    bestMove = allComputerMoves[0]
    highestValue = -10000000
    for move in allComputerMoves:
        #futureBoard.push_san(move)
        currentDepth = 0
        value = calculateMoveValue(futureBoard,move,selectDiff,currentDepth)
        if value > highestValue:
            highestValue = value
            bestMove = move

    return bestMove


def checkMovesRating(board,selectDiff):
    print("Make Computer Move")
    allComputerMoves = getMoveList(board)
    #return performTree(board,allComputerMoves,selectDiff)
    return random.choice(allComputerMoves)


def getMoveList(board):
    moves = board.legal_moves
    moves = str(moves)
    split_string = moves.split("(")
    split_string2 = split_string[1].split(")")
    allComputerMoves = split_string2[0].split(", ")
    return allComputerMoves


def startingOpening(board):
    print("Computer Does Starting Opening")
