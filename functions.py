from functools import reduce
import operator as op
from math import comb

def relative_map(sources,mapping):
    relative_mappings=[]
    for source in sources:
        relative_mapping = mapping.copy()
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
        relative_mappings.append(relative_mapping)
    return(relative_mappings)

def convert_path_to_edges(paths):
    path_list=[]
    for path in paths:
        vertex_to_vertex=[]
        for i in range(len(path)-1):
            vertex_to_vertex.append((path[i],path[i+1]))
        path_list.append(tuple(vertex_to_vertex))
    return(path_list)


def eq(x,y):
    x = list(x)
    y = list(y)
    x.sort()
    y.sort()
    if x==y:
        return(True)
    else:
        return(False)


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
            k = risk_mapping.get((current, vertex))
            if k == None:
                k = risk_mapping.get((vertex, current))
            if vertex not in infected:
                if infect(k) == True:
                    infected.append(vertex)
                    transfer_que.append(vertex)
        transfer_que.pop(0)
        if transfer_que == []:
            break
        else:
            current = transfer_que[0]
    return(infected)


mapping = {1: [2, 3, 4, 5, 6, 7], 2: [1, 3, 4, 5, 6, 7], 3: [1, 2, 4, 5, 6, 7],
           4: [1, 2, 3, 5, 6, 7], 5: [1, 2, 3, 4, 6, 7], 6: [1, 2, 3, 4, 5, 7], 7: [1, 2, 3, 4, 5, 6]}

print(relative_map(1,[1,2,3],mapping))
