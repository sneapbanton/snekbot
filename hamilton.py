import sys

def print_board(board):
    print("-"*len(board[0]*2))
    for r in board:
        row = ""
        for c in r:
            row += str(c) + " "
        print(row)
    print("-"*len(board[0]*2))

def unvisited_neighbours(board, visited, pos):
    possible = []
    width = len(board[0])
    height = len(board)
    r, c = map(int, pos)
    if r > 0 and (r-1 ,c) not in visited:
        possible.append((r-1 ,c))
    if c > 0 and (r ,c-1) not in visited:
        possible.append((r ,c-1))
    if r < height-1 and (r+1 ,c) not in visited:
        possible.append((r+1 ,c))
    if c < width-1 and (r ,c+1) not in visited:
        possible.append((r ,c+1))
    return possible

def cycle_generator(board, start_pos):
    queue = [(start_pos, [start_pos])]
    while (queue):
        pos, visited = queue.pop(-1)
        neighbours = unvisited_neighbours(board, visited, pos)
        if not neighbours and abs(pos[0]-start_pos[0]+pos[1]-start_pos[1]) == 1:
            return visited
        for neigh in neighbours:
            new_visited = visited.copy()
            new_visited.append(neigh)
            queue.append((neigh, new_visited))
        


if __name__ == "__main__":
    width, height = map(int, sys.argv[1:],)
    board = [[0 for i in range(width)] for j in range(height)]
    print_board(board)
    start = (0, 0) #row col
    print(cycle_generator(board, start))