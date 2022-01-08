"""This is the LinkState Protocol for Option 9

In this option the server will map the network upon client request.
Mapping the network in this assignment means getting a table with all the distances between nodes/machines. 
If one or more clients are running in the same machine, then the server must assign random
distances to those clients. 
"""
import random
from threading import Thread
import queue
import sys

class LinkState:
   
    # def __init__(self):
    #     self.result = "No Data"
    #     print("Initializing LinkState")
    @staticmethod
    def min_distance(dist, spt_set, V):
 
        # Initialize minimum distance for next node
        min = sys.maxsize
 
        # Search not nearest vertex not in the
        # shortest path tree
        for v in range(V):
            if dist[v] < min and spt_set[v] == False:
                min = dist[v]
                min_index = v
 
        return min_index
 
    #Initializing for the Thread. May or May not be needed. 
    @staticmethod
    def dijkstras(graph, src):
        print('started calculating')
        V = len(graph)

        dist = [sys.maxsize] * V
        dist[src] = 0
        spt_set = [False] * V

        for _ in range(V):

            u = LinkState.minDistance(dist, spt_set, V)

            # Put the minimum distance vertex in the
            # shortest path tree
            spt_set[u] = True

            for v in range(V):
                if graph[u][v] > 0 and spt_set[v] == False and dist[v] > dist[u] + graph[u][v]:
                    dist[v] = dist[u] + graph[u][v]
        print('finished calculating')
        return dist
        

    @staticmethod#Returns a Random Matrix of size N for the number of users as a 2D List
    def random_matrix(num_users):
        print("Random Matrix LSP")
        matrix = [[0]*num_users for x in range(num_users)]

        for i in range(num_users):

            for j in range(num_users):

                if i != j:

                    matrix[i][j] = random.randint(1,15)
        
        for i in range(0,len(matrix)):

            for j in range(i, len(matrix)):

                matrix[j][i] = matrix[i][j]

        
        return matrix
    #
    #Takes in a List of Names, and returns a Mapped out network with each name as a String. 
    def create_network(names_list, matrix):
        print("Creating Network LSP")
        listofnames = names_list
        
        # matrix = self.random_matrix(len(listofnames))

        listed = {listofnames[x]: matrix[x] for x in range(len(listofnames))}

        column_header = "| " + " |  ".join(x.center(2) for x in listofnames) + "  |"
        table = "\t\t" + column_header + "\n"

        for key in listed:
            table += key.rjust(15) + ": "
            for value in listed[key]:
                table += "   " + str(value).center(2) + "   |  "
            table += "\n"
       

        #Queue for the Thread, May or may not be used.

        #Want to return the printed table as a string to be displayed. 
        return table

