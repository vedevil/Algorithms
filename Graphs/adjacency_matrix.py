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
    return matrix

ver= input("list down all vertices of the graph as a string: ")
vlist=list(ver)
print("No of vertices in the graph is "+str(len(vlist)))
# print("\nEnter type of graph",end="")
# type=input("d for directed un for undirected: ")
print("\nList down edges of the graph")
print("eg. 12 5,23 2,31 5 and so on..",end="")
ed=input("where 12 5 shows if there is edge to edge 1 to 2 with edgeweight: ")
print("No. of edges  in the graph is "+str(len(ed.split(','))))

m=np.zeros((len(vlist),len(vlist)))
m=create_adjacency_matrix(ed,vlist)
print("\nAdjacency matrix:")
print(m)