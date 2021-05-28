import cycle_detection as cd
import sys
sys.path.append('/home/ved/Documents/Skills/progrmming/Algorithms/Graphs/adjacency_list')
import adli_without_weight as al

ver= input("list down all vertices of the graph as a string: ")
vlist=list(ver)
print("No of vertices in the graph is "+str(len(vlist)))
# print("\nEnter type of graph",end="")
# type=input("d for directed un for undirected: ")
print("\nList down edges of the graph")
ed=input("eg. 12,23,31 and so on..")
print("No. of edges  in the graph is "+str(len(ed.split(','))))
a=al.create_adjacency_list(ed, vlist)
c=cd.iscycle(a,vlist)
if c==True:
    print('Graph contains cycle')
else:
    print('Graph does not contain cycle')