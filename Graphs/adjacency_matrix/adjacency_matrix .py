import numpy as np

def create_adjacency_matrix(elist,vlist):
    matrix=np.zeros((len(vlist),len(vlist)))
    edges=elist.split(',')
    for e in edges:
        w=int(e.split()[1])
        fr=list(e.split()[0])[0]
        to=list(e.split()[0])[1]
        frindex=int(vlist.index(fr))
        toindex=int(vlist.index(to))
        matrix[frindex][toindex]=w
    matrix=matrix+matrix.transpose()
    for i in len(vlist):
        matrix[i][i]/=2
    return matrix

