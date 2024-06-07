import collections 
from collections import *
import numpy as np

def dfs(graph, node):
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

    print(list_dict)
    for item in [*list_dict.keys()]:
        converted = [values_dict[x] for x in list_dict[item]]
        # TODO For the sake of learning should probably figure out a nice insertion sort here
        converted.sort()
        temp = [[*values_dict.keys()][[*values_dict.values()].index(x)] for x in converted]
        list_dict[item] = temp

    print(list_dict)
    return out_list

graph = {
        'A' : ['B', 'G'], 
        'B' : ['C', 'D', 'E'], 
        'C' : [],
        'D' : [],
        'E' : ['F'],
        'F' : [],
        'G' : ['H'],
        'H' : ['I'],
        'I' : []
        }
# Now that we have the base graph, we need to set random values to sort off of.
values = {}
for item in [*graph.keys()]:
    values[item] = np.random.default_rng().random()
print(values)
print()

print(sort_list(graph, values))
print()

print(dfs(graph, 'A'))
print()

for item in [*graph.keys()]:
    print(graph[item])

print(dfs(graph, 'A'))
