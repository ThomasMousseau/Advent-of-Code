import os
print(os.listdir("2022/Inputs"))

with open("2022/Inputs/inputDay1.txt") as f:
        lines = f.read().strip().splitlines()

res = []
sum = 0;

for i in lines:
        if(i != ""):
                sum += int(i)
        else:
                res.append(sum)
                sum  = 0
res.sort()

print(res[-1] + res[-2] + res[-3])