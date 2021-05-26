import sys
sys.path.append('/home/ved/Documents/Skills/progrmming/Algorithms/Graphs/adjacency_list')
import adjacency_list as al

ver= input("list down all vertices of the graph as a string: ")
vlist=list(ver)
print("No of vertices in the graph is "+str(len(vlist)))
print("\nList down edges of the graph")
print("eg. 12 5,23 2,31 5 and so on..",end="")
ed=input("where 12 5 shows if there is edge to edge 1 to 2 with edgeweight: ")
print("No. of edges  in the graph is "+str(len(ed.split(','))))
adli=al.create_adjacency_list(ed, vlist)
current=vlist[0]
mst=dict()
weight_assigned=dict()
unvisited=[]
last=None
for v in vlist:
    unvisited.append(v)
while len(unvisited)!=0:
    for n in adli[current]:
        if n[0] != last:
            weight_assigned[n[0]]=int(n[1:])
    min_key=min(weight_assigned,key=weight_assigned.get)
    if min_key in mst:
        mst[min_key]=None
    mst[current]=min_key+str(weight_assigned[min_key])
    unvisited.remove(current)
    last=current
    current=min_key
    weight_assigned={}    
print(mst)
    
    
    