def ReadFileData(path):
    f = open(path, "r")
    return f.readlines()

pathData = "../Input/InputDay3.txt"

lignes = ReadFileData(pathData)
