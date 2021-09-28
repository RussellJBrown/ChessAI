import chess
import sys
from riskRewardPath import *
import os
import random
import ast
from testEndGame import *
from OpeningSetup import *
from getBoardValue import BoardValue
import time



Capture="Capture"
Move="Move"
Promote="Promote"
Captured="Captured"
White="White"
Black="Black"
CheckMate = "#"
Check="+"
Promotion="="
Capturing="x"


class BoardValues():
    def __init__(self):
        self.whitePawn = {"a1": 0, "a2": 0, "a3": 2, "a4": 4, "a5": 8, "a6": 12, "a7": 20, "a8": 0, "b1": 0, "b2": 0, "b3": 2, "b4": 6, "b5": 10, "b6": 14, "b7": 26, "b8": 0, "c1": 0, "c2": 0, "c3": 4, "c4": 8, "c5": 12, "c6": 16, "c7": 26, "c8": 0, "d1": 0, "d2": -4, "d3": 6, "d4": 14, "d5": 18, "d6": 21, "d7": 28, "d8": 0, "e1": 0, "e2": -4, "e3": 6, "e4": 16, "e5": 18, "e6": 21, "e7": 28, "e8": 0, "f1": 0, "f2": 0, "f3": 4, "f4": 8, "f5": 12, "f6": 16, "f7": 26, "f8": 0, "g1": 0, "g2": 0, "g3": 2, "g4": 6, "g5": 12, "g6": 14, "g7": 26, "g8": 0, "h1": 0, "h2": 0, "h3": 2, "h4": 4, "h5": 8, "h6": 12, "h7": 20, "h8": 0}
        self.blackPawn = {"a1": 0, "a2": -20, "a3": -12, "a4": -8, "a5": -4, "a6": -2, "a7": 0, "a8": 0, "b1": 0, "b2": -26, "b3": -14, "b4": -10, "b5": -6, "b6": -2, "b7": 0, "b8": 0, "c1": 0, "c2": -26, "c3": -16, "c4": -12, "c5": -8, "c6": -4, "c7": 0, "c8": 0, "d1": 0, "d2": -28, "d3": -21, "d4": -18, "d5": -16, "d6": -6, "d7": 4, "d8": 0, "e1": 0, "e2": -28, "e3": -21, "e4": -18, "e5": -16, "e6": -6, "e7": 4, "e8": 0, "f1": 0, "f2": -26, "f3": -16, "f4": -12, "f5": -8, "f6": -4, "f7": 0, "f8": 0, "g1": 0, "g2": -26, "g3": -14, "g4": -10, "g5": -6, "g6": -2, "g7": 0, "g8": 0, "h1": 0, "h2": -20, "h3": -12, "h4": -8, "h5": -4, "h6": -2, "h7": 0, "h8": 0}

        self.whiteBishop = {"a1": -50, "a2": 0, "a3": 0, "a4": 0, "a5": 0, "a6": 0, "a7": 0, "a8": -40, "b1": -20, "b2": 5, "b3": 0, "b4": 5, "b5": 10, "b6": 10, "b7": 5, "b8": -20, "c1": -10, "c2": 0, "c3": 5, "c4": 10, "c5": 10, "c6": 10, "c7": 5, "c8": -15, "d1": -20, "d2": 0, "d3": 5, "d4": 18, "d5": 18, "d6": 18, "d7": 5, "d8": -15, "e1": -20, "e2": 0, "e3": 5, "e4": 18, "e5": 18, "e6": 18, "e7": 5, "e8": -15, "f1": -10, "f2": 0, "f3": 5, "f4": 10, "f5": 10, "f6": 10, "f7": 5, "f8": -15, "g1": -20, "g2": 5, "g3": 0, "g4": 5, "g5": 10, "g6": 10, "g7": 0, "g8": -20, "h1": -50, "h2": 0, "h3": 0, "h4": 0, "h5": 0, "h6": 0, "h7": 0, "h8": -40}
        self.blackBishop = {"a1": 40, "a2": 0, "a3": 0, "a4": 0, "a5": 0, "a6": 0, "a7": 0, "a8": 50, "b1": 20, "b2": -5, "b3": -10, "b4": -10, "b5": -5, "b6": 0, "b7": -5, "b8": 20, "c1": 15, "c2": -5, "c3": -10, "c4": -10, "c5": -10, "c6": -5, "c7": 0, "c8": 10, "d1": 15, "d2": -5, "d3": -18, "d4": -18, "d5": -18, "d6": -5, "d7": 0, "d8": 20, "e1": 15, "e2": -5, "e3": -18, "e4": -18, "e5": -18, "e6": -5, "e7": 0, "e8": 20, "f1": 15, "f2": -5, "f3": -10, "f4": -10, "f5": -10, "f6": -5, "f7": 0, "f8": 10, "g1": 20, "g2": 0, "g3": -10, "g4": -10, "g5": -5, "g6": 0, "g7": -5, "g8": 20, "h1": 40, "h2": 0, "h3": 0, "h4": 0, "h5": 0, "h6": 0, "h7": 0, "h8": 50}

        self.whiteKnight = {"a1": -50, "a2": -5, "a3": -5, "a4": -5, "a5": -5, "a6": -5, "a7": -5, "a8": -50, "b1": -20, "b2": 0, "b3": 5, "b4": 5, "b5": 5, "b6": 5, "b7": 5, "b8": -10, "c1": -10, "c2": 5, "c3": 8, "c4": 10, "c5": 10, "c6": 10, "c7": 5, "c8": -5, "d1": -10, "d2": 5, "d3": 8, "d4": 15, "d5": 15, "d6": 15, "d7": 5, "d8": -5, "e1": -10, "e2": 5, "e3": 8, "e4": 15, "e5": 15, "e6": 15, "e7": 5, "e8": -5, "f1": -10, "f2": 5, "f3": 8, "f4": 10, "f5": 10, "f6": 10, "f7": 5, "f8": -5, "g1": -20, "g2": 0, "g3": 5, "g4": 5, "g5": 5, "g6": 5, "g7": 5, "g8": -10, "h1": -50, "h2": -5, "h3": -5, "h4": -5, "h5": -5, "h6": -5, "h7": -5, "h8": -40}
        self.blackKnight = {"a1": 40, "a2": 5, "a3": 5, "a4": 5, "a5": 5, "a6": 5, "a7": 5, "a8": 50, "b1": 10, "b2": -5, "b3": -5, "b4": -5, "b5": -5, "b6": -5, "b7": 0, "b8": 20, "c1": 5, "c2": -5, "c3": -10, "c4": -10, "c5": -10, "c6": -8, "c7": -5, "c8": 10, "d1": 5, "d2": -5, "d3": -15, "d4": -15, "d5": -15, "d6": -8, "d7": -5, "d8": 10, "e1": 5, "e2": -5, "e3": -15, "e4": -15, "e5": -15, "e6": -8, "e7": -5, "e8": 10, "f1": 5, "f2": -5, "f3": -10, "f4": -10, "f5": -10, "f6": -8, "f7": -5, "f8": 10, "g1": 10, "g2": -5, "g3": -5, "g4": -5, "g5": -5, "g6": -5, "g7": 0, "g8": 20, "h1": 40, "h2": 5, "h3": 5, "h4": 5, "h5": 5, "h6": 5, "h7": 5, "h8": 50}

        self.whiteRook = {"a1": 0, "a2": 0, "a3": 0, "a4": 0, "a5": 0, "a6": 0, "a7": 5, "a8": 10, "b1": 0, "b2": 0, "b3": 0, "b4": 0, "b5": 0, "b6": 0, "b7": 5, "b8": 10, "c1": 5, "c2": 5, "c3": 5, "c4": 5, "c5": 5, "c6": 5, "c7": 5, "c8": 10, "d1": 10, "d2": 10, "d3": 10, "d4": 10, "d5": 10, "d6": 10, "d7": 10, "d8": 10, "e1": 10, "e2": 10, "e3": 10, "e4": 10, "e5": 10, "e6": 10, "e7": 10, "e8": 10, "f1": 5, "f2": 5, "f3": 5, "f4": 5, "f5": 5, "f6": 5, "f7": 5, "f8": 10, "g1": 0, "g2": 0, "g3": 0, "g4": 0, "g5": 0, "g6": 0, "g7": 5, "g8": 10, "h1": 0, "h2": 0, "h3": 0, "h4": 0, "h5": 0, "h6": 0, "h7": 5, "h8": 10}
        self.blackRook = {"a1": -10, "a2": -5, "a3": 0, "a4": 0, "a5": 0, "a6": 0, "a7": 0, "a8": 0, "b1": -10, "b2": -5, "b3": 0, "b4": 0, "b5": 0, "b6": 0, "b7": 0, "b8": 0, "c1": -10, "c2": -5, "c3": -5, "c4": -5, "c5": -5, "c6": -5, "c7": -5, "c8": -5, "d1": -10, "d2": -10, "d3": -10, "d4": -10, "d5": -10, "d6": -10, "d7": -10, "d8": -10, "e1": -10, "e2": -10, "e3": -10, "e4": -10, "e5": -10, "e6": -10, "e7": -10, "e8": -10, "f1": -10, "f2": -5, "f3": -5, "f4": -5, "f5": -5, "f6": -5, "f7": -5, "f8": -5, "g1": -10, "g2": -5, "g3": 0, "g4": 0, "g5": 0, "g6": 0, "g7": 0, "g8": 0, "h1": -10, "h2": -5, "h3": 0, "h4": 0, "h5": 0, "h6": 0, "h7": 0, "h8": 0}

        self.whiteQueen = {"a1": 0, "a2": 0, "a3": 0, "a4": 0, "a5": 0, "a6": 0, "a7": 0, "a8": 0, "b1": 0, "b2": 0, "b3": 0, "b4": 0, "b5": 0, "b6": 0, "b7": 0, "b8": 0, "c1": 0, "c2": 0, "c3": 10, "c4": 10, "c5": 10, "c6": 10, "c7": 0, "c8": 0, "d1": 0, "d2": 0, "d3": 10, "d4": 15, "d5": 15, "d6": 10, "d7": 0, "d8": 0, "e1": 0, "e2": 0, "e3": 10, "e4": 15, "e5": 15, "e6": 10, "e7": 0, "e8": 0, "f1": 0, "f2": 0, "f3": 10, "f4": 10, "f5": 10, "f6": 10, "f7": 0, "f8": 0, "g1": 0, "g2": 0, "g3": 0, "g4": 0, "g5": 0, "g6": 0, "g7": 0, "g8": 0, "h1": 0, "h2": 0, "h3": 0, "h4": 0, "h5": 0, "h6": 0, "h7": 0, "h8": 0}
        self.blackQueen = {"a1": 0, "a2": 0, "a3": 0, "a4": 0, "a5": 0, "a6": 0, "a7": 0, "a8": 0, "b1": 0, "b2": 0, "b3": 0, "b4": 0, "b5": 0, "b6": 0, "b7": 0, "b8": 0, "c1": 0, "c2": 0, "c3": -10, "c4": -10, "c5": -10, "c6": -10, "c7": 0, "c8": 0, "d1": 0, "d2": 0, "d3": -10, "d4": -15, "d5": -15, "d6": -10, "d7": 0, "d8": 0, "e1": 0, "e2": 0, "e3": -10, "e4": -15, "e5": -15, "e6": -10, "e7": 0, "e8": 0, "f1": 0, "f2": 0, "f3": -10, "f4": -10, "f5": -10, "f6": -10, "f7": 0, "f8": 0, "g1": 0, "g2": 0, "g3": 0, "g4": 0, "g5": 0, "g6": 0, "g7": 0, "g8": 0, "h1": 0, "h2": 0, "h3": 0, "h4": 0, "h5": 0, "h6": 0, "h7": 0, "h8": 0}

        self.whiteEKing = {"a1": 24, "a2": 24, "a3": 16, "a4": 12, "a5": 0, "a6": 0, "a7": 0, "a8": 0, "b1": 24, "b2": 20, "b3": 12, "b4": 8, "b5": 0, "b6": 0, "b7": 0, "b8": 0, "c1": 24, "c2": 16, "c3": 8, "c4": 4, "c5": 0, "c6": 0, "c7": 0, "c8": 0, "d1": 16, "d2": 12, "d3": 4, "d4": 0, "d5": 0, "d6": 0, "d7": 0, "d8": 0, "e1": 16, "e2": 12, "e3": 4, "e4": 0, "e5": 0, "e6": 0, "e7": 0, "e8": 0, "f1": 6, "f2": 16, "f3": 8, "f4": 4, "f5": 0, "f6": 0, "f7": 0, "f8": 0, "g1": 32, "g2": 20, "g3": 12, "g4": 8, "g5": 0, "g6": 0, "g7": 0, "g8": 0, "h1": 32, "h2": 24, "h3": 16, "h4": 12, "h5": 0, "h6": 0, "h7": 0, "h8": 0}
        self.blackEBlack = {"a1": 0, "a2": 0, "a3": 0, "a4": 0, "a5": -12, "a6": -16, "a7": -24, "a8": -24, "b1": 0, "b2": 0, "b3": 0, "b4": 0, "b5": -8, "b6": -12, "b7": -20, "b8": -24, "c1": 0, "c2": 0, "c3": 0, "c4": 0, "c5": -4, "c6": -8, "c7": -16, "c8": -24, "d1": 0, "d2": 0, "d3": 0, "d4": 0, "d5": 0, "d6": -4, "d7": -12, "d8": -16, "e1": 0, "e2": 0, "e3": 0, "e4": 0, "e5": 0, "e6": -4, "e7": -12, "e8": -16, "f1": 0, "f2": 0, "f3": 0, "f4": 0, "f5": -4, "f6": -8, "f7": -16, "f8": -6, "g1": 0, "g2": 0, "g3": 0, "g4": 0, "g5": -8, "g6": -12, "g7": -20, "g8": -32, "h1": 0, "h2": 0, "h3": 0, "h4": 0, "h5": -12, "h6": -16, "h7": -24, "h8": -32}

        self.whiteLKing = {"a1": -40, "a2": -10, "a3": 0, "a4": 0, "a5": 0, "a6": 0, "a7": -5, "a8": -30, "b1": -10, "b2": 0, "b3": 0, "b4": 0, "b5": 0, "b6": 0, "b7": 0, "b8": -5, "c1": -5, "c2": 0, "c3": 0, "c4": 0, "c5": 0, "c6": 0, "c7": 0, "c8": 0, "d1": -5, "d2": 0, "d3": 0, "d4": 5, "d5": 5, "d6": 0, "d7": 0, "d8": 0, "e1": -5, "e2": 0, "e3": 0, "e4": 5, "e5": 5, "e6": 0, "e7": 0, "e8": 0, "f1": -5, "f2": 0, "f3": 0, "f4": 0, "f5": 0, "f6": 0, "f7": 0, "f8": 0, "g1": -10, "g2": 0, "g3": 0, "g4": 0, "g5": 0, "g6": 0, "g7": 0, "g8": -5, "h1": -40, "h2": -10, "h3": 0, "h4": 0, "h5": 0, "h6": 0, "h7": -5, "h8": -30}
        self.blackLKing = {"a1": 30, "a2": 5, "a3": 0, "a4": 0, "a5": 0, "a6": 0, "a7": 10, "a8": 40, "b1": 5, "b2": 0, "b3": 0, "b4": 0, "b5": 0, "b6": 0, "b7": 0, "b8": 10, "c1": 0, "c2": 0, "c3": 0, "c4": 0, "c5": 0, "c6": 0, "c7": 0, "c8": 5, "d1": 0, "d2": 0, "d3": 0, "d4": -5, "d5": -5, "d6": 0, "d7": 0, "d8": 5, "e1": 0, "e2": 0, "e3": 0, "e4": -5, "e5": -5, "e6": 0, "e7": 0, "e8": 5, "f1": 0, "f2": 0, "f3": 0, "f4": 0, "f5": 0, "f6": 0, "f7": 0, "f8": 5, "g1": 5, "g2": 0, "g3": 0, "g4": 0, "g5": 0, "g6": 0, "g7": 0, "g8": 10, "h1": 30, "h2": 5, "h3": 0, "h4": 0, "h5": 0, "h6": 0, "h7": 0, "h8": 40}
        
