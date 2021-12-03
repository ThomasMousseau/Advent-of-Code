from os import path


pathData  = "Day1/InputDay1_1.txt"

def ReadFileData(path):
    f = open(path, "r")
    return f.readlines()
    
def IncreaseNumber(liste):
    cpt = 0

    for i in range(len(liste) - 1 ):
        if int(liste[i]) < int(liste[i+1]):
            cpt +=1
    return cpt

lines = ReadFileData(pathData)

print(IncreaseNumber(lines))

