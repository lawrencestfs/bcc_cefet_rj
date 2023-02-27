##!/usr/bin/python
# -*- coding: utf-8 -*-

# File Name: graph.py
# Author: Lawrence Fernandes

""" Graph classs
A simple Python graph class, demonstrating the essential 
facts and functionalities of graphs.
"""

class Graph(object):

    # Class constructor
    def __init__(self, name, graph_dict=None):
        """ Initializes a graph object 
            If no dictionary or None is given, 
            an empty dictionary will be used
        """
        self.name = name

        if graph_dict == None:
            graph_dict = {}
        self.graph_dict = graph_dict

    def get_vertices(self):
        """ Returns the vertices of a graph """
        return list(self.graph_dict.keys())

    def get_edges(self):
        """ Returns the edges of a graph """
        return self.__generate_edges()

    def add_vertex(self, vertex):
        """ If the vertex "vertex" is not in self.graph_dict, 
            a key "vertex" with an empty list as a value is added 
            to the dictionary. Otherwise nothing has to be done. 
        """
        if vertex not in self.graph_dict:
            self.graph_dict[vertex] = []

    def add_edge(self, edge):
        """ Assumes that edge is of type set, tuple or list; 
            between two vertices can be multiple edges! 
        """
        edge = set(edge)
        (vertex1, vertex2) = tuple(edge)
        if vertex1 in self.graph_dict:
            self.graph_dict[vertex1].append(vertex2)
        else:
            self.graph_dict[vertex1] = [vertex2]

    def __generate_edges(self):
        """ A static method generating the edges of the graph. 
            Edges are represented as sets with one 
            (a loop back to the vertex) or two vertices 
        """
        edges = []
        for vertex in self.graph_dict:
            for neighbour in self.graph_dict[vertex]:
                if {neighbour, vertex} not in edges:
                    edges.append({vertex, neighbour})
        return edges

    def __repr__(self):
        #return str(self)
        return str(self.name)

    def __str__(self):
        """ Reimplementation of the string method
        """
        res = "Name: " + self.name
        res += "\nVertices: "
        for k in self.graph_dict:
            res += str(k) + " "
        res += "\nEdges: "
        for edge in self.__generate_edges():
            res += str(edge) + " "
        return res

    def __eq__(self, other):
        """ Reimplementation of the equals method,
            used to compare objects 
        """
        return self.name == other.name