
from hamilton import cycle_generator

def main(width, height, start_position):
    actions = ["up", "left", "down", "right"]

    board = [[0 for i in range(width)] for j in range(height)]

    cycle = cycle_generator(board, start_position)
    cycle_pos = dict()
    for i in range(len(cycle)):
        cycle_pos[cycle[i]] = i

    length = 4


    while True:
        pass
        # if cycle_pos[neigh] > cycle_pos[head_pos] or cycle_pos[neigh] < cycle_pos[tail_pos]
        # prioritize moves that shorten manhattan distance to fruit.
        # prioritize moves that shorten manhattan distance to other snake head.