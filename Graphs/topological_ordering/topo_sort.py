import sys
sys.path.append('/home/ved/Documents/Skills/progrmming/Algorithms/Graphs/adjacency_list')
import adli_without_weight_directed as al


def indegree_calculation(elist,vlist):
    edges=elist.split(',')
    in_degree=dict()
    for v in vlist:
        in_degree[v]=0
    for e in edges:
        to=e[1]
        if to in in_degree:
            in_degree[to]+=1
        else:
            in_degree[to]=1
    return in_degree
def topological_sort(elist,vlist):
    topo=[]
    in_deg=indegree_calculation(elist,vlist)
    min_key=min(in_deg,key=in_deg.get)
    a=al.create_adjacency_list(elist,vlist)
    for i in range(len(vlist)):
        if in_deg[min_key]!=0:
            print("Its not DAG")
            topo=None
            break
        else:
            in_deg.pop(min_key)
            topo.append(min_key)
            if min_key in a:
                if len(a[min_key])!=0:
                    for n in a[min_key]:
                        in_deg[n]-=1
            if len(in_deg)!=0:
                min_key=min(in_deg,key=in_deg.get)
    return topo
        