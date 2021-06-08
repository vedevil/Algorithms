
import numpy as np
import sys
sys.path.append('/home/ved/Documents/Skills/progrmming/Algorithms/Graphs/adjacency_list')
import adjacency_list_directed as al

with open('input.txt', 'r') as f:
    ver= f.readline().split('\n')[0]
    vlist=list(ver)
    print("No of vertices in the graph is "+str(len(vlist)))
    ed=f.readline().split('\n')[0]
    print("No. of edges  in the graph is "+str(len(ed.split(','))))
inf=99999
matrix=np.full((len(vlist),len(vlist)),inf)
a=al.create_adjacency_list(ed, vlist)
for vertex in a:
    edges_incident=a[vertex]
    for e in edges_incident:
        iv=e[0]
        w=int(e[1])
        row_index=vlist.index(vertex)
        col_index=vlist.index(iv)
        matrix[row_index][col_index]=w
for k in vlist:
    for i in vlist:
        for j in vlist:
            k_index=vlist.index(k)
            i_index=vlist.index(i)
            j_index=vlist.index(j)
            if matrix[i_index][k_index]+matrix[k_index][j_index]<matrix[i_index][j_index]:
                matrix[i_index][j_index]=matrix[i_index][k_index]+matrix[k_index][j_index]  
for i in range(len(vlist)):
    matrix[i][i]=0
print(matrix)