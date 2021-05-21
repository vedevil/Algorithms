import numpy as np
ver= input("list down all vertices of the graph as a string: ")
vlist=list(ver)
print("No of vertices in the graph is "+str(len(vlist)))
# print("\nEnter type of graph",end="")
# type=input("d for directed un for undirected: ")
print("\nList down edges of the graph")
print("eg. 12 5,23 2,31 5 and so on..",end="")
ed=input("where 12 5 shows if there is edge to edge 1 to 2 with edgeweight: ")
adli=dict()
matrix=np.zeros((len(vlist),len(vlist)))
edges=ed.split(',')
print("\nNo. of edges  in the graph is "+str(len(edges)))
for e in edges:
    w=int(e.split()[1])
    fr=list(e.split()[0])[0]
    to=list(e.split()[0])[1]
    if fr in adli:
        adli[fr].append(to+str(w))
    else:
        adli[fr]=[]
        adli[fr].append(to+str(w))
print("\nAdjacency list: ")
print(adli)
