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
import numpy as np
import matplotlib.pyplot as plt
import heapq
import math
from classes import ant


def move_ant(ant: Ant):
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
    
    possible = Map.get_possible(ant.pos)
    possible = np.transpose(possible)
    
    move_to = np.random.choice(possible[0], p = possible[1])#index index list, prob = probabilities
    
    ant.update(move_to)
    return

def main():
    # generate ants in a list

    ant1 = ant.Ant(0, np.array([0, 1, 2, 3])) #index, must visited nodes list(indices)
    # for every ant, I get the actual position

    #loop for the ants list until all necessary nodes are visited by all ants
    #move ant

    #until no new nodes are generated



if __name__ == "__main__":
    main()
