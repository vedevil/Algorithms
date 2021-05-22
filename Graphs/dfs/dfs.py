
def dfs(adli,vlist,start_vertex):
    head=start_vertex
    unvisited=vlist.copy()
    stack=[]
    dfs=[]
    while(len(unvisited)!=0):
        dfs.append(head)
        unvisited.remove(head)
        if head in adli:
            neighbourww=adli[head]
            neighbours=[]
            for n in neighbourww:
                e=list(n)[0]
                neighbours.append(e)
            for e in neighbours:
                stack.append(e)
        if len(unvisited)!=0:
            head=stack.pop()
    return dfs

