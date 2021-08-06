import chess
import sys
from riskRewardPath import *
import os
import random
import ast
from testEndGame import *
from OpeningSetup import *


def changeColour(currentColour):
        if currentColour == "White":
            currentColour = "Black"

        elif currentColour == "Black":
            currentColour = "White"

        return currentColour

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

#https://stackoverflow.com/questions/55650138/how-to-get-a-piece-in-python-chess
def getInputFromUser(board):
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
            #breakd

        else:
            print("Invalid Entry Please Try Again ")


        return selectedMove

if __name__ == '__main__':

    board = chess.Board()
    popularOpening = getOpeningList()
    computerColour, path = FirstSetUp()
    selectDiff = selectDiff()
    moveCount = 0
    inOpening = True
    movingList = []

    while (True):
        #This means it is your Turn
        if yourColour == currentColour:
            move = getInputFromUser(board)
            board.push_san(move)
            currentColour = changeColour(currentColour)
            if moveCount == 0:
                path = path+"/"+move
                movingList = os.listdir(path)
            if inOpening==True:
                movingList = updatedMoveList(move,movingList,path)
                if not movingList:
                    inOpening = False
                    print("Out of Opening")
            moveCount+=1

        #This means it is the computers turn
        elif yourColour != currentColour:
            if moveCount == 0:
                path = path+"/"+move
                movingList = os.listdir(path)

            if inOpening==True:
                print("Changed to Blacks turn")
                move, moveList = checkIfInOpen(moveCount,movingList)
                if move == "No Move":
                    isOpening=False
                    print("Out of Opening")
            if isOpening==False:
                print("Out of Opening")
                move = checkMovesRating(board,selectDiff,yourColour,computerColour)

            print("Below this line")
            print(move)
            board.push_san(move)
            currentColour = changeColour(currentColour)
            moveCount+=1

        isGameOver(board,currentColour)
