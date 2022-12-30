with open("2022/Inputs/inputDay3.txt") as f:
        lines = f.read().strip().splitlines()
sum = 0

for line in lines:
    firstHalf = set(line[:len(line) // 2])
    secondHalf = set(line[len(line) // 2:])

    intersection = firstHalf.intersection(secondHalf)

    for elem in intersection:
        if elem.isupper():
            sum += ord(elem) - ord('A') + 27
        else:
            sum += ord(elem) - ord('a') + 1
print(sum)



