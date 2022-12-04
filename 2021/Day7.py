from collections import Counter
import statistics

lignes = [int(x) for x in open("Inputs/InputDay7.txt" ).read().strip().split(",")]
lignes.sort()

#J'ai décidé de prendre cette approche puisque je pensais que la force brute (2 boucles) n'allais pas être assez rapide, comme dans le Day6

sum = 0

med = int(statistics.median(lignes))

mid =  lignes[len(lignes)//2] ##utilisation de la mediane
for i in lignes:
        sum += abs(i-mid)

#print(sum)

#Partie 2 la regle a suivre est n*(n+1)/2 pour le cout d'un deplacement

best = 1e9
for i in range(len(lignes)):
    score = 0
    for x in lignes:
        n = abs(x-i)
        score += n*(n+1)/2
    if score < best:
        best = score

print(best) ##it works



