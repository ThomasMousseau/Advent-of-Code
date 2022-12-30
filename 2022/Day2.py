


def points_per_round(round_string):
    opponent_shape = map_input[round_string[0]]
    our_shape = map_input[round_string[2]]

    if opponent_shape == our_shape:
        return points_per_outcome['Draw'] + points_per_shape[our_shape]
    elif (opponent_shape, our_shape) in [('Paper', 'Rock'), ('Rock', 'Scissors'), ('Scissors', 'Paper')]:
        return points_per_outcome['Lose'] + points_per_shape[our_shape]
    else:
        return points_per_outcome['Win'] + points_per_shape[our_shape]

def points_per_round2(round_string):
    opponent_shape = map_input[round_string[0]]
    our_goal = map_input[round_string[2]]

    if (opponent_shape, our_goal) in [('Rock', 'Draw'), ('Paper', 'Lose'), ('Scissors', 'Win')]:
        return points_per_outcome[our_goal] + points_per_shape['Rock']
    elif (opponent_shape, our_goal) in [('Rock', 'Win'), ('Paper', 'Draw'), ('Scissors', 'Lose')]:
        return points_per_outcome[our_goal] + points_per_shape['Paper']
    else:
        return points_per_outcome[our_goal] + points_per_shape['Scissors']

with open("2022/Inputs/inputDay2.txt") as f:
        rounds = f.read().strip().splitlines()

map_input = {'A': 'Rock', 'B': 'Paper', 'C': 'Scissors', 'X': 'Lose', 'Y': 'Draw', 'Z': 'Win'}
points_per_shape = {'Rock': 1, 'Paper': 2, 'Scissors': 3}
points_per_outcome = {'Lose': 0, 'Draw': 3, 'Win': 6}

#print(sum([points_per_round(round_string) for round_string in rounds]))

print(sum([points_per_round2(round_string) for round_string in rounds])
)