class BoardSetUp:
    
    def __init__(self,colour):
        self.colour = colour
        self.PawnPositions = []
        self.RookPositions = []
        self.BishopPositions = []
        self.KnightPositions = []
        self.QueenPositions = []
        self.KingPositions = []
    
    def UpdatePawnPostion(self,MoveType,OldPosition,NewPosition):
        if MoveType==Capture or MoveType==Move:
            self.pawnPositions.remove(OldPosition)
            self.pawnPositions.append(NewPosition)

        if MoveType==Promote or MoveType==Captured:
            self.pawnPositions.remove(OldPosition)
        
    def UpdateRookPostion(self,MoveType,OldPosition,NewPosition):
        if MoveType==Capture or MoveType==Move:
            self.rookPositions.remove(OldPosition)
            self.rookPositions.append(NewPosition)
        if MoveType==Captured:
            self.rookPositions.remove(OldPosition)

    def UpdateKnightPosition(self,MoveType,OldPosition,NewPosition):
        if MoveType==Capture or MoveType==Move:
            self.KnightPositions.remove(OldPosition)
            self.KnightPositions.append(NewPosition)
        if MoveType==Captured:
            self.KnightPositions.remove(OldPosition)


    def UpdateBishopPosition(self,MoveType,OldPosition,NewPosition):
        if MoveType==Capture or MoveType==Move:
            self.BishopPositions.remove(OldPosition)
            self.BishopPositions.append(NewPosition)
        if MoveType==Captured:
            self.BishopPositions.remove(OldPosition)

    def UpdateQueenPosition(self,MoveType,OldPosition,NewPosition):
        if MoveType==Capture or MoveType==Move:
            self.QueenPositions.remove(OldPosition)
            self.QueenPositions.append(NewPosition)
        if MoveType==Captured:
            self.QueenPositions.remove(OldPosition)


    def UpdateKingPostion(self,MoveType,OldPosition,NewPosition):
        if MoveType==Capture or MoveType==Move:
            self.KingPositions.remove(OldPosition)
            self.KingPositions.append(NewPosition)
        if MoveType==Captured:
            self.KingPositions.remove(OldPosition)

    def StartPosition(self):
        colour = self.colour
        if colour==White:
            self.pawnPositions = ["a2","b2","c2","d2","e2","f2","g2","h2"]
            self.rookPositions = ["a1","h1"]
            self.KnightPositions=["b1","g1"]
            self.BishopPositions=["c1","f1"]
            self.QueenPositions=["d1"]
            self.KingPositions=["e1"]

        else:
            self.pawnPositions = ["a7","b7","c7","d7","e7","f7","g7","h7"]
            self.rookPositions = ["a8","h8"]
            self.KnightPositions = ["b8","g8"]
            self.KnightPositions = ["c8","f8"]
            self.QueenPositions = ["d8"]
            self.KingPositions = ["e8"]

