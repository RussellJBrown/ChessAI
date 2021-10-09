from typing import Set
import chess
import sys
import os
import random
import ast
import time
import math
import copy

Capture="Capture"
Move="Move"
Promote="Promote"
Captured="Captured"
White="White"
Black="Black"
Checkmate = "#"
Check="+"
Promotion="="
Capturing="x"
Castling="0-0"

class BoardValues():
    def __init__(self):
        self.whitePawn = {"a1": 0, "a2": 0, "a3": 2, "a4": 4, "a5": 8, "a6": 12, "a7": 20, "a8": 0, "b1": 0, "b2": 0, "b3": 2, "b4": 6, "b5": 10, "b6": 14, "b7": 26, "b8": 0, "c1": 0, "c2": 0, "c3": 4, "c4": 8, "c5": 12, "c6": 16, "c7": 26, "c8": 0, "d1": 0, "d2": -4, "d3": 6, "d4": 14, "d5": 18, "d6": 21, "d7": 28, "d8": 0, "e1": 0, "e2": -4, "e3": 6, "e4": 16, "e5": 18, "e6": 21, "e7": 28, "e8": 0, "f1": 0, "f2": 0, "f3": 4, "f4": 8, "f5": 12, "f6": 16, "f7": 26, "f8": 0, "g1": 0, "g2": 0, "g3": 2, "g4": 6, "g5": 12, "g6": 14, "g7": 26, "g8": 0, "h1": 0, "h2": 0, "h3": 2, "h4": 4, "h5": 8, "h6": 12, "h7": 20, "h8": 0}
        self.blackPawn = {"a1": 0, "a2": -20, "a3": -12, "a4": -8, "a5": -4, "a6": -2, "a7": 0, "a8": 0, "b1": 0, "b2": -26, "b3": -14, "b4": -10, "b5": -6, "b6": -2, "b7": 0, "b8": 0, "c1": 0, "c2": -26, "c3": -16, "c4": -12, "c5": -8, "c6": -4, "c7": 0, "c8": 0, "d1": 0, "d2": -28, "d3": -21, "d4": -18, "d5": -20, "d6": -6, "d7": 4, "d8": 0, "e1": 0, "e2": -28, "e3": -21, "e4": -18, "e5": -20, "e6": -6, "e7": 4, "e8": 0, "f1": 0, "f2": -26, "f3": -16, "f4": -12, "f5": -8, "f6": -4, "f7": 0, "f8": 0, "g1": 0, "g2": -26, "g3": -14, "g4": -10, "g5": -6, "g6": -2, "g7": 0, "g8": 0, "h1": 0, "h2": -20, "h3": -12, "h4": -8, "h5": -4, "h6": -2, "h7": 0, "h8": 0}

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
        self.PawnPositions = {}
        self.RookPositions = {}
        self.BishopPositions = {}
        self.KnightPositions = {}
        self.QueenPositions = {}
        self.KingPositions = {}
    
    def UpdateWhitePawnPosition(self,MoveType,OldPosition,NewPosition,whiteP,blackP):
        if MoveType==Capture:
            del whiteP.PawnPositions[OldPosition]
            whiteP.PawnPositions[NewPosition]=NewPosition
            blackP.BishopPositions = self.DeleteBishop(NewPosition,blackP)
            blackP.KnightPositions = self.DeleteKnight(NewPosition,blackP)
            blackP.PawnPositions = self.DeletePawn(NewPosition,blackP)
            blackP.QueenPositions = self.DeleteQueen(NewPosition,blackP)
            blackP.RookPositions = self.DeleteRook(NewPosition,blackP)

        elif MoveType==Move:   
            del whiteP.PawnPositions[OldPosition]
            whiteP.PawnPositions[NewPosition]=NewPosition

        elif MoveType==Promote:
            del whiteP.PawnPositions[OldPosition]
        
        return whiteP, blackP
            
    def UpdateBlackPawnPosition(self,MoveType,OldPosition,NewPosition,whiteP,blackP):
        if MoveType==Capture:       
            del blackP.PawnPositions[OldPosition]
            blackP.PawnPositions[NewPosition]= NewPosition

            whiteP.BishopPositions = self.DeleteBishop(NewPosition,whiteP)
            whiteP.KnightPositions = self.DeleteKnight(NewPosition,whiteP)           
            whiteP.PawnPositions = self.DeletePawn(NewPosition,whiteP)
            whiteP.QueenPositions = self.DeleteQueen(NewPosition,whiteP)
            whiteP.RookPositions = self.DeleteRook(NewPosition,whiteP)


        if MoveType==Move:   
            del blackP.PawnPositions[OldPosition]
            blackP.PawnPositions[NewPosition]=NewPosition

        if MoveType==Promote:
            del blackP.PawnPositions[OldPosition]

        return whiteP, blackP
  
    def UpdateWhiteRookPosition(self,MoveType,OldPosition,NewPosition,whiteP,blackP):
        if MoveType==Capture: 
            del whiteP.RookPositions[OldPosition]
            whiteP.RookPositions[NewPosition]=NewPosition

            blackP.BishopPositions = self.DeleteBishop(NewPosition,blackP)
            blackP.KnightPositions = self.DeleteKnight(NewPosition,blackP)
            blackP.PawnPositions = self.DeletePawn(NewPosition,blackP)
            blackP.QueenPositions = self.DeleteQueen(NewPosition,blackP)
            blackP.RookPositions = self.DeleteRook(NewPosition,blackP)


        elif MoveType==Move:
            del whiteP.RookPositions[OldPosition]
            whiteP.RookPositions[NewPosition]=NewPosition

        return whiteP, blackP

    def UpdateBlackRookPosition(self,MoveType,OldPosition,NewPosition,whiteP,blackP):
        if MoveType==Capture: 
            del blackP.RookPositions[OldPosition]
            blackP.RookPositions[NewPosition]=NewPosition
            whiteP.BishopPositions = self.DeleteBishop(NewPosition,whiteP)
            whiteP.KnightPositions = self.DeleteKnight(NewPosition,whiteP)
            whiteP.PawnPositions = self.DeletePawn(NewPosition,whiteP)
            whiteP.QueenPositions = self.DeleteQueen(NewPosition,whiteP)
            whiteP.RookPositions = self.DeleteRook(NewPosition,whiteP)

        elif MoveType==Move:
            del blackP.RookPositions[OldPosition]
            blackP.RookPositions[NewPosition]=NewPosition

        return whiteP, blackP

    def UpdateWhiteKnightPosition(self,MoveType,OldPosition,NewPosition,whiteP,blackP):
        if MoveType==Capture: 
            del whiteP.KnightPositions[OldPosition]
            whiteP.KnightPositions[NewPosition] = NewPosition
            blackP.BishopPositions = self.DeleteBishop(NewPosition,blackP)
            blackP.KnightPositions = self.DeleteKnight(NewPosition,blackP)
            blackP.PawnPositions = self.DeletePawn(NewPosition,blackP)
            blackP.QueenPositions = self.DeleteQueen(NewPosition,blackP)
            blackP.RookPositions = self.DeleteRook(NewPosition,blackP)        
        
        if MoveType==Move:
            del whiteP.KnightPositions[OldPosition]
            whiteP.KnightPositions[NewPosition]=NewPosition
        return whiteP, blackP

    def UpdateBlackKnightPosition(self,MoveType,OldPosition,NewPosition,whiteP,blackP):
        if MoveType==Capture: 
            del blackP.KnightPositions[OldPosition]
            blackP.KnightPositions[NewPosition]=NewPosition        
            whiteP.BishopPositions = self.DeleteBishop(NewPosition,whiteP)
            whiteP.KnightPositions = self.DeleteKnight(NewPosition,whiteP)
            whiteP.PawnPositions = self.DeletePawn(NewPosition,whiteP)
            whiteP.QueenPositions = self.DeleteQueen(NewPosition,whiteP)
            whiteP.RookPositions = self.DeleteRook(NewPosition,whiteP)

        if MoveType==Move:
            del blackP.KnightPositions[OldPosition]
            blackP.KnightPositions[NewPosition]=NewPosition
        return whiteP, blackP

    def UpdateWhiteBishopPosition(self,MoveType,OldPosition,NewPosition,whiteP,blackP):
        if MoveType==Capture: 
            del whiteP.BishopPositions[OldPosition]
            whiteP.BishopPositions[NewPosition]=NewPosition
            blackP.BishopPositions = self.DeleteBishop(NewPosition,blackP)
            blackP.KnightPositions = self.DeleteKnight(NewPosition,blackP)
            blackP.PawnPositions = self.DeletePawn(NewPosition,blackP)
            blackP.QueenPositions = self.DeleteQueen(NewPosition,blackP)
            blackP.RookPositions = self.DeleteRook(NewPosition,blackP)

        if MoveType==Move:
            del whiteP.BishopPositions[OldPosition]
            whiteP.BishopPositions[NewPosition]=NewPosition
        return whiteP, blackP

    def UpdateBlackBishopPosition(self,MoveType,OldPosition,NewPosition,whiteP,blackP):
        if MoveType==Capture: 
            del blackP.BishopPositions[OldPosition]
            blackP.BishopPositions[NewPosition]=NewPosition
            whiteP.BishopPositions = self.DeleteBishop(NewPosition,whiteP)
            whiteP.KnightPositions = self.DeleteKnight(NewPosition,whiteP)
            whiteP.PawnPositions = self.DeletePawn(NewPosition,whiteP)
            whiteP.QueenPositions = self.DeleteQueen(NewPosition,whiteP)
            whiteP.RookPositions = self.DeleteRook(NewPosition,whiteP)

        if MoveType==Move:
            del blackP.BishopPositions[OldPosition]
            blackP.BishopPositions[NewPosition]=NewPosition
        return whiteP, blackP
   
    def UpdateWhiteQueenPosition(self,MoveType,OldPosition,NewPosition,whiteP,blackP):        
        if MoveType==Capture:
            del whiteP.QueenPositions[OldPosition]
            whiteP.QueenPositions[NewPosition]=NewPosition
            blackP.BishopPositions = self.DeleteBishop(NewPosition,blackP)
            blackP.KnightPositions = self.DeleteKnight(NewPosition,blackP)
            blackP.PawnPositions = self.DeletePawn(NewPosition,blackP)
            blackP.QueenPositions = self.DeleteQueen(NewPosition,blackP)
            blackP.RookPositions = self.DeleteRook(NewPosition,blackP)
        
        if MoveType==Move:
            del whiteP.QueenPositions[OldPosition]
            whiteP.QueenPositions[NewPosition]=NewPosition

        return whiteP, blackP

    def UpdateBlackQueenPosition(self,MoveType,OldPosition,NewPosition,whiteP,blackP):
        if MoveType==Capture:
            del blackP.QueenPositions[OldPosition]
            blackP.QueenPositions[NewPosition]=NewPosition
            whiteP.BishopPositions = self.DeleteBishop(NewPosition,whiteP)
            whiteP.KnightPositions = self.DeleteKnight(NewPosition,whiteP)
            whiteP.PawnPositions = self.DeletePawn(NewPosition,whiteP)
            whiteP.QueenPositions = self.DeleteQueen(NewPosition,whiteP)
            whiteP.RookPositions = self.DeleteRook(NewPosition,whiteP)
        
        if MoveType==Move:
            del blackP.QueenPositions[OldPosition]
            blackP.QueenPositions[NewPosition]=NewPosition

        return whiteP, blackP

    def UpdateWhiteKingPosition(self,MoveType,OldPosition,NewPosition,whiteP,blackP):
        if MoveType==Capture: 
            del whiteP.KingPositions[OldPosition]
            whiteP.KingPositions[NewPosition]=NewPosition
            blackP.BishopPositions = self.DeleteBishop(NewPosition,blackP)
            blackP.KnightPositions = self.DeleteKnight(NewPosition,blackP)
            blackP.PawnPositions = self.DeletePawn(NewPosition,blackP)
            blackP.QueenPositions = self.DeleteQueen(NewPosition,blackP)
            blackP.RookPositions = self.DeleteRook(NewPosition,blackP)


        if MoveType==Move:
            del whiteP.KingPositions[OldPosition]
            whiteP.KingPositions[NewPosition] = NewPosition
        
        if MoveType==Castling:
            del blackP.KingPositions[OldPosition[0]]
            del blackP.RookPositions[OldPosition[1]]
            blackP.KingPositions[NewPosition[0]]=NewPosition[0]
            blackP.RookPositions[NewPosition[1]]=NewPosition[1]

        return whiteP,blackP

    def UpdateBlackKingPosition(self,MoveType,OldPosition,NewPosition,whiteP,blackP):
        if MoveType==Capture: 
            del blackP.KingPositions[OldPosition]
            blackP.KingPositions[NewPosition]=NewPosition
            whiteP.BishopPositions = self.DeleteBishop(NewPosition,whiteP)
            whiteP.KnightPositions = self.DeleteKnight(NewPosition,whiteP)
            whiteP.PawnPositions = self.DeletePawn(NewPosition,whiteP)
            whiteP.QueenPositions = self.DeleteQueen(NewPosition,whiteP)
            whiteP.RookPositions = self.DeleteRook(NewPosition,whiteP)
        if MoveType==Move:
            del blackP.KingPositions[OldPosition]
            blackP.KingPositions[NewPosition] = NewPosition
        
        if MoveType==Castling:
            del blackP.KingPositions[OldPosition[0]]
            del blackP.RookPositions[OldPosition[1]]
            blackP.KingPositions[NewPosition[0]]=NewPosition[0]
            blackP.RookPositions[NewPosition[1]]=NewPosition[1]

        return whiteP,blackP


    def DeleteBishop(self,DeletePosition,Bishop):
        try:
             del Bishop.BishopPositions[DeletePosition]
             return Bishop.BishopPositions
        except:
            return Bishop.BishopPositions
    
    def DeleteRook(self,DeletePosition,Rook):
        try:
            del Rook.RookPositions[DeletePosition]
            return Rook.RookPositions
        except:
            return Rook.RookPositions
   
    def DeletePawn(self,DeletePosition,Pawn):
        try:
            del Pawn.PawnPositions[DeletePosition]
            return Pawn.PawnPositions
        except:
            return Pawn.PawnPositions
            
    def DeleteQueen(self,DeletePositon,Queen):
        try:
            del Queen.QueenPositions[DeletePositon]
            return Queen.QueenPositions
        except:
            return Queen.QueenPositions
  
    def DeleteKnight(self,DeletePosition,Knight):
        try:
            del Knight.KnightPositions[DeletePosition]       
            return Knight.KnightPositions
        except:
            return Knight.KnightPositions

    def StartPosition(self):
        colour = self.colour
        if colour==White:
            self.PawnPositions = {"a2":"a2","b2":"b2","c2":"c2","d2":"d2","e2":"e2","f2":"f2","g2":"g2","h2":"h2"}

            self.RookPositions = {"a1":"a1","h1":"h1"}
            
            self.KnightPositions={"b1":"b1","g1":"g1"}

            self.BishopPositions={"c1":"c1","f1":"f1"}

            self.QueenPositions={"d1":"d1"}

            self.KingPositions={"e1":"e1"}

        else:
            
            self.PawnPositions = {"a7":"a7","b7":"b7","c7":"c7","d7":"d7","e7":"e7","f7":"f7","g7":"g7","h7":"h7"}

            self.RookPositions = {"a8":"a8","h8":"h8"}

            self.KnightPositions={"b8":"b8","g8":"g8"}

            self.BishopPositions={"c8":"c8","f8":"f8"}

            self.QueenPositions={"d8":"d8"}

            self.KingPositions={"e8":"e8"}

