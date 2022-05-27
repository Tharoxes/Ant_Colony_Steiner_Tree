#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Name:      Huynh, Thanh Cong / Lucien Lang
   Email:     thanhcong.huynh@uzh.ch / lucien.lang@uzh.ch
   Date:      03 April, 2022
   Kurs:      ESC202
   Semester:  FS22
   Thema:     Ant Colony/ Steiners Colony
   Matrikel-nr.: 16-933-608/ 18-915-108
"""

# -*- coding: utf-8 -*-
import random

import numpy as np
import matplotlib.pyplot as plt
import heapq
import math
from classes import ant, node 
from classes import map as mp


def move_ant(ant: ant.Ant, map: mp.Map):
    """moves an Ant to a new node"""
    """rewrite to ask map an index -> map returns the possible next ones and their prob"""
    # possible = nodes.connect(ant.position) #i somehow need the possible conections from a given node
    
    # smart_choice_prob = 0.75 #probability to make the optimal choice
    # #make not smart choice
    # if(not (rd.random() < smart_choice_prob)):
    #     ant.update_position(np.choice(possible, 1))
    
    # #find the best next choice -> assumption pheromones are saved as a tuple (i,j)
    # best_next = (possible[0], pheromones[ant.pos, possible[0]])
    # for i in range(1, len(possible)):
    #     pheromones_onedge = pheromones[ant.pos, possible[i]]
    #     if  pheromones_onedge > best_next[1]:
    #         best_next = (possible[i], pheromones_onedge)
            
    # ant.update_position(best_next[0])
    
    
    possible = map.get_possible_paths(ant.position)
    possible = np.transpose(possible)
    
    move_to = np.random.choice(possible[0], p = possible[1])#index index list, prob = probabilities
    
    ant.update(move_to)
    return

def main():
    # setup
    evaporation = 0.9
    real_nodes = 4
    iterations = 100
    artificial_nodes = 0
    #generate node_list
    node_dict = {
        0: {"position": np.asarray([0,1]), "real": True},
        1: {"position": np.asarray([0,0]), "real": True},
        2: {"position": np.asarray([2,1]), "real": True},
        3: {"position": np.asarray([2,0]), "real": True},
    }
    
    paths = [[0,0]]
    for start in node_dict:
        for end in node_dict:
            if start < end:
                paths = np.append(paths, [[start, end]], axis=0)

    paths = np.delete(paths, 0, 0)
    #print(type(paths))

    pheromones = np.zeros((real_nodes, 1))

    map = mp.Map(node_list=node_dict, paths=paths, pheromones=pheromones)


    for i in range(iterations):
        #generate paths

        #generate map

        # generate ants in a list
        number_ants = 0
        if len(map.node_list) < 10:
            number_ants = 10
        else:
            number_ants = len(map.node_list)

        # path for one node to another; connection for a tree to all necessary nodes

        ants_connections = list()
        for i in range(number_ants):
            current_ant = ant.Ant(random.randint(0, real_nodes), np.arange(0, real_nodes)) #if nodes start at 0 the last +1 needs to be deleted
            while not current_ant.visited_all:
                # todo: move ant to index xy
                # possible_paths = map.get_possible_paths(current_ant.position) # todo: index xy
                # ants_path = ... # add to the path, if not already visited
                move_ant(current_ant, map)
            ants_connections.append(current_ant.path) # add the path of an ant to the list example [[0, 1][1, 3][3, 2][2, 4]]

        # add ants connections and compute their lengths, both lists are sorted
        map.compute_ants_path(ants_connections)

        # update pheromones (delete edges or evaporation)
        # old pheromones
        map.evaporate(evaporation)

        # add new pheromones
        map.add_new_pheromones()

        # add new nodes

        for i in map.cycles[artificial_nodes:]:
            map.new_artificial_node(real_nodes+artificial_nodes, i)
            artificial_nodes += 1

        if i % 11 == 0:
            print(map.lengths[0])


if __name__ == "__main__":
    main()
