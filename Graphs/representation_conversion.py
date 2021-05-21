
import numpy as np
import sys
sys.path.append('/home/ved/Documents/Skills/progrmming/Algorithms/Graphs/adjacency_list')
import adjacency_list as al

def adlisttoadmatrix(adli,vlist):
    matrix=np.zeros((len(vlist),len(vlist)))
    for k in adli:
        frin=vlist.index(k)
        for ele in adli[k]:
            to=list(ele)[0]
            toin=vlist.index(to)
            w=int(list(ele)[1])
            matrix[frin][toin]=w
    return matrix            

ver= input("list down all vertices of the graph as a string: ")
vlist=list(ver)
print("No of vertices in the graph is "+str(len(vlist)))
# print("\nEnter type of graph",end="")
# type=input("d for directed un for undirected: ")
print("\nList down edges of the graph")
print("eg. 12 5,23 2,31 5 and so on..",end="")
ed=input("where 12 5 shows if there is edge to edge 1 to 2 with edgeweight: ")
print("\nNo. of edges  in the graph is "+str(len(ed.split(','))))

a=al.create_adjacency_list(ed, vlist)
print("\nAdjacency list: ")
print(a)
        

m=adlisttoadmatrix(a, vlist)
print("\nAdjacency matrix: ")
print(m)
        
        