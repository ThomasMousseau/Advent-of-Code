import collections
import os.path

#path = os.getcwd() #get the current working directory
#INPUT_TXT = os.path.join(path, "InputsTestDay6.txt") ##local path not really good

#voici une autre facon que j'aimerais comprendre
#INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.txt') 

def ReadFileData(path):
    f = open(path, "r")
    return f.readlines()

pathData = "Inputs/InputDay6.txt" 

lignes = ReadFileData(pathData)

data = ''.join(str(item) for item in lignes)

numbers = collections.Counter(int(s) for s in data.strip().split(","))

for d in range(256):
    numbers2 = collections.Counter({8: numbers[0], 6: numbers[0]})
    #numbers2.update({k - 1: v for k, v in numbers.items() if k > 0})
    for k,v in numbers.items():
        if k > 0:
            numbers2[k - 1] += v
    numbers = numbers2

print(sum(numbers.values()))



#initialInput = [3,4,3,1,2]
#for i in range(0,80): ##very hard coded hay to to this
    #initialInput = [(n-1) % 7 if n < 8 else (n - 1) for n in initialInput] + [8] * initialInput.count(0)
    #print(len(initialInput))






