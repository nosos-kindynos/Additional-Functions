from functools import reduce
import operator as op


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


def ncr(n, r):
    r = min(r, n-r)
    numer = reduce(op.mul, range(n, n-r, -1), 1)
    denom = reduce(op.mul, range(1, r+1), 1)
    return numer // denom  # or / in Python 2

def estimate_time(processer_frequency, accuracy):
    from functools import reduce
    n = len(paths)

    def ncr(n, r):
        r = min(r, n-r)
        numer = reduce(op.mul, range(n, n-r, -1), 1)
        denom = reduce(op.mul, range(1, r+1), 1)
        return numer // denom  # or / in Python 2
    s = 0
    for i in range(1, n+1):
        s += i*accuracy*(ncr(n, i))
        k = s/(processer_frequency)
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
