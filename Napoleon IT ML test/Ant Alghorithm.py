# -*- coding: utf-8 -*-
"""
Редактор Spyder

Это временный скриптовый файл.
"""

import random as rn
import numpy as np
import sys
from numpy.random import choice as np_choice

class AntColony(object):

    def __init__(self, distances, n_ants, n_best, n_iterations, decay, alpha=1, beta=1):
        """
        Args:
            distances (2D numpy.array): Square matrix of distances. Diagonal is assumed to be np.inf.
            n_ants (int): Number of ants running per iteration
            n_best (int): Number of best ants who deposit pheromone
            n_iteration (int): Number of iterations
            decay (float): Rate it which pheromone decays. The pheromone value is multiplied by decay, so 0.95 will lead to decay, 0.5 to much faster decay.
            alpha (int or float): exponenet on pheromone, higher alpha gives pheromone more weight. Default=1
            beta (int or float): exponent on distance, higher beta give distance more weight. Default=1
        Example:
            ant_colony = AntColony(german_distances, 100, 20, 2000, 0.95, alpha=1, beta=2)          
        """
        self.distances  = distances
        self.pheromone = np.ones(self.distances.shape) / len(distances)
        self.all_inds = range(len(distances))
        self.n_ants = n_ants
        self.n_best = n_best
        self.n_iterations = n_iterations
        self.decay = decay
        self.alpha = alpha
        self.beta = beta

    def run(self):
        shortest_path = None
        all_time_shortest_path = ("placeholder", np.inf)
        for i in range(self.n_iterations):
            all_paths = self.gen_all_paths()
            self.spread_pheronome(all_paths, self.n_best, shortest_path=shortest_path)
            shortest_path = min(all_paths, key=lambda x: x[1])
            #if we want to see the work step by step, uncomment it 
            #print(shortest_path, '\n')
            if shortest_path[1] < all_time_shortest_path[1]:
                all_time_shortest_path = shortest_path            
            self.pheromone * self.decay            
        return all_time_shortest_path

    def spread_pheronome(self, all_paths, n_best, shortest_path):
        sorted_paths = sorted(all_paths, key=lambda x: x[1])
        for path, dist in sorted_paths[:n_best]:
            for move in path:
                self.pheromone[move] += 1.0 / self.distances[move]

    def gen_path_dist(self, path):
        total_dist = 0
        for ele in path:
            total_dist += self.distances[ele]
        return total_dist

    def gen_all_paths(self):
        all_paths = []
        for i in range(self.n_ants):
            path = self.gen_path(0)
            all_paths.append((path, self.gen_path_dist(path)))
        return all_paths

    def gen_path(self, start):
        path = []
        visited = set()
        visited.add(start)
        prev = start
        for i in range(len(self.distances) - 1):
            move = self.pick_move(self.pheromone[prev], self.distances[prev], visited)
            path.append((prev, move))
            prev = move
            visited.add(move)
        path.append((prev, start)) # going back to where we started    
        return path

    def pick_move(self, pheromone, dist, visited):
        pheromone = np.copy(pheromone)
        pheromone[list(visited)] = 0

        row = pheromone ** self.alpha * (( 1.0 / dist) ** self.beta)

        norm_row = row / row.sum()
        move = np_choice(self.all_inds, 1, p=norm_row)[0]
        return move
    
    
    
def main():      
    '''
         #convert in data to nparray
    in_list = list()
    clear_data = list()
    in_list = sys.stdin.read() 
    str_end = 0
    str_start = 0
    while str_end < len(in_list):
        #cut '\n' symbol and restruct list
        if in_list[str_end] == '\n':
            in_list =  in_list[:str_end] +  in_list[str_end+1:]
            clear_data.append(list(in_list[str_start:str_end].split(' ')))
            str_start = str_end
            
        str_end+=1    
    in_list = (in_list.split(' '))[:-1]
    distances = np.array([])
            
    distances = np.asarray(clear_data,dtype=np.float16)
    #change 0 to np.inf ( devision zero error)
    j = i = 0
    while i < len(distances):
        while j < len(distances):
            if distances[i][j] == 0:
                distances[i][j] = np.inf            
            j+=1  
        j=0    
        i+=1
    
    '''
    distances = np.array([[np.inf, 2, 2, 5, 7],
                          [2, np.inf, 4, 8, 2],
                          [2, 4, np.inf, 1, 3],
                          [5, 8, 1, np.inf, 2],
                          [7, 2, 3, 2, np.inf]])
        
    ant_colony = AntColony(distances, 1, 1, 100, 0.95, alpha=1, beta=1)
    shortest_path = ant_colony.run()
    
    
    
    print( "shorted_path: {}".format(shortest_path))
    #print(int(shortest_path[-1]))
 

if __name__ == "__main__":
    main()
