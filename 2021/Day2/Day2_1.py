
##import sys
  
#sys.path.append(r"C:\Users\15146\Desktop\Advent_Of_Code_2021\Day1")
#from Day1_1 import ReadFileData

#Je voulais l'import de Day1, mais j'avais plusieurs problemes de path (en allant le chercher et en l'appelant)

listeForward = []
listeDown = []
listeUp = []

dictTmp = {}


def ReadFileData(path):
    f = open(path, "r")
    return f.readlines()

def CreationList(lignes):
    tmp = []
    for i in range(len(lignes)):
        tmp = lignes[i].split(" ") ##je peux surement changer cette condition
        if tmp[0].strip() == "forward":
            listeForward.append(int(tmp[1]))
        elif tmp[0].strip() == "down":
            listeDown.append(int(tmp[1]))
        else:
            listeUp.append(int(tmp[1]))

    return listeForward, listeDown, listeUp

def Summation(liste):
    cptTmp = 0
    for i in range(len(liste)):
        cptTmp += liste[i]
    return cptTmp


pathData = "Day2/InputDay2_1.txt"
lines = ReadFileData(pathData)

CreationList(lines)

print(Summation(listeForward) * ((Summation(listeDown) - (Summation(listeUp)))))

##Puisque maintenant l'orde change qqc, je dois changer mon code
def CalculateAim(lignes):
    aim  = 0
    depth = 0
    horizontalPos = 0   
    tmp = []

    for i in range(len(lignes)):
        tmp = lignes[i].split(" ") ##je peux surement changer cette condition
        if tmp[0].strip() == "forward":
            horizontalPos += int(tmp[1])
            depth += aim * int(tmp[1])
        elif tmp[0].strip() == "down":
            aim += int(tmp[1])
        else:
            aim -= int(tmp[1])

    return horizontalPos * depth

print(CalculateAim(lines))


