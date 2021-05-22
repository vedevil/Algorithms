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