class Evaluations:  
    def __init__(self):

        self.PawnValueWhite = 124
        self.RookValueWhite = 1276
        self.KnightValueWhite = 781
        self.BishopValueWhite = 825
        self.QueenValueWhite = 2538
        self.KingValueWhite = 0

        self.PawnValueBlack = -124
        self.RookValueBlack = -1276
        self.KnightValueBlack = -781
        self.BishopValueBlack = -825
        self.QueenValueBlack  =-2538
        self.KingValueBlack = 0


    



        self.placesDictionary={}        
        self.placesDictionary[0]="a1"
        self.placesDictionary[1]="b1"
        self.placesDictionary[2]="c1"
        self.placesDictionary[3]="d1"
        self.placesDictionary[4]="e1"
        self.placesDictionary[5]="f1"
        self.placesDictionary[6]="g1"
        self.placesDictionary[7]="h1"

        self.placesDictionary[8]="a2"
        self.placesDictionary[9]="b2"
        self.placesDictionary[10]="c2"
        self.placesDictionary[11]="d2"
        self.placesDictionary[12]="e2"
        self.placesDictionary[13]="f2"
        self.placesDictionary[14]="g2"
        self.placesDictionary[15]="h2"

        self.placesDictionary[16]="a3"
        self.placesDictionary[17]="b3"
        self.placesDictionary[18]="c3"
        self.placesDictionary[19]="d3"
        self.placesDictionary[20]="e3"
        self.placesDictionary[21]="f3"
        self.placesDictionary[22]="g3"
        self.placesDictionary[23]="h3"

        self.placesDictionary[24]="a4"
        self.placesDictionary[25]="b4"
        self.placesDictionary[26]="c4"
        self.placesDictionary[27]="d4"
        self.placesDictionary[28]="e4"
        self.placesDictionary[29]="f4"
        self.placesDictionary[30]="g4"
        self.placesDictionary[31]="h4"

        self.placesDictionary[32]="a5"
        self.placesDictionary[33]="b5"
        self.placesDictionary[34]="c5"
        self.placesDictionary[35]="d5"
        self.placesDictionary[36]="e5"
        self.placesDictionary[37]="f5"
        self.placesDictionary[38]="g5"
        self.placesDictionary[39]="h5"

        self.placesDictionary[40]="a6"
        self.placesDictionary[41]="b6"
        self.placesDictionary[42]="c6"
        self.placesDictionary[43]="d6"
        self.placesDictionary[44]="e6"
        self.placesDictionary[45]="f6"
        self.placesDictionary[46]="g6"
        self.placesDictionary[47]="h6"


        self.placesDictionary[48]="a7"
        self.placesDictionary[49]="b7"
        self.placesDictionary[50]="c7"
        self.placesDictionary[51]="d7"
        self.placesDictionary[52]="e7"
        self.placesDictionary[53]="f7"
        self.placesDictionary[54]="g7"
        self.placesDictionary[55]="h7"

        self.placesDictionary[56]="a8"
        self.placesDictionary[57]="b8"
        self.placesDictionary[58]="c8"
        self.placesDictionary[59]="d8"
        self.placesDictionary[60]="e8"
        self.placesDictionary[61]="f8"
        self.placesDictionary[62]="g8"
        self.placesDictionary[63]="h8"

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


    def getValueHash(self,piece):
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

    def updatedMoveList(self,move,openingList,path):
        for i in openingList:
            file = open(path+"/"+i,"r")
            contents= file.read()
            dictionary = ast.literal_eval(contents) 
            if move not in dictionary:
                openingList.remove(i)
        
        return openingList


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
        bMoves = self.getMoveList(board)
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

    def printBoardValues(self):
        alphaBoard = ["a","b","c","d","e","f","g","h"]
        numBoard = ["8","7","6","5","4","3","2","1"]
        for i in numBoard:
            print("")
            for j in alphaBoard:
                    print(i+j ,end=" ")
        print("")

    def checkIfInOpen(self,board,moveCount,openinglists,path):
        CurrentComputerMoves = self.getMoveList(board)
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
            lists = self.remove(moveCount+openingMove,openinglists,path)
        
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
        whiteTotal+=len(WhitePiece.RookPositions)
        whiteTotal+=len(WhitePiece.BishopPositions)
        whiteTotal+=len(WhitePiece.KnightPositions)
        whiteTotal+=len(WhitePiece.QueenPositions)

        blackTotal+=len(BlackPiece.RookPositions)
        blackTotal+=len(BlackPiece.BishopPositions)
        blackTotal+=len(BlackPiece.KnightPositions)
        blackTotal+=len(BlackPiece.QueenPositions)

        if blackTotal<2 and whiteTotal<2:
            return False
        return True
         
    def remove(self,move,listOpening,path):
        for i in listOpening:
          file = open(path+"/"+i,"r")
          contents = file.read()
          dictionary = ast.literal_eval(contents)
          if move not in dictionary:
              listOpening.remove(i)

        return listOpening 