class Evaluations:  
    def __init__(self):

        self.PawnValueWhite = 100
        self.RookValueWhite = 500
        self.KnightValueWhite = 300
        self.BishopValueWhite = 300
        self.QueenValueWhite = 900
        self.KingValueWhite = 1000

        self.PawnValueBlack = -100
        self.RookValueBlack = -500
        self.KnightValueBlack = -300
        self.BishopValueBlack = -300
        self.QueenValueBlack = -900
        self.KingValueBlack = -1000


        self.placesDictionary={}        
        self.placesDictionary["a1"]=0
        self.placesDictionary["b1"]=1
        self.placesDictionary["c1"]=2
        self.placesDictionary["d1"]=3
        self.placesDictionary["e1"]=4
        self.placesDictionary["f1"]=5
        self.placesDictionary["g1"]=6
        self.placesDictionary["h1"]=7

        self.placesDictionary["a2"]=8
        self.placesDictionary["b2"]=9
        self.placesDictionary["c2"]=10
        self.placesDictionary["d2"]=11
        self.placesDictionary["e2"]=12
        self.placesDictionary["f2"]=13
        self.placesDictionary["g2"]=14
        self.placesDictionary["h2"]=15

        self.placesDictionary["a3"]=16
        self.placesDictionary["b3"]=17
        self.placesDictionary["c3"]=18
        self.placesDictionary["d3"]=19
        self.placesDictionary["e3"]=20
        self.placesDictionary["f3"]=21
        self.placesDictionary["g3"]=22
        self.placesDictionary["h3"]=23

        self.placesDictionary["a4"]=24
        self.placesDictionary["b4"]=25
        self.placesDictionary["c4"]=26
        self.placesDictionary["d4"]=27
        self.placesDictionary["e4"]=28
        self.placesDictionary["f4"]=29
        self.placesDictionary["g4"]=30
        self.placesDictionary["h4"]=31

        self.placesDictionary["a5"]=32
        self.placesDictionary["b5"]=33
        self.placesDictionary["c5"]=34
        self.placesDictionary["d5"]=35
        self.placesDictionary["e5"]=36
        self.placesDictionary["f5"]=37
        self.placesDictionary["g5"]=38
        self.placesDictionary["h5"]=39

        self.placesDictionary["a6"]=40
        self.placesDictionary["b6"]=41
        self.placesDictionary["c6"]=42
        self.placesDictionary["d6"]=43
        self.placesDictionary["e6"]=44
        self.placesDictionary["f6"]=45
        self.placesDictionary["g6"]=46
        self.placesDictionary["h6"]=47


        self.placesDictionary["a7"]=48
        self.placesDictionary["b7"]=49
        self.placesDictionary["c7"]=50
        self.placesDictionary["d7"]=51
        self.placesDictionary["e7"]=52
        self.placesDictionary["f7"]=53
        self.placesDictionary["g7"]=54
        self.placesDictionary["h7"]=55

        self.placesDictionary["a8"]=56
        self.placesDictionary["b8"]=57
        self.placesDictionary["c8"]=58
        self.placesDictionary["d8"]=59
        self.placesDictionary["e8"]=60
        self.placesDictionary["f8"]=61
        self.placesDictionary["g8"]=62
        self.placesDictionary["h8"]=63

