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
mst_edges=[]
weight_assigned=dict()
assigned_to=dict()
unvisited=[]
mstset=[]
weight=0
for v in vlist:
    unvisited.append(v) 
while len(unvisited)!=0:
    for n in adli[current]:
        if n[0] not in mstset:
            if n[0] in weight_assigned and int(n[1:])<weight_assigned[n[0]]:
                assigned_to[n[0]]=current
                weight_assigned[n[0]]=int(n[1:])
            if n[0] not in weight_assigned:
                assigned_to[n[0]]=current
                weight_assigned[n[0]]=int(n[1:])
    unvisited.remove(current)
    if len(unvisited)!=0:
        min_key=min(weight_assigned,key=weight_assigned.get)
        mst_edges.append(str(assigned_to[min_key])+str(min_key))
        weight+=weight_assigned[min_key]
        mstset.append(current)
        current=min_key
        weight_assigned.pop(min_key)
        assigned_to.pop(min_key)
print(mst_edges)
print("weight of the tree is: "+str(weight))
    
    
    