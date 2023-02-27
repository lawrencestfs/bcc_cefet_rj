##!/usr/bin/python
# -*- coding: utf-8 -*-

# File Name: main.py
# Author: Lawrence Fernandes

""" Main class
This is the main class of the program.
"""

# Imports
import os
import glob
import json
from pathlib import Path
from colorama import Fore, Back, Style
# Custom module imports
from graph import *
from graph_search import *

LOCAL_PATH = os.getcwd()
data_dir = os.path.join(LOCAL_PATH, "data")
graph_list = [] # list of graph objects

def import_graph(file_name):
    """ This function imports json files representing graphs """
    graph = {}
    file_extension = ".json"

    if file_name.endswith(file_extension):
        with open(file_name, encoding='utf-8') as data_file:
            graph = json.loads(data_file.read())
    else:
        print("ERRO: Não foi possível abrir o arquivo!")
    
    return graph


def auto_loader():
    """ This function automatically imports graphs from files in the data folder """
    for file in glob.glob(f"{data_dir}/*.json"):
        graph_list.append(Graph(
            name=Path(file).name, 
            graph_dict=import_graph(file)
        ))


def cls():
    """ Helper function that clears the screen and prints the logo """
    os.system('cls' if os.name=='nt' else 'clear')
    print(Fore.CYAN + 
          " _____            __                      __   _____ \n"+
          "|  __ \          / _|                    /  | |  _  |\n"+
          "| |  \/_ __ __ _| |_ ___  ___     __   __`| | | |/' |\n"+
          "| | __| '__/ _` |  _/ _ \/ __|    \ \ / / | | |  /| |\n"+
          "| |_\ \ | | (_| | || (_) \__ \     \ V / _| |_\ |_/ /\n"+
          "\____/|_|  \__,_|_| \___/|___/      \_/  \___(_)___/ \n")
    print(Style.RESET_ALL)


def main_menu():
    """ This function creates the main menu """
    cls()
    print("\n***** Menu *****")
    print("1. Import graph")
    print("2. List graphs")
    print("3. Print graph")
    print("4. Delete graph")
    print("5. Search methods")
    print("6. Exit")
    option = int(input("Select an option (1 - 6): "))
    return option


def search_menu():
    """ This function creates the seach menu """
    cls()
    print("\n***** Search methods *****")
    print("1. DFS")
    print("2. DFS (recursive)")
    print("3. BFS")
    option = int(input("Select an option (1 - 3): "))
    graph_name = input("\n Insert the name of the graph: ")
    return option, graph_name


def main():
    """ This is the main function of the program """
    auto_loader()
    condition = True

    while condition:
        option = main_menu()

        # 1. Graph definition
        if option == 1:
            cls()
            print("Import graph:")
            try:
                graph_name = input("\n Insert the name of the graph file: ")
                file = data_dir + "/" + graph_name + '.json'

                if os.path.isfile(file): # checking if the file exists
                    graph_dict = import_graph(file)
                    graph_list.append(Graph(graph_name, graph_dict))
                    input("\nDone! Press Enter to continue ...")

                else:
                    print(Fore.RED + "\nERROR: Failed to import the graph! Check if the file exists in the data folder.")
                    print(Style.RESET_ALL)
                    input("Press Enter to continue ...")

            # catch *all* exceptions
            except BaseException as error:
                print('An exception occurred: {}'.format(error))

        # 2. Shows defined graphs
        elif option == 2:
            cls()
            if len(graph_list) > 0:
                print("\nGraphs available: ")
                print(graph_list)
                input("\nPress Enter to continue ...")
            else:
                print(Fore.YELLOW + "\nNo graph was imported or defined!")
                print(Style.RESET_ALL)
                input("Press Enter to continue ...")

        # 3. Shows specific graph
        elif option == 3:
            cls()
            print("\nGraphs available: ")
            print(graph_list)
            graph_name = input("\nInsert the name of the graph file: ")
            if len(graph_list) > 0:
                list_size = len(graph_list)
                for x in range(list_size):
                    if graph_list[x].name == graph_name:
                        print(graph_list[x])
                        input("Press Enter to continue ...")
                        print("\n")
                        
            else:
                cls()
                print("\nNo graph was imported or defined!")

        # 4. Delete graph
        elif option == 4:
            cls()
            print("\nGraphs available: ")
            print(graph_list)
            if len(graph_list) > 0:
                graph_name = input("\nEnter the name of the graph to be removed: ")
                for graph in graph_list:
                    if graph.name == graph_name:
                        graph_list.remove(graph)
            else:
                print("\nThere is no graph to be removed!")

        # 5. Search methods
        elif option == 5:
            cls()
            print("Search methods")
            #print(graph.get_vertices())
            #print(graph.get_edges())

            option, graph = search_menu()

            # Check if graph was defined/imported
            list_size = len(graph_list)
            for x in range(list_size):
                if graph_list[x].name == graph_name:
                    graph = graph_list[x]

                    if option == 1:
                        print("\nDFS")
                        start = input("Inform the starting node: ")
                        response = dfs(graph.graph_dict, start)
                        print(response)
                        input("Press Enter to continue ...")

                    elif option == 2:
                        print("\nDFS (recursive)")
                        input("Press Enter to continue ...")

                    elif option == 3:
                        print("\nBFS")
                        input("Press Enter to continue ...")

                    else:
                        print(Fore.RED + "\nERROR: Invalid option!")
                        print(Style.RESET_ALL)
                        input("Press Enter to continue ...")

            else:
                print(Fore.RED + "\nERROR: Invalid graph name, object not found!")
                print(Style.RESET_ALL)
                input("Press Enter to continue ...")

        # 6. Exit
        elif option == 6:
            print("\n Closing the program...")
            graph_list.clear() # clear object list, to remove the graph objects created
            condition = False

        else:
            print(Fore.RED + "\nERROR: Invalid option!")
            print(Style.RESET_ALL)
            input("Press Enter to continue ...")

    print("\n Bye!")

if __name__ == '__main__':
    main()