from random import randrange
import os
from pathlib import Path
import json

'''
def updateNew():

'''


def openDatabase():
    file = open("/home/russell/Downloads/scid.txt",'r')
    data = {}
    cwd = os.getcwd()+"/"

    Lines = file.readlines()
    for line in Lines:
        try:
            line = line.split('"')
            if line[2].isspace()==False:

                sep = '*'
                stripped = line[2].split(sep, 1)[0]

                stripped = stripped[1:]
                stripped = stripped.split(" ")

                #print("Opening")
                fileName = line[1].strip().replace(" ","")+".txt"
                #print(fileName)
                i=1
                data = {}
                folder = ""
                while(i < len(stripped)):
                    if i == 1:
                        name=stripped[i]
                        Path(cwd+name[2:]).mkdir(parents=True,exist_ok=True)
                        folder=name[2:]

                    if i%2!=0:
                        test = stripped[i]
                        data[str(i)+test[2:]] = test[2:]

                    else:
                        data[str(i)+stripped[i]]=stripped[i]

                    i+=1
                fileNames = cwd+folder+"/"+fileName
                with open(fileNames,'w') as tempFile:
                    tempFile.write(json.dumps(data))
                    print("Made File: ")
                    print(fileNames)

        except Exception as e:
            pass



if __name__ == '__main__':
    openDatabase()
