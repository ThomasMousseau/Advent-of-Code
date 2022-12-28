with open("2022/Inputs/inputDay2.txt") as f:
        rounds = f.read().strip().splitlines()

map_input = {'A': 'Rock', 'B': 'Paper', 'C': 'Scissors', 'X': 'Rock', 'Y': 'Paper', 'Z': 'Scissors'}
points_per_shape = {'Rock': 1, 'Paper': 2, 'Scissors': 3}
points_per_outcome = {'Lose': 0, 'Draw': 3, 'Win': 6}

#rounds = [entry.strip() for entry in lines]

print("")
