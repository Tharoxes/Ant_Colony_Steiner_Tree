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
from bokeh.layouts import layout
import map as mp
import numpy as np
from bokeh.transform import linear_cmap
from bokeh.palettes import RdYlBu, Turbo256
import time

def plot_init(map: mp.Map):
    """plots the map"""
    palette = Turbo256  #if an other palette is used change this
    
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
    
    
    edge_color = linear_cmap(field_name = "pher", palette = palette, low= 0,  high = 1)     
    
    
    
    
    p = figure(width = 940, height = 940)
    p.circle(x = "x", y = "y", color = "color", source = node_source)
    p.segment(x0 = "x0", y0 = "y0", x1 = "x1", y1 = "y1", color = edge_color, alpha = 1, line_width = 1, source = edge_source)
    
    # show(p)
    
    
    return p, edge_source, node_source

def update_sources():
    global maplist
    global mapindex
    global node_source
    global edge_source
    mapindex += 1
    mapindex %= len(maplist)
    
    print(mapindex)
    map = maplist[mapindex]
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
    node_source.data = {
        "x": nodes_coor[:,0], 
        "y": nodes_coor[:,1],
        "color": colorlist}
    
    paths = map.paths
    x0, x1, y0, y1 = [],[],[],[]
    for edge in paths:
        x0.append(nodes[edge[0]]["position"][0])
        y0.append(nodes[edge[0]]["position"][1])
        x1.append(nodes[edge[1]]["position"][0])
        y1.append(nodes[edge[1]]["position"][1])
     
           
    
    edge_source.data = {
        "x0": x0,
        "y0": y0,
        "x1": x1,
        "y1": y1,
        "pher": (np.array(map.pheromone) - np.min(map.pheromone))/ (np.max(map.pheromone)- np.min(map.pheromone)) 
        }
    
    print(edge_source.data)
    
    return



# def plot_all():




node_dict = {
    1: {"position": np.asarray([0,1]), "real": True},
    2: {"position": np.asarray([0,0]), "real": True},
    3: {"position": np.asarray([2,1]), "real": True},
    4: {"position": np.asarray([2,0]), "real": True},
}

paths = [[1,2], [2,3], [1,3], [2,4]]

pheromones = [100, 50, 80, 10]

mapi = mp.Map(node_list=node_dict, paths=paths, pheromones=pheromones)


# plot, edge_source, node_source = plot_init(mapi)
maplist = [mapi]


# show(plot)
# while True:
for k in range(0,10):
    # print(k)
    path = []
    pheromones = []
    for idx, edge in enumerate(paths):
        path.append([np.random.randint(1,5), np.random.randint(1,5)])
        pheromones.append(np.random.randint(0,100))
        
    # print(paths)
    mapi = mp.Map(node_list=node_dict, paths=path, pheromones=pheromones)
    maplist.append(mapi)

paths = [[1,4], [2,3], [1,2], [2,4]]
pheromones = [90, 20, 3, 10]

mapi = mp.Map(node_list=node_dict, paths=paths, pheromones=pheromones)



"""everithyng below here needs to be in the main file"""
maplist.append(mapi)
        
      
mapindex = 0
plot, edge_source, node_source = plot_init(maplist[mapindex])

doc = curdoc()
doc.add_root(plot)
doc.add_periodic_callback(update_sources, 1000)



    
    


