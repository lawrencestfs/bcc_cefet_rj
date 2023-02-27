##!/usr/bin/python
# -*- coding: utf-8 -*-

# File Name: graph_search.py
# Author: Lawrence Fernandes

""" Graph Search class
This class demonstrates the seach methods available for graphs.
"""

'''
You can store many kinds of graphs this way, not just DAGs, 
so you will need to post-process it to make sure that it has no loops. 
Just pick a node, DFS, if you see any node more than once it is not a DAG. 
Then remove all of the nodes you just saw and repeat with any remaining nodes. 
Do this until you find a loop or you've removed all of the nodes, in the latter case the graph is a DAG.


https://www.python.org/doc/essays/graphs/

import time
'''

''' Depth-First Search '''
def dfs(graph, start):
    print(type(graph))
    #start_time = time.time()
    visited, stack = set(), [start]
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            stack.extend(graph[vertex] - visited)
    #print("--- %s seconds ---" % (time.time() - start_time))
    return visited


''' Recursive Depth-First Search '''
def dfs_recursive(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    for next in graph[start] - visited:
        dfs_recursive(graph, next, visited)
    return visited


def dfs_paths(graph, start, goal):
    stack = [(start, [start])]
    while stack:
        (vertex, path) = stack.pop()
        for next in graph[vertex] - set(path):
            if next == goal:
                yield path + [next]
            else:
                stack.append((next, path + [next]))


def dfs_paths_recursive(graph, start, goal, path=None):
    if path is None:
        path = [start]
    if start == goal:
        yield path
    for next in graph[start] - set(path):
        yield from dfs_paths_recursive(graph, next, goal, path + [next])


def dijkstra(graph, start):
    distances = graph
    nodes = list(graph)
    nodes.sort()
    print(nodes)
    
    unvisited = {node: float('inf') for node in nodes} # other option is to use None as +inf
    visited = {}
    current = start
    currentDistance = 0
    unvisited[current] = currentDistance

    while True:
        for neighbour, distance in distances[current].items():
            if neighbour not in unvisited: continue
            newDistance = currentDistance + distance
            if unvisited[neighbour] is float('inf') or unvisited[neighbour] > newDistance:
                unvisited[neighbour] = newDistance
        visited[current] = currentDistance
        del unvisited[current]
        if not unvisited: break
        candidates = [node for node in unvisited.items() if node[1]]
        current, currentDistance = sorted(candidates, key = lambda x: x[1])[0]

    print(visited)


# Bellman-Ford's single source shortest path algorithm.
def bellman_ford(graph, source):
    """ Input: Graph and a source vertex src
        Output: Shortest distance to all vertices from src. If there is a negative weight cycle, 
        then shortest distances are not calculated, negative weight cycle is reported.
    """

    # Step 1: Initialize distances from src to all other vertices as INFINITE
    d = {} # Stands for destination
    p = {} # Stands for predecessor
    # For each node prepare the destination and predecessor
    for node in graph:
        d[node] = float('Inf') # We start admiting that the rest of nodes are very very far
        p[node] = None
    d[source] = 0 # For the source we know how to reach

    # Step 2: Relax all edges |V| - 1 times. A simple shortest path from 
    # source to any other vertex can have at-most |V| - 1 edges
    for i in range(len(graph)-1): #Run this until is converges
        for node in graph:
            for neighbour in graph[node]: #For each neighbour of u
                # If the distance between the node and the neighbour is lower than the one I have now
                if d[neighbour] > d[node] + graph[node][neighbour]:
                    # Record this lower distance
                    d[neighbour]  = d[node] + graph[node][neighbour]
                    p[neighbour] = node

    # Step 3: check for negative-weight cycles
    for u in graph:
        for v in graph[u]:
            assert d[v] <= d[u] + graph[u][v]

    return d, p

#floyd_warshall
# https://www.geeksforgeeks.org/dynamic-programming-set-16-floyd-warshall-algorithm/
# https://www.geeksforgeeks.org/detecting-negative-cycle-using-floyd-warshall/

def test():

    graph1 = {
        'B': {'A': 5, 'D': 1, 'G': 2},
        'A': {'B': 5, 'D': 3, 'E': 12, 'F' :5},
        'D': {'B': 1, 'G': 1, 'E': 1, 'A': 3},
        'G': {'B': 2, 'D': 1, 'C': 2},
        'C': {'G': 2, 'E': 1, 'F': 16},
        'E': {'A': 12, 'D': 1, 'C': 1, 'F': 2},
        'F': {'A': 5, 'E': 2, 'C': 16}
        }

    graph2 = {
        'a': {'b': -1, 'c':  4},
        'b': {'c':  3, 'd':  2, 'e':  2},
        'c': {},
        'd': {'b':  1, 'c':  5},
        'e': {'d': -3}
        }

    d, p = bellman_ford(graph2, 'a')

    assert d == {
        'a':  0,
        'b': -1,
        'c':  2,
        'd': -2,
        'e':  1
        }

    assert p == {
        'a': None,
        'b': 'a',
        'c': 'b',
        'd': 'e',
        'e': 'b'
        }

    print(d)
    print(p)


    #dijkstra(graph, 'B')

if __name__ == '__main__': test()