class RiskAnalysis:
    def __init__(self):
        pass
    
    def SquareUpdating(self,Move,oldSquare,newSquare,whitePieces,blackPieces,colour):
        if(colour=="White"):  
                if(oldSquare in whitePieces.PawnPositions):
                    if(Capture==Move):
                     whitePieces,blackPieces = BoardSetUp("White").UpdateWhitePawnPosition(Capture,oldSquare,newSquare,whitePieces,blackPieces)
                    elif(Promotion==Move):
                      whitePieces,blackPieces = BoardSetUp("White").UpdateWhitePawnPosition(Promotion,oldSquare,newSquare,whitePieces,blackPieces)
                    else:
                       whitePieces,blackPieces = BoardSetUp("White").UpdateWhitePawnPosition(Move,oldSquare,newSquare,whitePieces,blackPieces)
                       
                elif(oldSquare in whitePieces.RookPositions):
                    if(Capture==Move):
                        whitePieces,blackPieces = BoardSetUp("White").UpdateWhiteRookPosition(Capture,oldSquare,newSquare,whitePieces,blackPieces)
                    else:
                        whitePieces,blackPieces = BoardSetUp("White").UpdateWhiteRookPosition(Move,oldSquare,newSquare,whitePieces,blackPieces)

                elif(oldSquare in whitePieces.BishopPositions):
                    if(Capture==Move):
                        whitePieces,blackPieces = BoardSetUp("White").UpdateWhiteBishopPosition(Capture,oldSquare,newSquare,whitePieces,blackPieces)
                    else:
                        whitePieces,blackPieces = BoardSetUp("White").UpdateWhiteBishopPosition(Move,oldSquare,newSquare,whitePieces,blackPieces)

                elif(oldSquare in whitePieces.KnightPositions):
                    if(Capture==Move):
                        whitePieces,blackPieces = BoardSetUp("White").UpdateWhiteKnightPosition(Capture,oldSquare,newSquare,whitePieces,blackPieces)
                    else:
                        whitePieces,blackPieces = BoardSetUp("White").UpdateWhiteKnightPosition(Move,oldSquare,newSquare,whitePieces,blackPieces)
                
                elif(oldSquare in whitePieces.QueenPositions):
                    if(Capture==Move):
                       whitePieces,blackPieces = BoardSetUp("White").UpdateWhiteQueenPosition(Capture,oldSquare,newSquare,whitePieces,blackPieces)
                    else:
                        whitePieces,blackPieces = BoardSetUp("White").UpdateWhiteQueenPosition(Move,oldSquare,newSquare,whitePieces,blackPieces)
                
                elif(oldSquare in whitePieces.KingPositions):
                    if(Capture==Move):
                       whitePieces,blackPieces = BoardSetUp("White").UpdateWhiteKingPosition(Capture,oldSquare,newSquare,whitePieces,blackPieces)
                    elif(Castling==Move):
                       whitePieces,blackPieces = BoardSetUp("White").UpdateWhiteKingPosition(Castling,oldSquare,newSquare,whitePieces,blackPieces)
                    else:
                       whitePieces,blackPieces = BoardSetUp("White").UpdateWhiteKingPosition(Move,oldSquare,newSquare,whitePieces,blackPieces)

        elif(colour=="Black"):           
                if(oldSquare in blackPieces.PawnPositions):
                    if(Capture==Move):
                        whitePieces,blackPieces = BoardSetUp("Black").UpdateBlackPawnPosition(Capture,oldSquare,newSquare,whitePieces,blackPieces)
                    elif(Promotion==Move):
                        whitePieces,blackPieces = BoardSetUp("Black").UpdateBlackPawnPosition(Promotion,oldSquare,newSquare,whitePieces,blackPieces)
                    else:
                        whitePieces,blackPieces = BoardSetUp("Black").UpdateBlackPawnPosition(Move,oldSquare,newSquare,whitePieces,blackPieces)
                    
                elif(oldSquare in blackPieces.RookPositions):
                    if(Capture==Move):
                       whitePieces,blackPieces = BoardSetUp("Black").UpdateBlackRookPosition(Capture,oldSquare,newSquare,whitePieces,blackPieces)
                    else:
                       whitePieces,blackPieces = BoardSetUp("Black").UpdateBlackRookPosition(Move,oldSquare,newSquare,whitePieces,blackPieces)

                elif(oldSquare in blackPieces.BishopPositions):
                    if(Capture==Move):
                        whitePieces,blackPieces = BoardSetUp("Black").UpdateBlackBishopPosition(Capture,oldSquare,newSquare,whitePieces,blackPieces)
                    else:
                        whitePieces,blackPieces = BoardSetUp("Black").UpdateBlackBishopPosition(Move,oldSquare,newSquare,whitePieces,blackPieces)

                elif(oldSquare in blackPieces.KnightPositions):
                    if(Capture==Move):
                       whitePieces,blackPieces = BoardSetUp("Black").UpdateBlackKnightPosition(Capture,oldSquare,newSquare,whitePieces,blackPieces)
                    else:
                        whitePieces,blackPieces = BoardSetUp("Black").UpdateBlackKnightPosition(Move,oldSquare,newSquare,whitePieces,blackPieces)

                elif(oldSquare in blackPieces.QueenPositions):
                    if(Capture==Move):
                        whitePieces,blackPieces = BoardSetUp("Black").UpdateBlackQueenPosition(Capture,oldSquare,newSquare,whitePieces,blackPieces)
                    else:
                        whitePieces,blackPieces = BoardSetUp("Black").UpdateBlackQueenPosition(Move,oldSquare,newSquare,whitePieces,blackPieces)
                
                elif(oldSquare in blackPieces.KingPositions):
                    if(Capture==Move):
                        whitePieces,blackPieces = BoardSetUp("Black").UpdateBlackKingPosition(Capture,oldSquare,newSquare,whitePieces,blackPieces)
                    elif(Castling==Move):
                        whitePieces,blackPieces = BoardSetUp("Black").UpdateBlackKingPosition(Castling,oldSquare,newSquare,whitePieces,blackPieces)
                    else:
                        whitePieces,blackPieces = BoardSetUp("Black").UpdateBlackKingPosition(Move,oldSquare,newSquare,whitePieces,blackPieces)

        return whitePieces, blackPieces

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
        bestWhite = copy.deepcopy(whitePieces)
        bestBlack = copy.deepcopy(blackPieces)
        moveType=""     
        boardLocations=Evaluations()
        for move in allComputerMoves:
            oldWhitePieces = copy.deepcopy(whitePieces)
            oldBlackPieces = copy.deepcopy(blackPieces)
            futureBoard = board.copy()
            futureBoard.push_san(move)
            oldSquare=boardLocations.placesDictionary[futureBoard.peek().from_square]
            newSquare=boardLocations.placesDictionary[futureBoard.peek().to_square]         
            if Capturing in move:
                moveType=Capture
            elif Promotion in move:
                moveType=Promotion
            elif Castling in move:
                moveType = Castling
            else:
                moveType = Move                  
         
            tempW,tempB=self.SquareUpdating(moveType,oldSquare,newSquare,oldWhitePieces,oldBlackPieces,oldColour)
            ImposterValue, Zobrist, HighestValue, LowestValue,realValue = self.alphaBeta(futureBoard,1,BoardInformation,Setup,Zobrist,HighestValue,LowestValue,oldWhitePieces,oldBlackPieces)                

            print("------------Move: -------------------------")
            print(oldColour)
            print(move)
            print("Real Value: ")
            print(realValue)



            if oldColour==White:        
                if realValue>high:
                    high=realValue
                    bestMove=move
                    bestWhite = tempW
                    bestBlack = tempB
                    
                
            elif oldColour==Black:
                if realValue<low:
                    low=realValue
                    bestMove=move
                    bestWhite = tempW
                    bestBlack = tempB
              
        print("Best Move: ")
        print(bestMove)
        return bestMove,Zobrist, bestWhite, bestBlack
     
    def alphaBeta(self,board,depth,BoardInformation,Setup,Zobrist,alpha,beta,whitePieces,blackPieces):
        allComputerMoves = BoardInformation.getMoveList(board)
        #allComputerMoves = getMoveList(board)
        boardLocations=Evaluations()
        move=""
        if depth == Setup.diff:
            hashValue = Zobrist.computeHash(Zobrist.ZobHashTable, board)
            if hashValue in Zobrist.ZobHashDict:
                return False, Zobrist, alpha, beta,0
            else:
                Zobrist.ZobHashDict[hashValue]=hashValue
                BoardInformation.checkInEndGame = BoardInformation.EndGame(whitePieces,blackPieces)
                if BoardInformation.currentColour == "White":
                    return self.calculateMoveValue(move,whitePieces,blackPieces,BoardInformation,alpha,beta) 
                else:
                    return self.calculateMoveValue(move,whitePieces,blackPieces,BoardInformation,alpha,beta)

        elif BoardInformation.currentColour == White:
            bestVal = float('-inf')
            try:               
                for moveInList in allComputerMoves:
                    # print("Depth: " +str(depth))
                    # print("White Move:")
                    # print(moveInList)
                    oldWhitePieces = copy.deepcopy(whitePieces)
                    oldBlackPieces = copy.deepcopy(blackPieces)
                    board.push_san(moveInList)
                    oldSquare=boardLocations.placesDictionary[board.peek().from_square]
                    newSquare=boardLocations.placesDictionary[board.peek().to_square]         
                    if Capturing in move:
                        move=Capture
                    elif Promotion in move:
                        move=Promotion
                    elif Castling in move:
                        move = Castling
                    else:
                        move = Move
                                                        
                    oldWhitePieces,oldBlackPieces=self.SquareUpdating(move,oldSquare,newSquare,oldWhitePieces,oldBlackPieces,White)                                    
                    BoardInformation.currentColour = Black
                    treeValue,Zobrist,alpha, beta,actualValue = self.alphaBeta(board,depth+1,BoardInformation,Setup,Zobrist,alpha,beta,oldWhitePieces,oldBlackPieces)          
                    board.pop()
                    if treeValue!=False:                    
                        #bestVal = max(bestVal,treeValue)                    
                        bestVal = max(bestVal,actualValue)
                        alpha = max(alpha,bestVal)
                        # print("----White Move After Move Check----")
                        # print("Depth: " + str(depth))
                        # print("Beta: "+ str(beta))
                        # print("Alpha: "+str(alpha))
                        # print("Best Value: " + str(bestVal))
                        if beta<=alpha:
                            break

            except Exception as e:
                print("Error in AlphaBeta White Move White")
                print(e)
                sys.exit()

            return BoardInformation, Zobrist, alpha, beta,bestVal

        elif BoardInformation.currentColour == Black:
            bestVal = float('inf')
            try:
                for moveInList in allComputerMoves:
                    # print("Depth: " +str(depth))
                    # print("Black Move:")
                    #print(moveInList)
                    oldWhitePieces = copy.deepcopy(whitePieces)
                    oldBlackPieces = copy.deepcopy(blackPieces)
                    board.push_san(moveInList)
                    oldSquare=boardLocations.placesDictionary[board.peek().from_square]
                    newSquare=boardLocations.placesDictionary[board.peek().to_square]
                    if Capturing in moveInList:
                        move=Capture
                    elif Promotion in moveInList:
                        move=Promotion
                    elif Castling in moveInList:
                        move = Castling         
                    else: 
                        move = Move
                                                                    
                    oldWhitePieces,oldBlackPieces=self.SquareUpdating(move,oldSquare,newSquare,oldWhitePieces,oldBlackPieces,Black)
                    BoardInformation.currentColour = White
                    treeValue,Zobrist,alpha,beta,actualValue = self.alphaBeta(board,depth+1,BoardInformation,Setup,Zobrist,alpha,beta,oldWhitePieces,oldBlackPieces)
                    board.pop()
                    if treeValue!=False:
                        #bestVal = min(bestVal,treeValue)                        
                        bestVal = min(bestVal,actualValue)
                        beta = min(beta, bestVal)
                        if beta<=alpha:
                            break
            except Exception as e:
                print("Error in AlphaBeta White Move Black")
                print(e)
                sys.exit()

            return BoardInformation, Zobrist, alpha, beta,bestVal

    def calculateMoveValue(self,move,WhitePieces,BlackPieces,BoardInformation,alpha,beta):
        value=0
        if "#" in move and BoardInformation.currentColour==White:
            value+=math.inf

        elif "#" in move and BoardInformation.currentColour==Black:
            value+=-math.inf

        elif "+" in move and BoardInformation.currentColour==White and BoardInformation.checkInEndGame==True:
            value+=15

        elif "+" in move and BoardInformation.currentColour==Black and BoardInformation.checkInEndGame==True:
            value+=-15

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
        value += self.BoardValue(WhitePieces,BlackPieces,BoardInformation)
        return BoardInformation,Zobrist,alpha,beta,value

    def BoardValue(self,WhitePieces,BlackPieces,BoardInformation):
        #This Method Working on
        Locations=BoardValues()
        PieceValues=Evaluations()
        valueWhite=0
        valueBlack=0        
        for i in WhitePieces.PawnPositions:
            valueWhite+=self.getValuePosition(White,1,BoardInformation.checkInEndGame,i,Locations)+PieceValues.PawnValueWhite        
        for i in WhitePieces.RookPositions:
            valueWhite+=self.getValuePosition(White,4,BoardInformation.checkInEndGame,i,Locations)+PieceValues.RookValueWhite
        for i in WhitePieces.BishopPositions:
            valueWhite+=self.getValuePosition(White,3,BoardInformation.checkInEndGame,i,Locations)+PieceValues.BishopValueWhite
        for i in WhitePieces.KnightPositions:
            valueWhite+=self.getValuePosition(White,2,BoardInformation.checkInEndGame,i,Locations)+PieceValues.KnightValueWhite
        for i in WhitePieces.QueenPositions:
            valueWhite+=self.getValuePosition(White,5,BoardInformation.checkInEndGame,i,Locations)+PieceValues.QueenValueWhite
        for i in WhitePieces.KingPositions:
            valueWhite+=self.getValuePosition(White,6,BoardInformation.checkInEndGame,i,Locations)


        for i in BlackPieces.PawnPositions:
            valueBlack+=self.getValuePosition(Black,1,BoardInformation.checkInEndGame,i,Locations)+PieceValues.PawnValueBlack
        for i in BlackPieces.RookPositions:
            valueBlack+=self.getValuePosition(Black,4,BoardInformation.checkInEndGame,i,Locations)+PieceValues.RookValueBlack
        for i in BlackPieces.BishopPositions:
            valueBlack+=self.getValuePosition(Black,3,BoardInformation.checkInEndGame,i,Locations)+PieceValues.BishopValueBlack
        for i in BlackPieces.KnightPositions:
            valueBlack+=self.getValuePosition(Black,2,BoardInformation.checkInEndGame,i,Locations)+PieceValues.KnightValueBlack
        for i in BlackPieces.QueenPositions:
            valueBlack+=self.getValuePosition(Black,5,BoardInformation.checkInEndGame,i,Locations)+PieceValues.QueenValueBlack
        for i in BlackPieces.KingPositions:
            valueBlack+=self.getValuePosition(Black,6,BoardInformation.checkInEndGame,i,Locations)

        # print("Value White: ")
        # print(valueWhite)

        # print("Value Black: ")
        # print(valueBlack)

        # print("Value: ")
        # print(valueWhite+valueBlack)

        return valueWhite+valueBlack


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
            if Checkmate in i:
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
    moveType = ""
    while (True):
        moveCount+=1
        print(board)
        if Setup.yourColour == BoardInformation.currentColour:
            print("User Turn")
            move = BoardInformation.getInputFromUser(board)
            board.push_san(move)
            boardLocations=Evaluations()
            oldSquare=boardLocations.placesDictionary[board.peek().from_square]
            newSquare=boardLocations.placesDictionary[board.peek().to_square]         
            if Capturing in move:
                moveType=Capture
            elif Promotion in move:
                moveType=Promotion
            elif Castling in move:
                moveType = Castling
            else:
                moveType = Move
            
            whitePieces,blackPieces=MainAlgorthim.SquareUpdating(moveType,oldSquare,newSquare,whitePieces,blackPieces,White)
            BoardInformation.currentColour = BoardInformation.changeColour(BoardInformation.currentColour)

            if moveCount == 1:
                temppath = Setup.path+"/"+move
                openingMove = move
                movingList = os.listdir(temppath)
                     
            if inOpening==True:
                movingList = Setup.updatedMoveList(str(moveCount)+move,movingList,temppath)            
                if not movingList:
                    inOpening = False

            BoardInformation.currentColour=Black       

        elif Setup.yourColour != BoardInformation.currentColour:
            print("Computer Turn")                       
            if inOpening==True:
                bestMove, moveList = BoardInformation.checkIfInOpen(board,str(moveCount),movingList,Setup.path+"/"+openingMove)               
                if move == "No Move" or len(moveList)==0:          
                    inOpening=False

            if inOpening==False: 
                t0 = time.time()             
                bestMove,Zobrist, whitePieces, blackPieces = MainAlgorthim.PerformTree(board,BoardInformation,Setup,Zobrist,whitePieces,blackPieces)                                            
                t1 = time.time()
                print("Time Move")
                print(t1-t0)
                print("Move Being Pushed")
                print(bestMove)
          

            board.push_san(bestMove)
            BoardInformation.currentColour=White
        

        BoardInformation.isGameOver(board,BoardInformation.currentColour)

