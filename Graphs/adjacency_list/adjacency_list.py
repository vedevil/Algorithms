import numpy as np


def create_adjacency_list(elist,vlist):
    adli=dict()
    edges=elist.split(',')
    for e in edges:
        w=int(e.split()[1])
        fr=list(e.split()[0])[0]
        to=list(e.split()[0])[1]
        if fr in adli:
            adli[fr].append(to+str(w))
        else:
            adli[fr]=[]
            adli[fr].append(to+str(w))
        if to in adli:
            adli[to].append(fr+str(w))
        else:
            adli[to]=[]
            adli[to].append(fr+str(w))
    return adli


