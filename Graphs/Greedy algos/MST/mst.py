import sys
sys.path.append('/home/ved/Documents/Skills/progrmming/Algorithms/Graphs/adjacency_list')
import adjacency_list as al

def create_mst(adlist,vlist):
    stack=[]
    mst=dict()
    head=vlist[0]
    neighbours=adlist[head]
    w=[]
    for n in neighbours:
        w.append(int(list(n)[1])
    min_value = min(w)
    min_index = a_list.index(min_value)
    vlist.remove(head)
    mst
    head=list(adlist[head][min_index])[0]    
    

