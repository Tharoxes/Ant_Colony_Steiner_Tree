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
from bokeh.io import output_file, show, save, curdoc
from bokeh.plotting import figure
from bokeh.models import ColumnDataSource
import map as mp
import numpy as np

def plot_one(map: mp.Map):
    """plots the map
    Remark: Because of normalizatio not all edges are always visible"""
    nodes = map.node_list
    nodes_coor = []
    colorlist = []
    for key in nodes.keys():
        color = "green"
        if nodes[key]["real"]:
            color = "firebrick"
            
        colorlist.append(color)
        nodes_coor.append(nodes[key]["position"])
    
    
    nodes_coor = np.array(nodes_coor)
    node_source = ColumnDataSource(data = {
        "x": nodes_coor[:,0], 
        "y": nodes_coor[:,1],
        "color": colorlist})
    
    paths = map.paths
    x0, x1, y0, y1 = [],[],[],[]
    for edge in paths:
        x0.append(nodes[edge[0]]["position"][0])
        y0.append(nodes[edge[0]]["position"][1])
        x1.append(nodes[edge[1]]["position"][0])
        y1.append(nodes[edge[1]]["position"][1])
     
           
    
    edge_source = ColumnDataSource(data = {
        "x0": x0,
        "y0": y0,
        "x1": x1,
        "y1": y1,
        "pher": (np.array(map.pheromone) - np.min(map.pheromone))/ (np.max(map.pheromone)- np.min(map.pheromone)) 
        })
    
    
                 
    
    
    
    
    p = figure()
    p.circle(x = "x", y = "y", color = "color", source = node_source)
    p.segment(x0 = "x0", y0 = "y0", x1 = "x1", y1 = "y1", color = "black", alpha = "pher", line_width = 1, source = edge_source)
    
    show(p)
    
    
    return 



def main():

    node_dict = {
        1: {"position": np.asarray([0,1]), "real": True},
        2: {"position": np.asarray([0,0]), "real": True},
        3: {"position": np.asarray([2,1]), "real": True},
        4: {"position": np.asarray([2,0]), "real": True},
    }
    
    paths = [[1,2], [2,3], [1,3], [2,4]]
    
    pheromones = [60, 50, 50, 50]
    
    mapi = mp.Map(node_list=node_dict, paths=paths, pheromones=pheromones)
    
    plot_one(mapi)


if __name__ == "__main__":
    main()