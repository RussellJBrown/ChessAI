import chess
import sys
from riskRewardPath import *

def checkmate(board,currentColour):
    checkmate = board.is_checkmate()
    if checkmate == True:
        print(currentColour + " is the Winner")
        sys.exit()

def stalemate(board):
    stalemate = board.is_stalemate()
    if stalemate == True:
        print("Stalemate Game is a Draw")
        sys.exit()

def insufficient(board):
    insufficient = board.is_insufficient_material()
    if insufficient == True:
        print("The game is a draw by insufficient material")
        sys.exit()

def threeFoldRep(board):
    threeRep = board.can_claim_threefold_repetition()
    if threeRep == True:
        print("Draw by Repition")
        sys.exit()

def fiftyMoveNoCap(board):
    noCap = board.can_claim_fifty_moves()
    if noCap == True:
        print("No Capture in 50 moves, Game is a Draw")
        sys.exit()

def isGameOver(board,currentColour):
    checkmate(board,currentColour)
    stalemate(board)
    insufficient(board)
    threeFoldRep(board)
    gameOver = board.is_game_over()
    if gameOver == True:
        print("Game Over for a different reason")
        print("Add Reason Later")
        sys.exit()
    return False

def selectColour():
    print("Would you prefer to be White or Black?")
    x = ""
    yourColour = ""
    while(True):
        x = input()
        if x == "B":
            yourColour = "Black"
            break

        elif x == "b":
            yourColour = "Black"
            break

        elif x == "Black":
            yourColour = "Black"
            break

        elif x == "black":
            yourColour = "Black"
            break

        elif x == "W":
            yourColour = "White"
            break

        elif x == "w":
            yourColour = "White"
            break

        elif x =="White":
            yourColour = "White"
            break

        elif x == "white":
            yourColour = "White"
            break

        print("Invalid entry try again")


    return yourColour

def changeColour(currentColour):
        if currentColour == "White":
            currentColour = "Black"

        elif currentColour == "Black":
            currentColour = "White"

        return currentColour

def selectDiff():
    while(True):
        print("Select a Number between 1 - 10 for Computer Level")
        x = input()
        x = int(x)
        if x >= 1 and x<=10:
            return x
        print("Invalid entry")

def undoMove(Board):
    Board = Board.pop()
    return Board

def printBoardValues():
    alphaBoard = ["a","b","c","d","e","f","g","h"]
    numBoard = ["8","7","6","5","4","3","2","1"]
    for i in numBoard:
        print("")
        for j in alphaBoard:
                print(i+j ,end=" ")
    print("")


def getInputFromUser(board):

    selectedMove = ""
    while(True):
        print(board)
        print("")
        print("Enter one of these moves")
        bMoves = getMoveList(board)
        print(bMoves)
        print("")
        print("Undo Previous Moves By Typing: 'Undo' ")
        print("")
        print("To see board values type: 'PB'")
        move = input()

        #Undo feature not implemented yet
        #if move == "Undo" or move == "undo" or move == "U" or move == "u":
        #    board = undoMove(board)
        #    currentColour = yourColour
        if move == "PB" or move == "pb" or move == "Pb" or move == "pB":
            printBoardValues()

        elif move == "Exit" or move == "Quit" or move == "exit" or move =="quit":
            sys.exit()


        elif move in bMoves:
            selectedMove = move
            break

        else:
            print("Invalid Entry Please Try Again ")


    return selectedMove


if __name__ == '__main__':

    board = chess.Board()
    print("Starting Chess Game")
    print("")
    currentColour = "White"
    yourColour = selectColour()
    selectDiff = selectDiff()

    while (True):
        #This means it is your Turn
        if yourColour == currentColour:
            move = getInputFromUser(board)
            board.push_san(move)
            currentColour = changeColour(currentColour)

        #This means it is the computers turn
        elif yourColour != currentColour:
            move = checkMovesRating(board,selectDiff)
            board.push_san(move)
            currentColour = changeColour(currentColour)


        checkmate(board,currentColour)
        stalemate(board)
        insufficient(board)
        threeFoldRep(board)
        fiftyMoveNoCap(board)
        isGameOver(board)
