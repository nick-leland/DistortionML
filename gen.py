import numpy as np
from collections import *

# TODO See if you can determine the recursive version of this algorithm
def search(graph, node, debug=None):
    """Basic Depth First Search Algorithm"""
    if debug == True:
        print("Beginning Search function")
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
                # TODO Need to set possible maze end points and randomize which point will be the finish
    if debug == True:
        print("Finished Search function")
    return order

def sort_list(list_dict, values_dict, debug=None):
    """Sorts the list based on the corresponding values"""
    if debug == True:
        print("Beginning sort_list function")
    out_list = []

    # print("Original 'list_dict' is", "\n", list_dict)
    
    for item in [*list_dict.keys()]:
        if debug == True:
            print(item)
        converted = [values_dict[x] for x in list_dict[item]]
        # TODO For the sake of learning, might be beneficial to not use the .sort() feature
        converted.sort()
        temp = [[*values_dict.keys()][[*values_dict.values()].index(x)] for x in converted]
        list_dict[item] = temp
    # print("Final 'list_dict' is", "\n", list_dict)
    if debug == True:
        print("Finished sort_list function")
    return out_list

def generate(size_x, size_y, seedin=None, debug=None):
    """Generates a size x size maze with a given seed
    Utilizes numpy random.default_rng for seed input"""
    if debug == True:
        print("Beginning Generate function")
    # Create a random generator and then sets random values for each position
    if seedin == None:
        rng = np.random.default_rng()
    else:
        rng = np.random.default_rng(seed=seedin)
    x = np.zeros((size_x, size_y), dtype=np.int16)
    maze_values = rng.random((size_x, size_y))

    # Creates a list of all positions in the maze and sets their value equal to the random value
    maze_neighbors = {}
    maze_value = {}
    xsize = size_x - 1
    ysize = size_y - 1
    # This might need to be switched
    for x in range(size_x):
        for y in range(size_y):
    
            # Determines the neighbors by the current x,y coordinate
            neighbors = []
            if y != 0:
                neighbors.append(f"{x} {y-1}")
            if y != ysize:
                neighbors.append(f"{x} {y+1}")
            if x != 0:
                neighbors.append(f"{x-1} {y}")
            if x != xsize:
                neighbors.append(f"{x+1} {y}")
    
            # Adds the neighbors and values to the designated dictionary
            maze_neighbors.update({f"{x} {y}" : neighbors})
            maze_value.update({f"{x} {y}" : maze_values[x][y]})
    # Sample print to verify
    # print(maze_neighbors[[*maze_neighbors.keys()][0]])
    # print(maze_value[[*maze_neighbors.keys()][0]])

    # TODO determine the starting node randomly based on one of the four corners
    
    sort_list(maze_neighbors, maze_value)
    if debug == True:
        print("Finished Generate function")
    return search(maze_neighbors, '0 0'), maze_neighbors


if __name__ == "__main__":
    # Sets the size of the maze
    # TODO Explore a maze that is not a square
    
    # size = int(input("What size of maze would you like to generate? \n"))
    # sizex = 5
    # sizey = 8

    sizex = input("What size x? ")
    if sizex == '':
        sizex = 5
        sizey = 8
    else:
        sizex = int(sizex)
        sizey = int(input("What size y? "))

    # seedq = input("Do you want a seed? Please answer Yes or No \n")[0]
    # seedq = seedq.title()
    # if seedq == 'N':
    #     seed = None
    # else:
    #     seed = int(input("Please give a number for the seed"))
    seed = None
    x, y = generate(sizex, sizey)
    print(x)
    print()
    print(y)