class ZobristHashing:
    def __init__(self):
        self.ZobHashTable = [[[random.randint(1,2**64 - 1) for i in range(12)]for j in range(8)]for k in range(8)]
        self.ZobHashDict = {}

    def computeHash(self, zobatable, board):
        h=0
        for i in range(8):
            for j in range(8):
                piece = self.getValueHash(board.piece_at(7*i+j))
                if piece!=-1:
                    h^=zobatable[i][j][piece]

        return h


    def getValueHash(piece):
        try:
            piece_type = piece.piece_type
            piece_colour = piece.color
            if piece_type==1 and piece_colour==True:
                return 0        
            elif piece_type==2 and piece_colour==True:
                return 1            
            elif piece_type==3 and piece_colour==True:
                return 2
            elif piece_type==4 and piece_colour==True:
                return 3
            elif piece_type==5 and piece_colour==True:
                return 4
            elif piece_type==6 and piece_colour==True:
                return 5
            elif piece_type==1 and piece_colour==False:
                return 6
            elif piece_type==2 and piece_colour==False:
                return 7
            elif piece_type==3 and piece_colour==False:
                return 8
            elif piece_type==4 and piece_colour==False:
                return 9
            elif piece_type==5 and piece_colour==False:
                return 10
            elif piece_type==6 and piece_colour==False:
                return 11

        except:
            return -1

