def keysPrint(moveDict):
    moveList = moveDict.keys()
    for i in moveList:
        if "0" in i:
            value = moveDict[i] 