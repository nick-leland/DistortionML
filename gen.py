import numpy as np
from collections import *

size = 10

rng = np.random.default_rng(seed=223)

x = np.zeros((size, size), dtype=np.int16)


# Initializes the random values for each maze position
maze_values = rng.random((size, size))
# print(maze_values)
# print(maze_values[0][0])

# Creates a list of all positions in the maze and sets their value equal to the random value
maze = []
zsize = size - 1
for x in range(size):
    for y in range(size):

        # Determines the neighbors by the current x,y coordinate
        neighbors = []
        if y != 0:
            neighbors.append(f"{x} {y-1}")
        if y != zsize:
            neighbors.append(f"{x} {y+1}")
        if x != 0:
            neighbors.append(f"{x-1} {y}")
        if x != zsize:
            neighbors.append(f"{x+1} {y}")

        maze.append({f"{x} {y}" : [maze_values[0][0], neighbors]})

# Verification print sequence
# for position in maze:
#     print(list(position.keys())[0], position[list(position.keys())[0]][1])

def search(graph, node):
    visited = []
    stack = deque()

    visited.append(node)
    stack.append(node)

    print(stack)
    while stack:
        s = stack.pop()
        print("s = ", s, end=" ")
        print("graph is a long list here is the first item", graph[0])
        print(graph[s][0])
        print(reversed(graph[s]))
        for n in reversed(graph[s]):
            if n not in visited:
                visited.append(n)
                stack.append(n)

search(maze, maze[0][list(maze[0].keys())[0]][1])
