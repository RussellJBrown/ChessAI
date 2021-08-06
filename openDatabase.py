from os import listdir
from os.path import isfile, join
import json
import os

def openDatabaseStartingMove(openingMove):
    cwd = os.getcwd()+"/"+openingMove
    list = []
    onlyfile = listdir(cwd)

    for i in onlyfile:
        d2 = json.load(open(cwd+"/"+i))
        list.append(d2)
    return list




if __name__ == '__main__':
    list =  openDatabaseStartingMove("e4")
    print(list)
