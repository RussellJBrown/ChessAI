import os
import ast
import random
import sys


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


def selectDiff():
    while(True):
        print("Select a Number between 1 - 10 for Computer Level")
        x = input()
        x = int(x)
        if x >= 1 and x<=10:
            return x
        print("Invalid entry")

def getOpeningList():
    moveList = []
    moveList.append('a3')
    moveList.append('a4')
    moveList.append('b3')
    moveList.append('b4')
    moveList.append('c3')
    moveList.append('c4')
    moveList.append('d3')
    moveList.append('d4')
    moveList.append('e3')
    moveList.append('e4')
    moveList.append('f3')
    moveList.append('f4')
    moveList.append('g3')
    moveList.append('g4')
    moveList.append('h3')
    moveList.append('h4')
    moveList.append('Na3')
    moveList.append('Nc3')
    moveList.append('Nf3')
    moveList.append('Nh3')
    return moveList

def getMoveList(board):
    moves = board.legal_moves
    moves = str(moves)
    split_string = moves.split("(")
    split_string2 = split_string[1].split(")")
    allComputerMoves = split_string2[0].split(", ")
    sortedMoveList = [None]*1
    for i in allComputerMoves:
        if '#' in i:
            sortedMoveList[0]=i
            return sortedMoveList
    return allComputerMoves

'''
board: The current Board of the game
moveCount: The current move count of the game
openinglists: the list of all the possible opening still viable
path: current path used to find the opening data


This method checks for the computer

'''
def checkIfInOpen(board,moveCount,openinglists,path):
   CurrentComputerMoves = getMoveList(board)
   possibleMovesForPlayer = []
   lists=[]
   openingMove = "No Move"
   for i in openinglists:
       file = open(path+"/"+i,"r")
       contents= file.read()
       dictionary = ast.literal_eval(contents)
       for possibleMoves in CurrentComputerMoves:          
           if moveCount+possibleMoves in dictionary:
                possibleMovesForPlayer.append(possibleMoves)           
   try:
      openingMove = random.choice(possibleMovesForPlayer)
   except Exception as e:
        print(e)  

   if openingMove != "No Move":
     lists = remove(moveCount+openingMove,openinglists,path)
   
   return openingMove, lists

def remove(move,list,path):
    for i in list:
        file = open(path+"/"+i,"r")
        contents = file.read()
        dictionary = ast.literal_eval(contents)
        if move not in dictionary:
            list.remove(i)

    return list


#Checking if in Opening for the Player
def updatedMoveList(move,list,path):
   for i in list:
       file = open(path+"/"+i,"r")
       contents= file.read()
       dictionary = ast.literal_eval(contents) 
       if move not in dictionary:
             list.remove(i)
   
   


   return list


def FirstSetUp():
        print("Starting Chess Game")
        print("")
        currentColour = "White"
        yourColour = selectColour()
        computerColour=""
        path = os.getcwd()
        if yourColour == "White":
            computerColour = "Black"
        else:
            computerColour= "White"
        return yourColour,computerColour, path