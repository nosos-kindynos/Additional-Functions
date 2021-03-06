from functools import reduce
import operator as op
from math import comb
from collections import OrderedDict
from copy import deepcopy
import csv

def relative_map(source,sources,mapping):
    
    relative_mapping = deepcopy(mapping)
    other_sources=sources.copy()
    if source!=None:
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

def weighted_average(x,y,l):
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

def read(file):
    k = []
    ladm = []

    with open(file, 'r') as f:
        reader = csv.reader(f)
        for i in reader:
            if len(i) >= 4 and not i[3] == '':
                x = i[3]
                x = eval(x)
                x = x[0]
                if isinstance(x,float)==True:
                    continue
                k.append(x)
                ladm.append(i[0])


    temp_data = {}
    for i in k:
        temp_data.update(i)

    data = {}
    for i in temp_data:
        contacts = []
        for j in temp_data.get(i):
            vertex = (int(j[0]), j[1])
            contacts.append(vertex)
        data.update({int(i): contacts})

    list_of_amdno = []
    for i in ladm:
        list_of_amdno.append(int(i))

    return([list_of_amdno,data])


def write(people, full_analysis, di, file,sources):

    l1 = []

    with open(file, 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            if not row == [] and not '' in row and not row[0] == 'Admno' and len(row) > 2:
                row = row[0:4]
                admno = int(row[0])
                if admno in people and not row[0] in sources:
                    k = di.get(admno)
                    l = full_analysis.get(admno)
                    if l == None:
                        l = []
                    report = l+[k]
                    row.append(report)
            if not row == [] and not row == ['', '']:
                l1.append(row)

    with open(file, 'w') as f:
        writer = csv.writer(f)
        for i in l1:
            if not i == []:
                writer.writerow(i)


def count_all_paths(paths):
    count={}
    for edge in paths:
        if edge in count:
            k=count.get(edge)
            k+=1
            count.update({edge:k})
        else:
            count.update({edge:1})
    return(count)

def union(x):
    k=1
    for i in x:
        k*=(1-i)
    return(1-k)

def intersection_of(path,risk_mapping):
    intersection = 1
    for t in path:
        intersection*= get_risk(t, risk_mapping)
    return(intersection)

def rank(paths,risk_mapping,top):
    if len(paths)>top:
        path_dict={}
        for path in paths:
            path_dict.update({path:intersection_of(path,risk_mapping)})

        top_paths = []
        for i in range(top):
            keymax = max(path_dict, key=path_dict.get)
            top_paths.append(keymax)
            path_dict.pop(keymax)

        return(top_paths)
    else:
        return(paths)


def extract_and_insert(edge,dictionary,value):
    reverse_edge=(edge[1], edge[0])
    h=dictionary.get(edge)
    k=False
    if h==None:
        h=dictionary.get(reverse_edge)
        k=True
    h+=value
    if k==False:
        dictionary.update({edge:h})
    else:
        dictionary.update({reverse_edge:h})

def sort_values(edge_count):
    sorted = {}
    for i in range(len(edge_count)):
        keymax = max(edge_count, key=edge_count.get)
        sorted.update({keymax: edge_count.get(keymax)})
        edge_count.pop(keymax)
    return(sorted)
    
