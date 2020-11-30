from functools import reduce
import operator as op
from math import comb
from copy import deepcopy

def relative_map(source,sources,mapping):
    
    relative_mapping = deepcopy(mapping)
    other_sources=sources.copy()
    other_sources.remove(source)
    for other_source in other_sources:
        relative_mapping.pop(other_source)
    for vertex in relative_mapping:
        connections=relative_mapping.get(vertex)
        connections_copy=connections.copy()
        for connection in connections_copy:
            if connection in other_sources:
                connections.remove(connection)
        relative_mapping.update({vertex:connections})
        
    return(relative_mapping)

def convert_path_to_edges(paths):
    path_list=[]
    for path in paths:
        vertex_to_vertex=[]
        for i in range(len(path)-1):
            vertex_to_vertex.append((path[i],path[i+1]))
        path_list.append(tuple(vertex_to_vertex))
    return(path_list)

def average(x): 
    return(sum(x)/len(x))

def other_vertex(vertex,edge):
    if vertex==edge[0]:
        return(edge[1])
    else:
        return(edge[0])

def weighted_average(x,y,k):
    if l[0]==l[1]:
        return(average([x,y]))
    else:
        return(((l[0]*y)+(l[1]*x))/(l[0]+l[1]))

def eq(x,y):
    x = list(x)
    y = list(y)
    x.sort()
    y.sort()
    if x==y:
        return(True)
    else:
        return(False)

def get_risk(relation,risk_mapping):
    risk=risk_mapping.get(relation)
    if risk==None:
        risk=risk_mapping.get((relation[1],relation[0]))
    return(risk)
        
        
def distinct(x):
    k = []
    for i in x:
        append = True
        for j in k:
            if eq(i, j) == True:
                append = False
        if append == True:
            k.append(i)
    return(k)


def estimate_time(processer_frequency, total_paths, accuracy):
    from functools import reduce
    s = 0
    for i in range(1, total_paths+1):
        s += i*accuracy*(comb(total_paths, i))
        k = s//(processer_frequency)
    return(k)


def infect(risk):
    from random import random
    if risk >= random():
        return(True)
    else:
        return(False)


def simulate(source, mapping, risk_mapping):
    
    current = source
    infected = [source]
    transfer_que = [source]
    
    while True:
        
        for vertex in mapping[current]:
            if vertex not in infected and infect(get_risk((vertex,current),risk_mapping)) == True:
                infected.append(vertex)
                transfer_que.append(vertex)
                
        transfer_que.pop(0)
        if transfer_que == []:
            break
        else:
            current = transfer_que[0]
    
    return(infected)