class OpeningSetup:
    def __init__(self):
        self.yourColour = self.SelectColour()
        self.computerColour = self.getComputerColour(self.yourColour)
        self.path = self.getPath()
        self.diff = self.getDiff()

    def getComputerColour(self,yourColour):
       if yourColour == "White":
            computerColour = "Black"
            return computerColour
       else:
            computerColour= "White"
            return computerColour

    def SelectColour(self):
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

    def getPath(self):
        path = os.getcwd()
        return path

    def getDiff(self):
        while(True):
            print("Select a Number between 1 - 10 for Computer Level")
            x = input()
            x = int(x)
            if x >= 1 and x<=10:
                return x
            print("Invalid entry")

class BoardUpdatingMethods:
    
    def __init__(self,currentColour):
        self.currentColour = currentColour
        self.InputFromUser = ""
        self.InOpening=True
        self.openingMove= ""
        self.openingMoveList = []
        self.PreviousValue = 0
        self.InOpen = False
        self.checkInEndGame = False

    def changeColour(self,currentColour):
            if currentColour == "White":
                currentColour = "Black"

            elif currentColour == "Black":
                currentColour = "White"

            return currentColour

    def getInputFromUser(self,board):
        print("Enter one of these moves")
        bMoves = getMoveList(board)
        print(bMoves)
        move = input()
     
        if move in bMoves:
            return move
       
        if move == "PB" or move == "pb" or move == "Pb" or move == "pB":
            self.printBoardValues()

        elif move == "Exit" or move == "Quit" or move == "exit" or move =="quit":
            sys.exit()


        elif move not in bMoves:
            print("Invalid Entry Please Try Again ")
            move = self.getInputFromUser(board)

        return move

    def getMoveList(self,board):
        moves = board.legal_moves
        moves = str(moves)
        split_string = moves.split("(")
        split_string2 = split_string[1].split(")")
        allComputerMoves = split_string2[0].split(", ")
        return allComputerMoves

    def printBoardValues():
        alphaBoard = ["a","b","c","d","e","f","g","h"]
        numBoard = ["8","7","6","5","4","3","2","1"]
        for i in numBoard:
            print("")
            for j in alphaBoard:
                    print(i+j ,end=" ")
        print("")

    def checkIfInOpen(self,board,moveCount,openinglists,path):
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

    def stalemate(self,board):
        stalemate = board.is_stalemate()
        if stalemate == True:
            print("Stalemate Game is a Draw")
            sys.exit()

    def insufficient(self,board):
        insufficient = board.is_insufficient_material()
        if insufficient == True:
            print("The game is a draw by insufficient material")
            sys.exit()

    def threeFoldRep(self,board):
        threeRep = board.can_claim_threefold_repetition()
        if threeRep == True:
            print("Draw by Repition")
            sys.exit()

    def fiftyMoveNoCap(self,board):
        noCap = board.can_claim_fifty_moves()
        if noCap == True:
            print("No Capture in 50 moves, Game is a Draw")
            sys.exit()

    def isGameOver(self,board,currentColour):
        self.checkmate(board,currentColour)
        self.stalemate(board)
        self.insufficient(board)
        self.threeFoldRep(board)
        self.fiftyMoveNoCap(board)
        gameOver = board.is_game_over()
        if gameOver == True:
            print("Game Over for a different reason")
            print("Add Reason Later")
            sys.exit()

    def checkmate(self,board,currentColour):
        checkmate = board.is_checkmate()
        if checkmate == True:
            print(currentColour + " is the Winner")
            sys.exit()


    def EndGame(self,WhitePiece,BlackPiece):
        whiteTotal = 0
        blackTotal = 0
        whiteTotal+=len(WhitePiece.rookPositions)
        whiteTotal+=len(WhitePiece.BishopPositions)
        whiteTotal+=len(WhitePiece.KnightPositions)
        whiteTotal+=len(WhitePiece.QueenPositions)

        blackTotal+=len(BlackPiece.rookPositions)
        blackTotal+=len(BlackPiece.BishopPositions)
        blackTotal+=len(BlackPiece.KnightPositions)
        blackTotal+=len(BlackPiece.QueenPositions)

        if blackTotal<2 and whiteTotal<2:
            return False
        return True
         
