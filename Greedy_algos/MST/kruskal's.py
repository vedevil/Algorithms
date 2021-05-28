import numpy as np
import sys
sys.path.append('/home/ved/Documents/Skills/progrmming/Algorithms/Graphs/adjacency_matrix')
import adjacency_matrix_directed as am
sys.path.append('/home/ved/Documents/Skills/progrmming/Algorithms/Graphs/cycle_detection')
import cycle_detection as cd
sys.path.append('/home/ved/Documents/Skills/progrmming/Algorithms/Graphs/adjacency_list')
import adli_without_weight as al

ver= input("list down all vertices of the graph as a string: ")
vlist=list(ver)
print("No of vertices in the graph is "+str(len(vlist)))
# print("\nEnter type of graph",end="")
# type=input("d for directed un for undirected: ")
print("\nList down edges of the graph")
print("eg. 12 5,23 2,31 5 and so on..",end="")
ed=input("where 12 5 shows if there is edge to edge 1 to 2 with edgeweight: ")
print("No. of edges  in the graph is "+str(len(ed.split(','))))
def create_mst(elist,vlist):
    mst_edge=[]
    a=am.create_adjacency_matrix(elist, vlist)
    w_arr=a.reshape(-1)
    weight=0
    while len(mst_edge)!=len(vlist)-1:
        min_edge=np.min(w_arr[w_arr>0])
        ind=list(w_arr).index(min_edge)
        edge_weight=w_arr[ind]
        w_arr[ind]=0
        x_ind=ind//len(vlist)
        y_ind=ind % len(vlist)
        mst_edge.append(vlist[x_ind]+vlist[y_ind])
        mst_edge_string=','.join(str(v) for v in mst_edge)
        a_list=al.create_adjacency_list(mst_edge_string,vlist)
        if cd.iscycle(a_list, vlist):
            mst_edge.pop()
        else:
            weight+=edge_weight
    return mst_edge,weight

m,w=create_mst(ed, vlist)
print("Edges of mst is:")
print(m)
print('Weight of the tree is: ',end='')
print(w)