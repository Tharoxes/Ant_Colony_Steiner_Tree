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
    
    
    nodesource = ColumnDataSource(data = {
        "x": nodes_coor[:,0], 
        "y": nodes_coor[:,1],
        "color": colorlist})
    
    
    
    p = figure()
    p.circle(x = "x", y = "y", color = "color", source = nodesource)
    show(p)
    return





node_dict = {
    1: {"position": np.asarray([0,1]), "real": True},
    2: {"position": np.asarray([0,0]), "real": True},
    3: {"position": np.asarray([2,1]), "real": True},
    4: {"position": np.asarray([2,0]), "real": True},
}

paths = np.zeros((1,3))
for start in node_dict:
    for end in node_dict:
        if start < end:
            np.append(paths, [[start, end]])

pheromones = np.zeros((4, 1))

map = mp.Map(node_list=node_dict, paths=paths, pheromones=pheromones)