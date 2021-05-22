import sys
sys.path.append('/home/ved/Documents/Skills/progrmming/Algorithms/Graphs/adjacency_list')
import adjacency_list as al
sys.path.append('/home/ved/Documents/Skills/progrmming/Algorithms/Graphs/dfs')
import dfs

def no_of_components(vlist,ed):
    a=al.create_adjacency_list(ed, vlist)
    vertices=vlist.copy()
    component=0
    while len(vertices) != 0:
        dfslist=dfs.dfs(a, vlist, vertices[0])
        component=component+1
        for v in dfslist:
            vertices.remove(v)
    return component

ver= input("list down all vertices of the graph as a string: ")
vlist=list(ver)
print("No of vertices in the graph is "+str(len(vlist)))
# print("\nEnter type of graph",end="")
# type=input("d for directed un for undirected: ")
print("\nList down edges of the graph")
print("eg. 12 5,23 2,31 5 and so on..",end="")
ed=input("where 12 5 shows if there is edge to edge 1 to 2 with edgeweight: ")
print("No. of edges  in the graph is "+str(len(ed.split(','))))

c=no_of_components(vlist, ed)
print(c)