class RiskAnalysis:
    def __init__(self):
        pass
    
    def PerformTree(self,board,BoardInformation,Setup,Zobrist,whitePieces,blackPieces):
        HighestValue = -math.inf
        LowestValue = math.inf
        high=-math.inf
        low=math.inf
        allComputerMoves = BoardInformation.getMoveList(board)
        oldColour = BoardInformation.currentColour
        BoardInformation.currentColour = BoardInformation.changeColour(BoardInformation.currentColour)        
        bestMove=""
        # SortedClass = Sorting(allComputerMoves)
        # SortedClass.sortedMoveList = SortedClass.sortMoveList(SortedClass.sortedMoveList)
        for move in allComputerMoves:
            futureBoard = board.copy()
            futureBoard.push_san(move)
            value, Zobrist, HighestValue, LowestValue = self.alphaBeta(futureBoard,1,BoardInformation,Setup,Zobrist,HighestValue,LowestValue,whitePieces,blackPieces)
            
        if oldColour==White:
            print(value)         
            if value>high:
              high=value
              bestMove=move

        elif oldColour==Black:
            if value<low:
              low=value
              bestMove=move
              
        
        #May need to look into return function
        return bestMove,Zobrist
     
    def alphaBeta(self,board,depth,BoardInformation,Setup,Zobrist,alpha,beta,whitePieces,blackPieces):
        allComputerMoves = BoardInformation.getMoveList(board)
        #allComputerMoves = getMoveList(board)
        if depth == Setup.diff:
            hashValue = computeHash(Zobrist.ZobHashTable, board)
            if hashValue in Zobrist.ZobHashDict:
                return False, Zobrist, alpha, beta
            else:
                Zobrist.ZobHashDict[hashValue]=hashValue
                BoardInformation.checkInEndGame = BoardInformation.EndGame(whitePieces,blackPieces)
                if BoardInformation.currentColour == "White":
                    return self.calculateMoveValue(move,whitePieces,blackPieces,BoardInformation,alpha,beta) 
                else:
                    return self.calculateMoveValue(move,whitePieces,blackPieces,BoardInformation,alpha,beta)

        if BoardInformation.currentColour == White:
            bestVal = float('-inf')
            try:
                for moveInList in allComputerMoves:
                    board.push_san(moveInList)
                    BoardInformation.currentColour = Black
                    treeValue,Zobrist,alpha, beta = self.alphaBeta(board,depth+1,BoardInformation,Setup,Zobrist,alpha,beta,whitePieces,blackPieces)
                    board.pop()
                    if treeValue!=False:                    
                        bestVal = max(bestVal,treeValue)                    
                        alpha = max(alpha,bestVal)
                        if beta<=alpha:
                            break
            except Exception as e:
                print("Error in AlphaBeta White Move")
                print(e)
                sys.exit()

            return bestVal, Zobrist, alpha, beta

        elif BoardInformation.currentColour == Black:
            bestVal = float('inf')
            try:
                for moveInList in allComputerMoves:
                    board.push_san(moveInList)
                    BoardInformation.currentColour = White
                    treeValue,Zobrist,alpha,beta = self.alphaBeta(board,depth+1,BoardInformation,Setup,Zobrist,alpha,beta,whitePieces,blackPieces)
                    board.pop()
                    if treeValue!=False:
                        bestVal = min(bestVal,treeValue)                        
                        beta = min(beta, bestVal)
                        if beta<=alpha:
                            break
            except Exception as e:
                print("Error in AlphaBeta White Move")
                print(e)
                sys.exit()

            return bestVal, Zobrist, alpha, beta

    def calculateMoveValue(self,move,WhitePieces,BlackPieces,BoardInformation,alpha,beta):
        value=0
        if "#" in move and BoardInformation.currentColour==White:
            value+=math.inf

        elif "#" in move and BoardInformation.currentColour==Black:
            value+=-math.inf

        elif "+" in move and BoardInformation.currentColour==White and BoardInformation.checkInEndGame==True:
            value+=50

        elif "+" in move and BoardInformation.currentColour==Black and BoardInformation.checkInEndGame==True:
            value+=-50

        elif "O-O-O" in move and BoardInformation.currentColour == White:
            value+=50

        elif "O-O-O" in move and BoardInformation.currentColour == Black:
            value+=-50

        elif "0-0" in move and BoardInformation.currentColour == White:
            value+=50

        elif "0-0" in move and BoardInformation.currentColour == Black:
            value+=-50

        elif "=" in move and BoardInformation.currentColour == White:
            value+=25
        elif "=" in move and BoardInformation.currentColour == Black:
            value+=-25
        BoardInformation = self.BoardValue(WhitePieces,BlackPieces,BoardInformation)
        return BoardInformation,Zobrist,alpha,beta

    def BoardValue(self,WhitePieces,BlackPieces,BoardInformation):
        #This Method Working on
        Locations=BoardValues()
        PieceValues=Evaluations()
        value=0        
        for i in WhitePieces.PawnPositions:
            value+=self.getValuePosition(White,1,BoardInformation.checkInEndGame,i,Locations)+PieceValues.PawnValueWhite        
        for i in WhitePieces.RookPositions:
            value+=self.getValuePosition(White,4,BoardInformation.checkInEndGame,i,Locations)+PieceValues.RookValueWhite
        for i in WhitePieces.BishopPositions:
            value+=self.getValuePosition(White,3,BoardInformation.checkInEndGame,i,Locations)+PieceValues.BishopValueWhite
        for i in WhitePieces.KnightPositions:
            value+=self.getValuePosition(White,2,BoardInformation.checkInEndGame,i,Locations)+PieceValues.KnightValueWhite
        for i in WhitePieces.QueenPositions:
            value+=self.getValuePosition(White,5,BoardInformation.checkInEndGame,i,Locations)+PieceValues.QueenValueWhite
        for i in WhitePieces.KingPositions:
            value+=self.getValuePosition(White,6,BoardInformation.checkInEndGame,i,Locations)

        for i in BlackPieces.PawnPositions:
            value+=self.getValuePosition(Black,1,BoardInformation.checkInEndGame,i,Locations)+PieceValues.PawnValueBlack
        for i in BlackPieces.RookPositions:
            value+=self.getValuePosition(White,4,BoardInformation.checkInEndGame,i,Locations)+PieceValues.RookValueBlack
        for i in BlackPieces.BishopPositions:
            value+=self.getValuePosition(White,3,BoardInformation.checkInEndGame,i,Locations)+PieceValues.BishopValueBlack
        for i in BlackPieces.KnightPositions:
            value+=self.getValuePosition(White,2,BoardInformation.checkInEndGame,i,Locations)+PieceValues.KnightValueBlack
        for i in BlackPieces.QueenPositions:
            value+=self.getValuePosition(White,5,BoardInformation.checkInEndGame,i,Locations)+PieceValues.QueenValueBlack
        for i in BlackPieces.KingPositions:
            value+=self.getValuePosition(White,6,BoardInformation.checkInEndGame,i,Locations)

        return value

    def getValuePosition(self,Colour,PieceType,LateGame,Location,Locations):
        
        if Colour==White:
            if PieceType==1:
                value = Locations.whitePawn[Location]
            elif PieceType==2:
                value = Locations.whiteKnight[Location]
            elif PieceType==3:
                value = Locations.whiteBishop[Location]
            elif PieceType==4:
                value = Locations.whiteRook[Location]
            elif PieceType==5:
                value = Locations.whiteQueen[Location]
            elif PieceType==6 and LateGame==False:
                value = Locations.whiteEKing[Location]
            elif PieceType==6 and LateGame==True:
                value = Locations.whiteLKing[Location]

        else:
            if PieceType==1:
                value=Locations.blackPawn[Location]
            elif PieceType==2:
                value=Locations.blackKnight[Location]
            elif PieceType==3:
                value=Locations.blackBishop[Location]
            elif PieceType==4:
                value=Locations.blackRook[Location]
            elif PieceType==5:
                value=Locations.blackQueen[Location]
            elif PieceType==6 and LateGame==False:
                value = Locations.whiteEKing[Location]
            elif PieceType==6 and LateGame==True:
                value = Locations.blackLKing[Location]
        return value

