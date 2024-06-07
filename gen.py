import numpy as np
from collections import *

# TODO See if you can determine the recursive version of this algorithm
def search(graph, node):
    """Basic Depth First Search Algorithm"""
    order = []
    visited = []
    stack = deque()

    visited.append(node)
    stack.append(node)

    while stack:
        s = stack.pop()
        order.append(s)
        for n in reversed(graph[s]):
            if n not in visited:
                visited.append(n)
                stack.append(n)
    return order

def sort_list(list_dict, values_dict):
    """Sorts the list based on the corresponding values"""
    out_list = []

    for item in [*list_dict.keys()]:
        converted = [values_dict[x] for x in list_dict[item]]
        # TODO For the sake of learning, might be beneficial to not use the .sort() feature
        converted.sort()
        temp = [[*values_dict.keys()][[*values_dict.values()].index(x)] for x in converted]
        list_dict[item] = temp
    return out_list

# Sets the size of the maze
size = 10

# Create a random generator and then sets random values for each position
# rng = np.random.default_rng(seed=223)
rng = np.random.default_rng()
print(rng.random())
x = np.zeros((size, size), dtype=np.int16)
maze_values = rng.random((size, size))

# Creates a list of all positions in the maze and sets their value equal to the random value
maze_neighbors = {}
maze_value = {}
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

        # Adds the neighbors and values to the designated dictionary
        maze_neighbors.update({f"{x} {y}" : neighbors})
        maze_value.update({f"{x} {y}" : [maze_values[0][0]]})

# Sample print to verify
# print(maze_neighbors[[*maze_neighbors.keys()][0]])
# print(maze_value[[*maze_neighbors.keys()][0]])

# print(maze_neighbors)

# Search(graph, node)
# TODO determine the starting node randomly based on one of the four corners
print(sort_list(maze_neighbors, maze_value))
print(search(maze_neighbors, '0 0'))


