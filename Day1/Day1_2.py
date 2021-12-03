from Day1_1 import IncreaseNumber, ReadFileData

pathData  = "Day1/InputDay1_2.txt"

liste = ReadFileData(pathData)
listePar3 = []

for i in range(len(liste) - 2):
    listePar3.append(int(liste[i]) + int(liste[i+1]) + int(liste[i+2]))

print(IncreaseNumber(listePar3))