class Sorting:
    def __init__(self,boardMoveList):
        self.sortedMoveList = boardMoveList

    def sortMoveList(self,boardMoveList):
        sortedMoves = []
        checkmateFlag = False
        winningCaputure = False
        winningPromotion = False
        checkmateCount = 0
        for i in boardMoveList:
            if not sortedMoves:
                sortedMoves.append(i)
            if checkmate in i:
                 sortedMoves.insert(0,i)
                 checkmateFlag = True
                 checkmateCount+=1                
            elif ((Capturing in i or Promotion in i) and checkmateFlag==False and winningCaputure and winningPromotion): 
                sortedMoves.insert(0,i)
            
            elif ((Capturing in i or Promotion in i) and checkmateFlag==True and winningCaputure and winningPromotion):
                sortedMoves.insert(checkmateCount,i)
            else:
                sortedMoves.append(i)
        return sortedMoves

if __name__ == '__main__':
    Setup = OpeningSetup()
    whitePieces = BoardSetUp(White)
    blackPieces = BoardSetUp(Black)
    Zobrist = ZobristHashing()
    BoardInformation = BoardUpdatingMethods(White)
    MainAlgorthim = RiskAnalysis()
    whitePieces.StartPosition()
    blackPieces.StartPosition()
    board = chess.Board()

    moveCount = 0
    inOpening = True
   
    while (True):
        moveCount+=1
        print(board)
        
        if Setup.yourColour == BoardInformation.currentColour:
            print("User Turn")
            move = BoardInformation.getInputFromUser(board)
            board.push_san(move)          
            BoardInformation.currentColour = BoardInformation.changeColour(BoardInformation.currentColour)
                        
            if moveCount == 1:
                temppath = Setup.path+"/"+move
                openingMove = move
                movingList = os.listdir(temppath)
                     
            if inOpening==True:
                movingList = updatedMoveList(str(moveCount)+move,movingList,temppath)            
                print(len(movingList))
                if not movingList:
                    inOpening = False
                    

        elif Setup.yourColour != BoardInformation.currentColour:
            print("Computer Turn")                       
            if inOpening==True:
                move, moveList = checkIfInOpen(board,str(moveCount),movingList,Setup.path+"/"+openingMove)               
                if move == "No Move" or len(moveList)==0:          
                    inOpening=False

            if inOpening==False: 
                t0 = time.time()             
                move,Zobrist = MainAlgorthim.PerformTree(board,BoardInformation,Setup,Zobrist,whitePieces,blackPieces)                                            
                t1 = time.time()
                print("Time Move")
                print(t1-t0)

            print("Move Being Pushed")
            print(move)
            print("Current Colour")
            print(BoardInformation.currentColour)
            board.push_san(move)
            print(board)
            sys.exit()


        BoardInformation.isGameOver(board,BoardInformation.currentColour)

