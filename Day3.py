#dirname("Day3/Input/InputDay3.txt")
import math

def ReadFileData(path):
    f = open(path, "r")
    return f.readlines()

pathData = "Inputs/InputDay3.txt" #le ../ sinigfie un étage plus haut soit vers les parents de ce fichiers

lignes = ReadFileData(pathData)

def SplitIntoChar(strBin): #joue le role du .split()
    return [char for char in strBin.strip()]

def Creation2DListChar(lines):
    
    return [[SplitIntoChar(lines[i])[j] for i in range(len(lines))] for j in range(len(lines[0].strip()))]


def FindMostRecurentChar(liste2DOfChar, charWanted, nonWantedChar):

    cpt1 = 0
    gamma = []

    for i in range(len(liste2DOfChar)):
        for j in range(len(liste2DOfChar[0])):
            if liste2DOfChar[i][j] == '1':
                cpt1 +=1  
            else: 
                cpt1 -= 1
        if cpt1 > 0:
            gamma.append(charWanted)
        else:
            gamma.append(nonWantedChar)
        cpt1 = 0
    
    return gamma


gammaRate = FindMostRecurentChar(Creation2DListChar(lignes),'1', '0') #gamma
print(FindMostRecurentChar(Creation2DListChar(lignes),'1', '0' ))
epsilonRate = FindMostRecurentChar(Creation2DListChar(lignes), '0', '1') #epsilon
print(FindMostRecurentChar(Creation2DListChar(lignes), '0', '1'))

def CreatingCleanBin(liste):
    s = 0
    liste.reverse() ## a la place de reverse j'aurais du faire [-1]
    for i in range(len(liste)):
        s+= int(liste[i]) * 2**i
    return s

print(CreatingCleanBin(gammaRate) * CreatingCleanBin(epsilonRate))

## PART 2

