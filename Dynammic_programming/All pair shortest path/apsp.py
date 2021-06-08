import sys
sys.path.append('/home/ved/Documents/Skills/progrmming/Algorithms/Graphs/adjacency_list')
import adjacency_list_directed as al

with open('input.txt', 'r') as f:
    ver= f.readline()
    vlist=list(ver)
    print("No of vertices in the graph is "+str(len(vlist)))
    ed=f.readline()
    print("No. of edges  in the graph is "+str(len(ed.split(','))))

a=al.create_adjacency_list(ed, vlist)
print(a)