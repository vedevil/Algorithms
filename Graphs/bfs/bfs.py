
def bfs(adli,vlist,start_vertex):
    head=start_vertex
    unvisited=vlist.copy()
    queue=[]
    bfs=[]
    while(len(unvisited)!=0):
        if head in unvisited:
            bfs.append(head)
            unvisited.remove(head)
            if head in adli:
                neighbourww=adli[head]
                neighbours=[]
                for n in neighbourww:
                    e=list(n)[0]
                    neighbours.append(e)
                for e in neighbours:
                    queue.append(e)
        if len(unvisited)!=0:
            head=unvisited[0]
    return bfs

