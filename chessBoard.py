import chess
import sys
from riskRewardPath import *
import os
import random
import ast
from testEndGame import *
from OpeningSetup import *

'''
currentColour: the current players colour

Changes the players colour
'''
def changeColour(currentColour):
        if currentColour == "White":
            currentColour = "Black"

        elif currentColour == "Black":
            currentColour = "White"

        return currentColour

'''
Not yet implemented
'''
def undoMove(Board):
    Board = Board.pop()
    return Board

'''
Prints the current board state
'''
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
        move = input()

       
        if move in bMoves:
            return move
       
        #Undo feature not implemented yet
        #if move == "Undo" or move == "undo" or move == "U" or move == "u":
        #    board = undoMove(board)
        #    currentColour = yourColour
        if move == "PB" or move == "pb" or move == "Pb" or move == "pB":
            printBoardValues()

        elif move == "Exit" or move == "Quit" or move == "exit" or move =="quit":
            sys.exit()


        elif move not in bMoves:
            print("Invalid Entry Please Try Again ")
            move = getInputFromUser(board)

        return move


if __name__ == '__main__':
    board = chess.Board()
    popularOpening = getOpeningList()
    yourColour, computerColour, path = FirstSetUp()
    diff = selectDiff()
    currentColour="White"
    moveCount = 0
    inOpening = True
    movingList = []
    openingMove = ""
    temppath=""
    move=""
    InFirstMove=True
    while (True):
        moveCount+=1
        print(board)
    

        #This means it is your Turn
        if yourColour == currentColour:
            print("User Turn")
            move = getInputFromUser(board)
            board.push_san(move)
            currentColour = changeColour(currentColour)
            if moveCount == 1:
                temppath = path+"/"+move
                openingMove = move
                # print("Checking If Move Count 1 reached")
                movingList = os.listdir(temppath)
                     
            if inOpening==True:
                # print("Printing out Move Out Move Count")
                # print(moveCount)
                movingList = updatedMoveList(str(moveCount)+move,movingList,temppath)            
                print(len(movingList))
                if not movingList:
                    inOpening = False
                    # print("Out of Opening")

        #This means it is the computers turn
        elif yourColour != currentColour:
            print("Computer Turn")                       
            if inOpening==True:
                move, moveList = checkIfInOpen(board,str(moveCount),movingList,path+"/"+openingMove)               
                if move == "No Move" or len(moveList)==0:          
                    inOpening=False
                       
            if inOpening==False:
                # print("Out of Opening")                                
                move = performTree(board,currentColour,computerColour,diff,0,movingList,"",0)
                

           
            
            board.push_san(move)
            currentColour = changeColour(currentColour)

        isGameOver(board,currentColour)

