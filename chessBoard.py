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
CastlingLong="O-O-O"
CastlingShort="O-O"

class BoardValues():
    def __init__(self):
        self.whitePawnMid = {"a1": 0, "a2": 3, "a3": -9, "a4": -4, "a5": 13, "a6": 5, "a7": -7, "a8": 0, "b1": 0, "b2": 3, "b3": -15, "b4": -23, "b5": -2, "b6": -12, "b7": 7, "b8": 0, "c1": 0, "c2": 10, "c3": 11, "c4": 6, "c5": -13, "c6": -7, "c7": -3, "c8": 0, "d1": 0, "d2": 19, "d3": 15, "d4": 20, "d5": 1, "d6": 22, "d7": -13, "d8": 0, "e1": 0, "e2": 16, "e3": 32, "e4": 40, "e5": 11, "e6": -8, "e7": 5, "e8": 0, "f1": 0, "f2": 19, "f3": 22, "f4": 17, "f5": -2, "f6": -5, "f7": -16, "f8": 0, "g1": 0, "g2": 7, "g3": 5, "g4": 4, "g5": -13, "g6": -15, "g7": 10, "g8": 0, "h1": 0, "h2": -5, "h3": -22, "h4": -8, "h5": 5, "h6": -8, "h7": -5, "h8": 0}
        self.whiteBishopMid = {"a1": -53, "a2": -15, "a3": -7, "a4": -5, "a5": -12, "a6": -16, "a7": -17, "a8": -48, "b1": -5, "b2": 8, "b3": 21, "b4": 11, "b5": 29, "b6": 6, "b7": -14, "b8": 1, "c1": -8, "c2": 19, "c3": -5, "c4": 25, "c5": 22, "c6": 1, "c7": 5, "c8": -14, "d1": -23, "d2": 4, "d3": 17, "d4": 39, "d5": 31, "d6": 11, "d7": 6, "d8": -23, "e1": -23, "e2": 4, "e3": 17, "e4": 39, "e5": 31, "e6": 11, "e7": 4, "e8": -23, "f1": -8, "f2": 19, "f3": -5, "f4": 25, "f5": 22, "f6": 1, "f7": 5, "f8": -14, "g1": -5, "g2": 8, "g3": 21, "g4": 11, "g5": 29, "g6": 6, "g7": -14, "g8": 1, "h1": -53, "h2": -15, "h3": -7, "h4": -5, "h5": -12, "h6": -16, "h7": -17, "h8": -48}
        self.whiteKnightMid = {"a1": -175, "a2": -77, "a3": -61, "a4": -35, "a5": -34, "a6": -9, "a7": -67, "a8": -201, "b1": -92, "b2": -42, "b3": -17, "b4": 8, "b5": 13, "b6": 22, "b7": -27, "b8": -83, "c1": -74, "c2": -27, "c3": 6, "c4": 40, "c5": 44, "c6": 58, "c7": 4, "c8": -56, "d1": -73, "d2": -15, "d3": 12, "d4": 49, "d5": 51, "d6": 53, "d7": 37, "d8": -26, "e1": -73, "e2": -15, "e3": 12, "e4": 49, "e5": 51, "e6": 53, "e7": 37, "e8": -26, "f1": -74, "f2": -27, "f3": 6, "f4": 40, "f5": 44, "f6": 58, "f7": 4, "f8": -56, "g1": -92, "g2": -41, "g3": -17, "g4": 8, "g5": 13, "g6": 22, "g7": -27, "g8": -83, "h1": -175, "h2": -77, "h3": -61, "h4": -35, "h5": -34, "h6": -9, "h7": -67, "h8": -201}
        self.whiteRookMid = {"a1": -31, "a2": -21, "a3": -25, "a4": -13, "a5": -27, "a6": -22, "a7": -2, "a8": -17, "b1": -20, "b2": -13, "b3": -11, "b4": -5, "b5": -15, "b6": -2, "b7": 12, "b8": -19, "c1": -14, "c2": -8, "c3": -1, "c4": -4, "c5": -4, "c6": 6, "c7": 16, "c8": -1, "d1": -5, "d2": 6, "d3": 3, "d4": -6, "d5": 3, "d6": 12, "d7": 18, "d8": 8, "e1": -5, "e2": 6, "e3": 3, "e4": -6, "e5": 3, "e6": 12, "e7": 18, "e8": 9, "f1": -14, "f2": -8, "f3": -1, "f4": -4, "f5": -4, "f6": 6, "f7": 16, "f8": -1, "g1": -20, "g2": -13, "g3": -11, "g4": -5, "g5": -15, "g6": -2, "g7": 12, "g8": -19, "h1": -31, "h2": -21, "h3": -25, "h4": -13, "h5": -27, "h6": -22, "h7": -2, "h8": -17}
        self.whiteQueenMid = {"a1": 3, "a2": -3, "a3": -3, "a4": 4, "a5": 8, "a6": -4, "a7": -5, "a8": -2, "b1": -5, "b2": 5, "b3": 6, "b4": 5, "b5": 14, "b6": 10, "b7": 6, "b8": -2, "c1": -5, "c2": 8, "c3": 13, "c4": 9, "c5": 12, "c6": 6, "c7": 10, "c8": 1, "d1": 4, "d2": 12, "d3": 7, "d4": 8, "d5": 5, "d6": 8, "d7": 8, "d8": -2, "e1": 4, "e2": 12, "e3": 7, "e4": 8, "e5": 5, "e6": 8, "e7": 8, "e8": -2, "f1": -5, "f2": 8, "f3": 13, "f4": 9, "f5": 12, "f6": 6, "f7": 10, "f8": 1, "g1": -5, "g2": 5, "g3": 6, "g4": 5, "g5": 14, "g6": 10, "g7": 6, "g8": -2, "h1": 3, "h2": -3, "h3": -3, "h4": 4, "h5": -4, "h6": -4, "h7": -5, "h8": -2}
        self.whiteKingMid = {"a1": 271, "a2": 278, "a3": 195, "a4": 164, "a5": 154, "a6": 123, "a7": 88, "a8": 59, "b1": 327, "b2": 303, "b3": 258, "b4": 190, "b5": 179, "b6": 145, "b7": 120, "b8": 89, "c1": 271, "c2": 234, "c3": 169, "c4": 138, "c5": 105, "c6": 81, "c7": 65, "c8": 45, "d1": 198, "d2": 179, "d3": 120, "d4": 98, "d5": 70, "d6": 31, "d7": 33, "d8": -1, "e1": 198, "e2": 179, "e3": 120, "e4": 98, "e5": 70, "e6": 31, "e7": 33, "e8": -1, "f1": 271, "f2": 234, "f3": 169, "f4": 138, "f5": 105, "f6": 81, "f7": 65, "f8": 45, "g1": 327, "g2": 303, "g3": 258, "g4": 190, "g5": 179, "g6": 145, "g7": 120, "g8": 89, "h1": 271, "h2": 278, "h3": 195, "h4": 164, "h5": 154, "h6": 123, "h7": 88, "h8": 59}


        self.blackPawnMid = {"a8": 0, "a7": 3, "a6": -9, "a5": -4, "a4": 13, "a3": 5, "a2": -7, "a1": 0, "b8": 0, "b7": 3, "b6": -15, "b5": -23, "b4": -2, "b3": -12, "b2": 7, "b1": 0, "c8": 0, "c7": 10, "c6": 11, "c5": 6, "c4": -13, "c3": -7, "c2": -3, "c1": 0, "d8": 0, "d7": 19, "d6": 15, "d5": 20, "d4": 1, "d3": 22, "d2": -13, "d1": 0, "e8": 0, "e7": 16, "e6": 32, "e5": 40, "e4": 11, "e3": -8, "e2": 5, "e1": 0, "f8": 0, "f7": 19, "f6": 22, "f5": 17, "f4": -2, "f3": -5, "f2": -16, "f1": 0, "g8": 0, "g7": 7, "g6": 5, "g5": 4, "g4": -13, "g3": -15, "g2": 10, "g1": 0, "h8": 0, "h7": -5, "h6": -22, "h5": -8, "h4": 5, "h3": -8, "h2": -5, "h1": 0}
        self.blackBishopMid = {"a8": -53, "a7": -15, "a6": -7, "a5": -5, "a4": -12, "a3": -16, "a2": -17, "a1": -48, "b8": -5, "b7": 8, "b6": 21, "b5": 11, "b4": 29, "b3": 6, "b2": -14, "b1": 1, "c8": -8, "c7": 19, "c6": -5, "c5": 25, "c4": 22, "c3": 1, "c2": 5, "c1": -14, "d8": -23, "d7": 4, "d6": 17, "d5": 39, "d4": 31, "d3": 11, "d2": 6, "d1": -23, "e8": -23, "e7": 4, "e6": 17, "e5": 39, "e4": 31, "e3": 11, "e2": 4, "e1": -23, "f8": -8, "f7": 19, "f6": -5, "f5": 25, "f4": 22, "f3": 1, "f2": 5, "f1": -14, "g8": -5, "g7": 8, "g6": 21, "g5": 11, "g4": 29, "g3": 6, "g2": -14, "g1": 1, "h8": -53, "h7": -15, "h6": -7, "h5": -5, "h4": -12, "h3": -16, "h2": -17, "h1": -48}
        self.blackKnightMid = {"a8": -175, "a7": -77, "a6": -61, "a5": -35, "a4": -34, "a3": -9, "a2": -67, "a1": -201, "b8": -92, "b7": -42, "b6": -17, "b5": 8, "b4": 13, "b3": 22, "b2": -27, "b1": -83, "c8": -74, "c7": -27, "c6": 6, "c5": 40, "c4": 44, "c3": 58, "c2": 4, "c1": -56, "d8": -73, "d7": -15, "d6": 12, "d5": 49, "d4": 51, "d3": 53, "d2": 37, "d1": -26, "e8": -73, "e7": -15, "e6": 12, "e5": 49, "e4": 51, "e3": 53, "e2": 37, "e1": -26, "f8": -74, "f7": -27, "f6": 6, "f5": 40, "f4": 44, "f3": 58, "f2": 4, "f1": -56, "g8": -92, "g7": -41, "g6": -17, "g5": 8, "g4": 13, "g3": 22, "g2": -27, "g1": -83, "h8": -175, "h7": -77, "h6": -61, "h5": -35, "h4": -34, "h3": -9, "h2": -67, "h1": -201}
        self.blackRookMid = {"a8": -31, "a7": -21, "a6": -25, "a5": -13, "a4": -27, "a3": -22, "a2": -2, "a1": -17, "b8": -20, "b7": -13, "b6": -11, "b5": -5, "b4": -15, "b3": -2, "b2": 12, "b1": -19, "c8": -14, "c7": -8, "c6": -1, "c5": -4, "c4": -4, "c3": 6, "c2": 16, "c1": -1, "d8": -5, "d7": 6, "d6": 3, "d5": -6, "d4": 3, "d3": 12, "d2": 18, "d1": 8, "e8": -5, "e7": 6, "e6": 3, "e5": -6, "e4": 3, "e3": 12, "e2": 18, "e1": 9, "f8": -14, "f7": -8, "f6": -1, "f5": -4, "f4": -4, "f3": 6, "f2": 16, "f1": -1, "g8": -20, "g7": -13, "g6": -11, "g5": -5, "g4": -15, "g3": -2, "g2": 12, "g1": -19, "h8": -31, "h7": -21, "h6": -25, "h5": -13, "h4": -27, "h3": -22, "h2": -2, "h1": -17}
        self.blackQueenMid = {"a8": 3, "a7": -3, "a6": -3, "a5": 4, "a4": 8, "a3": -4, "a2": -5, "a1": -2, "b8": -5, "b7": 5, "b6": 6, "b5": 5, "b4": 14, "b3": 10, "b2": 6, "b1": -2, "c8": -5, "c7": 8, "c6": 13, "c5": 9, "c4": 12, "c3": 6, "c2": 10, "c1": 1, "d8": 4, "d7": 12, "d6": 7, "d5": 8, "d4": 5, "d3": 8, "d2": 8, "d1": -2, "e8": 4, "e7": 12, "e6": 7, "e5": 8, "e4": 5, "e3": 8, "e2": 8, "e1": -2, "f8": -5, "f7": 8, "f6": 13, "f5": 9, "f4": 12, "f3": 6, "f2": 10, "f1": 1, "g8": -5, "g7": 5, "g6": 6, "g5": 5, "g4": 14, "g3": 10, "g2": 6, "g1": -2, "h8": 3, "h7": -3, "h6": -3, "h5": 4, "h4": -4, "h3": -4, "h2": -5, "h1": -2}
        self.blackKingMid = {"a8": 271, "a7": 278, "a6": 195, "a5": 164, "a4": 154, "a3": 123, "a2": 88, "a1": 59, "b8": 327, "b7": 303, "b6": 258, "b5": 190, "b4": 179, "b3": 145, "b2": 120, "b1": 89, "c8": 271, "c7": 234, "c6": 169, "c5": 138, "c4": 105, "c3": 81, "c2": 65, "c1": 45, "d8": 198, "d7": 179, "d6": 120, "d5": 98, "d4": 70, "d3": 31, "d2": 33, "d1": -1, "e8": 198, "e7": 179, "e6": 120, "e5": 98, "e4": 70, "e3": 31, "e2": 33, "e1": -1, "f8": 271, "f7": 234, "f6": 169, "f5": 138, "f4": 105, "f3": 81, "f2": 65, "f1": 45, "g8": 327, "g7": 303, "g6": 258, "g5": 190, "g4": 179, "g3": 145, "g2": 120, "g1": 89, "h8": 271, "h7": 278, "h6": 195, "h5": 164, "h4": 154, "h3": 123, "h2": 88, "h1": 59}


        #End Game
        self.whitePawnEnd = {"a1": 0, "a2": -10, "a3": -10, "a4": 6, "a5": 10, "a6": 28, "a7": 1, "a8": 0, "b1": 0, "b2": -6, "b3": -10, "b4": -2, "b5": 5, "b6": 20, "b7": -11, "b8": 0, "c1": 0, "c2": 10, "c3": -10, "c4": -8, "c5": 4, "c6": 21, "c7": 12, "c8": 0, "d1": 0, "d2": 0, "d3": 4, "d4": -4, "d5": -5, "d6": 28, "d7": 21, "d8": 0, "e1": 0, "e2": 14, "e3": 4, "e4": -13, "e5": -5, "e6": 30, "e7": 25, "e8": 0, "f1": 0, "f2": 7, "f3": 3, "f4": -12, "f5": -5, "f6": 7, "f7": 19, "f8": 0, "g1": 0, "g2": -5, "g3": -6, "g4": -10, "g5": 14, "g6": 6, "g7": 4, "g8": 0, "h1": 0, "h2": -19, "h3": -4, "h4": -9, "h5": 9, "h6": 13, "h7": 7, "h8": 0}
        self.whiteBishopEnd = {"a1": -57, "a2": -37, "a3": -16, "a4": -20, "a5": -17, "a6": -30, "a7": -31, "a8": -46, "b1": -30, "b2": -13, "b3": -1, "b4": -6, "b5": -1, "b6": 6, "b7": -20, "b8": -42, "c1": -37, "c2": -17, "c3": -2, "c4": 37, "c5": -14, "c6": 4, "c7": -1, "c8": -37, "d1": -12, "d2": 1, "d3": 10, "d4": 17, "d5": 15, "d6": 6, "d7": 1, "d8": -24, "e1": -12, "e2": 1, "e3": 10, "e4": 17, "e5": 15, "e6": 6, "e7": 1, "e8": -24, "f1": -37, "f2": -17, "f3": -2, "f4": 0, "f5": -14, "f6": 4, "f7": -1, "f8": -37, "g1": -30, "g2": -13, "g3": -1, "g4": -6, "g5": -1, "g6": 6, "g7": -20, "g8": -42, "h1": -57, "h2": -37, "h3": -16, "h4": -20, "h5": -17, "h6": -30, "h7": -31, "h8": -46}
        self.whiteKnightEnd = {"a1": -175, "a2": -77, "a3": -61, "a4": -35, "a5": -34, "a6": -9, "a7": -67, "a8": -201, "b1": -92, "b2": -42, "b3": -17, "b4": 8, "b5": 13, "b6": 22, "b7": -27, "b8": -83, "c1": -74, "c2": -27, "c3": 6, "c4": 40, "c5": 44, "c6": 58, "c7": 4, "c8": -56, "d1": -73, "d2": -15, "d3": 12, "d4": 49, "d5": 51, "d6": 53, "d7": 37, "d8": -26, "e1": -73, "e2": -15, "e3": 12, "e4": 49, "e5": 51, "e6": 53, "e7": 37, "e8": -26, "f1": -74, "f2": -27, "f3": 6, "f4": 40, "f5": 44, "f6": 58, "f7": 4, "f8": -56, "g1": -92, "g2": -41, "g3": -17, "g4": 8, "g5": 13, "g6": 22, "g7": -27, "g8": -83, "h1": -175, "h2": -77, "h3": -61, "h4": -35, "h5": -34, "h6": -9, "h7": -67, "h8": -201}
        self.whiteRookEnd = {"a1": -9, "a2": -12, "a3": 6, "a4": -6, "a5": -5, "a6": 6, "a7": 4, "a8": 18, "b1": -13, "b2": -9, "b3": -8, "b4": 1, "b5": 8, "b6": 1, "b7": 5, "b8": 18, "c1": -10, "c2": -1, "c3": -2, "c4": -9, "c5": 7, "c6": -7, "c7": 20, "c8": 19, "d1": -9, "d2": -2, "d3": -6, "d4": 7, "d5": -6, "d6": 10, "d7": -5, "d8": 13, "e1": -9, "e2": -2, "e3": -6, "e4": 7, "e5": -6, "e6": 10, "e7": -5, "e8": 13, "f1": -10, "f2": -1, "f3": -2, "f4": -9, "f5": 7, "f6": -7, "f7": 20, "f8": 19, "g1": -13, "g2": -9, "g3": -8, "g4": 1, "g5": 8, "g6": 1, "g7": 5, "g8": 5, "h1": -9, "h2": -12, "h3": 6, "h4": -6, "h5": -5, "h6": 6, "h7": 4, "h8": 18}
        self.whiteQueenEnd = {"a1": -69, "a2": -55, "a3": -39, "a4": -23, "a5": -29, "a6": -38, "a7": -50, "a8": -75, "b1": -57, "b2": -31, "b3": -18, "b4": -3, "b5": -6, "b6": -18, "b7": -27, "b8": -52, "c1": -47, "c2": -22, "c3": -9, "c4": 13, "c5": 9, "c6": -12, "c7": -24, "c8": -43, "d1": -26, "d2": -4, "d3": 3, "d4": 24, "d5": 21, "d6": 1, "d7": -8, "d8": -36, "e1": -26, "e2": -4, "e3": 3, "e4": 24, "e5": 21, "e6": 1, "e7": -8, "e8": -36, "f1": -47, "f2": -22, "f3": -9, "f4": 13, "f5": 9, "f6": -12, "f7": -24, "f8": -43, "g1": -57, "g2": -31, "g3": -18, "g4": -3, "g5": -6, "g6": -18, "g7": -27, "g8": -52, "h1": -69, "h2": -55, "h3": -39, "h4": -23, "h5": -29, "h6": -38, "h7": -50, "h8": -75}
        self.whtieKingEnd = {"a1": 1, "a2": 53, "a3": 88, "a4": 103, "a5": 96, "a6": 92, "a7": 47, "a8": 11, "b1": 45, "b2": 100, "b3": 130, "b4": 156, "b5": 166, "b6": 172, "b7": 121, "b8": 59, "c1": 85, "c2": 133, "c3": 169, "c4": 172, "c5": 199, "c6": 184, "c7": 116, "c8": 73, "d1": 76, "d2": 135, "d3": 175, "d4": 172, "d5": 199, "d6": 191, "d7": 131, "d8": 78, "e1": 76, "e2": 135, "e3": 175, "e4": 172, "e5": 199, "e6": 191, "e7": 131, "e8": 78, "f1": 85, "f2": 133, "f3": 169, "f4": 172, "f5": 199, "f6": 184, "f7": 116, "f8": 73, "g1": 45, "g2": 100, "g3": 130, "g4": 156, "g5": 166, "g6": 172, "g7": 121, "g8": 59, "h1": 1, "h2": 53, "h3": 88, "h4": 103, "h5": 96, "h6": 92, "h7": 47, "h8": 11}


        self.blackPawnEnd = {"a8": 0, "a7": -10, "a6": -10, "a5": 6, "a4": 10, "a3": 28, "a2": 1, "a1": 0, "b8": 0, "b7": -6, "b6": -10, "b5": -2, "b4": 5, "b3": 20, "b2": -11, "b1": 0, "c8": 0, "c7": 10, "c6": -10, "c5": -8, "c4": 4, "c3": 21, "c2": 12, "c1": 0, "d8": 0, "d7": 0, "d6": 4, "d5": -4, "d4": -5, "d3": 28, "d2": 21, "d1": 0, "e8": 0, "e7": 14, "e6": 4, "e5": -13, "e4": -5, "e3": 30, "e2": 25, "e1": 0, "f8": 0, "f7": 7, "f6": 3, "f5": -12, "f4": -5, "f3": 7, "f2": 19, "f1": 0, "g8": 0, "g7": -5, "g6": -6, "g5": -10, "g4": 14, "g3": 6, "g2": 4, "g1": 0, "h8": 0, "h7": -19, "h6": -4, "h5": -9, "h4": 9, "h3": 13, "h2": 7, "h1": 0}
        self.blackBishopEnd = {"a8": -57, "a7": -37, "a6": -16, "a5": -20, "a4": -17, "a3": -30, "a2": -31, "a1": -46, "b8": -30, "b7": -13, "b6": -1, "b5": -6, "b4": -1, "b3": 6, "b2": -20, "b1": -42, "c8": -37, "c7": -17, "c6": -2, "c5": 37, "c4": -14, "c3": 4, "c2": -1, "c1": -37, "d8": -12, "d7": 1, "d6": 10, "d5": 17, "d4": 15, "d3": 6, "d2": 1, "d1": -24, "e8": -12, "e7": 1, "e6": 10, "e5": 17, "e4": 15, "e3": 6, "e2": 1, "e1": -24, "f8": -37, "f7": -17, "f6": -2, "f5": 0, "f4": -14, "f3": 4, "f2": -1, "f1": -37, "g8": -30, "g7": -13, "g6": -1, "g4": -6, "g3": -1, "g2": -20, "g1": -42, "h8": -57, "h7": -37, "h6": -16, "h5": -20, "h4": -17, "h3": -30, "h2": -31, "h1": -46}
        self.blackKnightEnd = {"a8": -175, "a7": -77, "a6": -61, "a5": -35, "a4": -34, "a3": -9, "a2": -67, "a1": -201, "b8": -92, "b7": -42, "b6": -17, "b5": 8, "b4": 13, "b3": 22, "b2": -27, "b1": -83, "c8": -74, "c7": -27, "c6": 6, "c5": 40, "c4": 44, "c3": 58, "c2": 4, "c1": -56, "d8": -73, "d7": -15, "d6": 12, "d5": 49, "d4": 51, "d3": 53, "d2": 37, "d1": -26, "e8": -73, "e7": -15, "e6": 12, "e5": 49, "e4": 51, "e3": 53, "e2": 37, "e1": -26, "f8": -74, "f7": -27, "f6": 6, "f5": 40, "f4": 44, "f3": 58, "f2": 4, "f1": -56, "g8": -92, "g7": -41, "g6": -17, "g5": 8, "g4": 13, "g3": 22, "g2": -27, "g1": -83, "h8": -175, "h7": -77, "h6": -61, "h5": -35, "h4": -34, "h3": -9, "h2": -67, "h1": -201}
        self.blackRookEnd = {"a8": -9, "a7": -12, "a6": 6, "a5": -6, "a4": -5, "a3": 6, "a2": 4, "a1": 18, "b8": -13, "b7": -9, "b6": -8, "b5": 1, "b4": 8, "b3": 1, "b2": 5, "b1": 18, "c8": -10, "c7": -1, "c6": -2, "c5": -9, "c4": 7, "c3": -7, "c2": 20, "c1": 19, "d8": -9, "d7": -2, "d6": -6, "d5": 7, "d4": -6, "d3": 10, "d2": -5, "d1": 13, "e8": -9, "e7": -2, "e6": -6, "e5": 7, "e4": -6, "e3": 10, "e2": -5, "e1": 13, "f8": -10, "f7": -1, "f6": -2, "f5": -9, "f4": 7, "f3": -7, "f2": 20, "f1": 19, "g8": -13, "g7": -9, "g6": -8, "g5": 1, "g4": 8, "g3": 1, "g2": 5, "g1": 5, "h8": -9, "h7": -12, "h6": 6, "h5": -6, "h4": -5, "h3": 6, "h2": 4, "h1": 18}
        self.blackQueenEnd = {"a8": -69, "a7": -55, "a6": -39, "a5": -23, "a4": -29, "a3": -38, "a2": -50, "a1": -75, "b8": -57, "b7": -31, "b6": -18, "b5": -3, "b4": -6, "b3": -18, "b2": -27, "b1": -52, "c8": -47, "c7": -22, "c6": -9, "c5": 13, "c4": 9, "c3": -12, "c2": -24, "c1": -43, "d8": -26, "d7": -4, "d6": 3, "d5": 24, "d4": 21, "d3": 1, "d2": -8, "d1": -36, "e8": -26, "e7": -4, "e6": 3, "e5": 24, "e4": 21, "e3": 1, "e2": -8, "e1": -36, "f8": -47, "f7": -22, "f6": -9, "f5": 13, "f4": 9, "f3": -12, "f2": -24, "f1": -43, "g8": -57, "g7": -31, "g6": -18, "g5": -3, "g4": -6, "g3": -18, "g2": -27, "g1": -52, "h8": -69, "h7": -55, "h6": -39, "h5": -23, "h4": -29, "h3": -38, "h2": -50, "h1": -75}
        self.blackKingEnd={"a8": 1, "a7": 53, "a6": 88, "a5": 103, "a4": 96, "a3": 92, "a2": 47, "a1": 11, "b8": 45, "b7": 100, "b6": 130, "b5": 156, "b4": 166, "b3": 172, "b2": 121, "b1": 59, "c8": 85, "c7": 133, "c6": 169, "c5": 172, "c4": 199, "c3": 184, "c2": 116, "c1": 73, "d8": 76, "d7": 135, "d6": 175, "d5": 172, "d4": 199, "d3": 191, "d2": 131, "d1": 78, "e8": 76, "e7": 135, "e6": 175, "e5": 172, "e4": 199, "e3": 191, "e2": 131, "e1": 78, "f8": 85, "f7": 133, "f6": 169, "f5": 172, "f4": 199, "f3": 184, "f2": 116, "f1": 73, "g8": 45, "g7": 100, "g6": 130, "g5": 156, "g4": 166, "g3": 172, "g2": 121, "g1": 59, "h8": 1, "h7": 53, "h6": 88, "h5": 103, "h4": 96, "h3": 92, "h2": 47, "h1": 11}


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
            #print("White Knight Moving")
            del whiteP.KnightPositions[OldPosition]
            whiteP.KnightPositions[NewPosition]=NewPosition
            # print("Move Dict")
            # print(whiteP.KnightPositions)
            # print("Value Updated")
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
        
        if MoveType==CastlingLong:
            del whiteP.KingPositions["e1"]
            del whiteP.RookPositions["a1"]
            whiteP.KingPositions["c1"]="c1"
            whiteP.RookPositions["d1"]="d1"

        if MoveType==CastlingShort:
            del whiteP.KingPositions["e1"]
            del whiteP.RookPositions["h1"]
            whiteP.KingPositions["g1"]="g1"
            whiteP.RookPositions["f1"]="f1"

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
        elif MoveType==Move:
            del blackP.KingPositions[OldPosition]
            blackP.KingPositions[NewPosition] = NewPosition
        
        elif MoveType==CastlingLong:
            print("Castling Long")
            print(blackP.KingPositions)
            print(blackP.RookPositions)
            del blackP.KingPositions["e8"]
            del blackP.RookPositions["a8"]
            blackP.KingPositions["c8"]=["c8"]
            blackP.RookPositions["d8"]="d8"

        elif MoveType==CastlingShort:
            print("Castling Long")
            print(blackP.KingPositions)
            print(blackP.RookPositions)
            del blackP.KingPositions["e8"]
            del blackP.RookPositions["h8"]
            blackP.KingPositions["g7"]="g7"
            blackP.RookPositions["f7"]="f7"
            

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

        self.PawnValue = 124
        self.RookValue = 1276
        self.KnightValue = 781
        self.BishopValue = 825
        self.QueenValue = 2538
        self.KingValue = 0

        # self.PawnValueBlack = 124
        # self.RookValueBlack = -1276
        # self.KnightValueBlack = -781
        # self.BishopValueBlack = -825
        # self.QueenValueBlack  =-2538
        # self.KingValueBlack = 0

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
            try:
                x = int(x)
                if x >= 1 and x<=10:
                    return x
                print("Invalid entry")
            except:
                pass

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
    

    def printPieces(self,whitePieces,blackPieces):
        print("White Pieces:")
        print("Pawn")
        print(whitePieces.PawnPositions)
        print("Bishop")
        print(whitePieces.BishopPositions)
        print("Knight")
        print(whitePieces.KnightPositions)
        print("Rook")
        print(whitePieces.RookPositions)
        print("Queen")
        print(whitePieces.QueenPositions)

        print("Black Pieces:")
        print("Pawn")
        print(blackPieces.PawnPositions)
        print("Bishop")
        print(blackPieces.BishopPositions)
        print("Knight")
        print(blackPieces.KnightPositions)
        print("Rook")
        print(blackPieces.RookPositions)
        print("Queen")
        print(blackPieces.QueenPositions)

    def listSort(self,allMoves):
        
        for i in range(len(allMoves)):
            if("e" in allMoves[i] or "d" in allMoves[i] or "f" in allMoves[i] or "c" in allMoves[i]):
                allMoves = [allMoves[i]] + allMoves[:i] + allMoves[i+1:]
            if("a" in allMoves[i] or "h" in allMoves[i] or "b" in allMoves[i] or "g" in allMoves[i]):
                allMoves.append(allMoves.pop(allMoves.index(allMoves[i])))
        
             
        for i in range(len(allMoves)):
            if("x" in allMoves[i]):
                allMoves = [allMoves[i]] + allMoves[:i] + allMoves[i+1:]
            
        for i in range(len(allMoves)):
            if(allMoves[i] == "="):
                allMoves = [allMoves[i]] + allMoves[:i] + allMoves[i+1:]
        
        for i in range(len(allMoves)):
            if(allMoves[i] == "+"):
                allMoves = [allMoves[i]] + allMoves[:i] + allMoves[i+1:]
               
        for i in range(len(allMoves)):
            if(allMoves[i] == "#"):
                allMoves = [allMoves[i]] + allMoves[:i] + allMoves[i+1:]
        return allMoves

    def SquareUpdating(self,Move,oldSquare,newSquare,whitePieces,blackPieces,colour):
        if(colour=="White"):              
                if(oldSquare in whitePieces.PawnPositions):
                    if(Capture==Move):
                     whitePieces,blackPieces = BoardSetUp("White").UpdateWhitePawnPosition(Capture,oldSquare,newSquare,whitePieces,blackPieces)
                    elif(Promotion==Move):
                      whitePieces,blackPieces = BoardSetUp("White").UpdateWhitePawnPosition(Promotion,oldSquare,newSquare,whitePieces,blackPieces)
                    else:
                       whitePieces,blackPieces = BoardSetUp("White").UpdateWhitePawnPosition(Move,oldSquare,newSquare,whitePieces,blackPieces)
                       
                elif(Move==CastlingLong or Move==CastlingShort):
                    if(CastlingShort==Move):
                       whitePieces,blackPieces = BoardSetUp("White").UpdateWhiteKingPosition(CastlingShort,oldSquare,newSquare,whitePieces,blackPieces)
                    elif(CastlingLong==Move):
                        whitePieces,blackPieces = BoardSetUp("White").UpdateWhiteKingPosition(CastlingLong,oldSquare,newSquare,whitePieces,blackPieces)  

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

                elif(Move==CastlingLong or Move==CastlingShort):
                        if(CastlingShort==Move):
                            whitePieces,blackPieces = BoardSetUp("Black").UpdateBlackKingPosition(CastlingShort,oldSquare,newSquare,whitePieces,blackPieces)
                        elif(CastlingLong==Move):
                            whitePieces,blackPieces = BoardSetUp("Black").UpdateBlackKingPosition(CastlingLong,oldSquare,newSquare,whitePieces,blackPieces) 
                
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
                    else:
                        whitePieces,blackPieces = BoardSetUp("Black").UpdateBlackKingPosition(Move,oldSquare,newSquare,whitePieces,blackPieces)

        return whitePieces, blackPieces
       
    def leadUpdates(self,board,colour,oldWhite,oldBlack,updatingMove):
        copiedWhite = copy.deepcopy(oldWhite)
        copiedBlack = copy.deepcopy(oldBlack)
        oldSquare=boardLocations.placesDictionary[board.peek().from_square]
        newSquare=boardLocations.placesDictionary[board.peek().to_square]         
        if Capturing in updatingMove:
            moveType=Capture
        elif Promotion in updatingMove:
            moveType=Promotion
        elif CastlingLong in updatingMove:
            moveType = CastlingLong
        elif CastlingShort in updatingMove:
            moveType = CastlingShort
        else:
            moveType = Move                           
        tempW,tempB=self.SquareUpdating(moveType,oldSquare,newSquare,copiedWhite,copiedBlack,colour)
        return tempW, tempB

    def getMoveList(self,board):
        moves = board.legal_moves
        moves = str(moves)
        split_string = moves.split("(")
        split_string2 = split_string[1].split(")")
        allComputerMoves = split_string2[0].split(", ")
        return allComputerMoves

   
    def alphaBetaMaxWhite(self,board,alpha,beta,whitePieces,blackPieces,depth,move):
            allComputerMoves = self.getMoveList(board)         
            bestMove=""
            if depth == 3:
                value = self.calculateMoveValue(whitePieces,blackPieces,Black,move)
                return value
            try:                    
                allComputerMoves=self.listSort(allComputerMoves)
                for move in allComputerMoves:                
                    board.push_san(move)
                               
                    
                    copiedWhite,copiedBlack=self.leadUpdates(board,White,whitePieces,blackPieces,move)
                    if "#" not in move:               
                        value = self.alphaBetaMiniBlack(board,alpha,beta,copiedWhite,copiedBlack,depth+1,move)
                    else:
                        value = math.inf
                        bestMove=move
                        break
                    
                    board.pop()                                        
                    if value>=beta:
                        if depth!=0:
                            return beta
                        if depth==0:
                            return move

                    if value>alpha:
                        alpha=value 
                        if depth==0:
                            bestMove=move                       
                
                if depth!=0:               
                    return alpha
                if depth==0:
                    return bestMove

            except Exception as e:
                print("Error in AlphaBeta White Move")
                print(depth)
                print(e)
                sys.exit()
    
    def alphaBetaMiniBlack(self,board,alpha,beta,whitePieces,blackPieces,depth,move):
        allComputerMoves = self.getMoveList(board)
        bestMove=""
        if depth == 3:
            value = self.calculateMoveValue(whitePieces,blackPieces,White,move)
            return -value
        try:
            allComputerMoves=self.listSort(allComputerMoves)
            for move in allComputerMoves:               
                board.push_san(move)
                
                copiedWhite,copiedBlack = self.leadUpdates(board,Black,whitePieces,blackPieces,move)               
                if "#" not in move:
                    value = self.alphaBetaMaxWhite(board,alpha,beta,copiedWhite,copiedBlack,depth+1,move)
                else:
                    value = -math.inf
                    if depth==0:
                        bestMove=move
                        break
                
                board.pop()
                if depth==0:
                    print("Start-------")
                    print(move)
                    print(value)
                    print("----End")


                if value<=alpha:
                    if depth!=0:
                        return alpha
                    if depth==0:
                        return move              
                if value<beta:
                    beta=value
                    if depth==0:
                        bestMove=move
            if depth!=0:
                return beta
            if depth == 0:
                return bestMove

        except Exception as e:
            print("Error in AlphaBeta Black Move")
            print(e)
            print(depth)
            sys.exit()

  


    def calculateMoveValue(self,WhitePieces,BlackPieces,Colour,move):
        whiteValue=0
        blackValue=0
        if "#" in move and Colour==White:
             whiteValue+=math.inf

        elif "#" in move and Colour==Black:
             blackValue+=math.inf

        elif "O-O-O" in move and Colour == White:
             whiteValue+=50

        elif "O-O-O" in move and Colour == Black:
             blackValue+=50

        elif "O-O" in move and Colour == White:
             whiteValue+=50

        elif "O-O" in move and Colour == Black:
             blackValue+=50

        elif "=" in move and Colour == White:
             whiteValue+=25
        elif "=" in move and Colour == Black:
             blackValue+=25
        
        LateGame = False
        tempWhite, tempBlack = self.BoardValue(WhitePieces,BlackPieces,LateGame)
        whiteValue += tempWhite
        blackValue += tempBlack
        
        tempWhite, tempBlack = self.PiecesValue(WhitePieces,BlackPieces)
        whiteValue += tempWhite
        blackValue += tempBlack
        value = whiteValue-blackValue

        return value

    def BoardValue(self,WhitePieces,BlackPieces,LateGame):
        #This Method Working on
        Locations=BoardValues()
        valueWhite=0
        valueBlack=0        
        for i in WhitePieces.PawnPositions:
            valueWhite+=self.getValuePosition(White,1,LateGame,i,Locations) 
        for i in WhitePieces.RookPositions:
            valueWhite+=self.getValuePosition(White,4,LateGame,i,Locations)
            # print("Rook")
            # print(valueWhite)
        for i in WhitePieces.BishopPositions:
            valueWhite+=self.getValuePosition(White,3,LateGame,i,Locations)
        for i in WhitePieces.KnightPositions:
            valueWhite+=self.getValuePosition(White,2,LateGame,i,Locations)
        for i in WhitePieces.QueenPositions:
            valueWhite+=self.getValuePosition(White,5,LateGame,i,Locations)
        for i in WhitePieces.KingPositions:
            valueWhite+=self.getValuePosition(White,6,LateGame,i,Locations)

        for i in BlackPieces.PawnPositions:
            valueBlack+=self.getValuePosition(Black,1,LateGame,i,Locations)       
        for i in BlackPieces.RookPositions:
            valueBlack+=self.getValuePosition(Black,4,LateGame,i,Locations)       
        for i in BlackPieces.BishopPositions:
            valueBlack+=self.getValuePosition(Black,3,LateGame,i,Locations)           
        for i in BlackPieces.KnightPositions:
            valueBlack+=self.getValuePosition(Black,2,LateGame,i,Locations)
        for i in BlackPieces.QueenPositions:
            valueBlack+=self.getValuePosition(Black,5,LateGame,i,Locations)
        for i in BlackPieces.KingPositions:
            valueBlack+=self.getValuePosition(Black,6,LateGame,i,Locations)

        return valueWhite,valueBlack

    def PiecesValue(self,WhitePieces,BlackPieces):
        pieceValues=Evaluations()

        pawnCountWhiteValue = len(WhitePieces.PawnPositions)*pieceValues.PawnValue
        pawnCountBlackValue = len(BlackPieces.PawnPositions)*pieceValues.PawnValue

        bishopCountWhiteValue = len(WhitePieces.BishopPositions)*pieceValues.BishopValue
        bishopCountBlackValue = len(BlackPieces.BishopPositions)*pieceValues.BishopValue

        knightCountWhiteValue = len(WhitePieces.KnightPositions)*pieceValues.KnightValue
        knightCountBlackValue = len(BlackPieces.KnightPositions)*pieceValues.KnightValue

        rookCountWhiteValue = len(WhitePieces.RookPositions)*pieceValues.RookValue
        rookCountBlackValue = len(BlackPieces.RookPositions)*pieceValues.RookValue

        queenCountWhiteValue = len(WhitePieces.QueenPositions)*pieceValues.RookValue
        queenCountBlackValue = len(BlackPieces.QueenPositions)*pieceValues.RookValue


        whiteValue = pawnCountWhiteValue + bishopCountWhiteValue + knightCountWhiteValue + rookCountWhiteValue + queenCountWhiteValue
        blackValue = pawnCountBlackValue + bishopCountBlackValue + knightCountBlackValue + rookCountBlackValue + queenCountBlackValue

        return whiteValue, blackValue

    def getValuePosition(self,Colour,PieceType,LateGame,Location,Locations):
        value = 0
        LateGame=False
        if Colour==White and LateGame==False:
            if PieceType==1:
                value = Locations.whitePawnMid[Location]
            elif PieceType==2:
                value = Locations.whiteKnightMid[Location]
            elif PieceType==3:
                value = Locations.whiteBishopMid[Location]
            elif PieceType==4:
                value = Locations.whiteRookMid[Location]
            elif PieceType==5:
                value = Locations.whiteQueenMid[Location]
            elif PieceType==6:
                value = Locations.whiteKingMid[Location]



        elif Colour==White and LateGame==True:
            if PieceType==1:
                value = Locations.whitePawnEnd[Location]
            elif PieceType == 2:
                value = Locations.whiteKnightEnd[Location]
            elif PieceType == 3:
                value = Locations.whiteBishopEnd[Location]
            elif PieceType == 4:
                value = Locations.whiteRookEnd[Location]
            elif PieceType == 5:
                value = Locations.whiteQueenEnd[Location]
            elif PieceType == 6:
                value = Locations.whiteKnightEnd[Location]

        
        elif Colour==Black and LateGame==False:
            if PieceType==1:
                value = Locations.blackPawnMid[Location]
            elif PieceType==2:
                value = Locations.blackKnightMid[Location]
            elif PieceType==3:
                value = Locations.blackBishopMid[Location]
            elif PieceType==4:
                value = Locations.blackRookMid[Location]
            elif PieceType==5:
                value = Locations.blackQueenMid[Location]
            elif PieceType==6:
                value = Locations.blackKingMid[Location]

        elif Colour==Black and LateGame==True:
            if PieceType==1:
                value = Locations.blackPawnMid[Location]
            elif PieceType == 2:
                value = Locations.blackKnightEnd[Location]
            elif PieceType == 3:
                value = Locations.blackBishopEnd[Location]
            elif PieceType == 4:
                value = Locations.blackRookEnd[Location]
            elif PieceType == 5:
                value = Locations.blackQueenEnd[Location]
            elif PieceType == 6:
                value = Locations.blackKingEnd[Location]

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
            whitePieces,blackPieces = MainAlgorthim.leadUpdates(board,BoardInformation.currentColour,whitePieces,blackPieces,move) 
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
                # bestMove,Zobrist, whitePieces, blackPieces = MainAlgorthim.PerformTree(board,BoardInformation,Setup,Zobrist,whitePieces,blackPieces)                                            
                if BoardInformation.currentColour == White:
                   bestMove = MainAlgorthim.alphaBetaMaxWhite(board,-math.inf,math.inf,whitePieces,blackPieces,0,"")
                elif BoardInformation.currentColour == Black:
                   bestMove = MainAlgorthim.alphaBetaMiniBlack(board,-math.inf,math.inf,whitePieces,blackPieces,0,"")
                
            # t1 = time.time()
            # print("Time Move")
            # print(t1-t0)
            print("Move Being Pushed")
            print(bestMove)          
            board.push_san(bestMove)
            BoardInformation.isGameOver(board,BoardInformation.currentColour)    
            whitePieces,blackPieces = MainAlgorthim.leadUpdates(board,BoardInformation.currentColour,whitePieces,blackPieces,bestMove)            
            BoardInformation.currentColour=White
            print("White Pieces: ")
            print(whitePieces.PawnPositions)
            print(whitePieces.KnightPositions)

            print("Black Pieces: ")
            print(blackPieces.PawnPositions)
            print(blackPieces.KnightPositions)

        BoardInformation.isGameOver(board,BoardInformation.currentColour)

