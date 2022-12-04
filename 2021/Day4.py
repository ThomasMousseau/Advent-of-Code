def ReadFileData(path):
    f = open(path, "r")
    return f.readlines()

pathData = "Inputs/InputDay4.txt" 

lignes = ReadFileData(pathData)

class Case:
    def __init__(self, number, marked, matrixPosition): #on va prendre les ccords matricielles et non les coords cartesiennes (alors 0,0 est en haut à gauche)
        self.number = number
        self.marked = marked
        self.matrixPosition = matrixPosition

class Board:
     def __init__(self, listCase, boardId):
         self.listCase = listCase
         self.boardId = boardId

numberDrawn = lignes[0].strip().split(",") ##IMP c'est une liste de string pas de int

rows = []
listOfRows = []
listOfBoard = []

numRow = 2


for k in range(int((len(lignes)-1) / 6)): #enumerate()
    for i in range(0, 5): 
        for j in range(0,5):
            rows.append(Case(lignes[numRow].strip().split()[j], False, (i,j)))

        listOfRows.append(rows) #make a deep copy
        rows.clear()
        numRow +=1

    numRow +=1
    listOfBoard.append(Board(listOfRows, k)) #make a deep copy of listOfRows
    listOfRows.clear()


print(listOfBoard)


def VerifiyWinningCondition():
    return 0