with open('input.txt', 'r') as f:
    stages=int(f.readline().split('\n')[0])
    vlist=dict()
    cost=dict()
    assigned=dict()
    inf=999999
    for i in range(stages):
        l=f.readline().split('\n')[0].split(' ')
        if i not in vlist:
            vlist[i]=[]
        for v in l:
            vlist[i].append(v)
            cost[v]=inf
            assigned[v]=None
    cost[v]=0
    edges_to=dict()
    edges_from=dict()
    for stage in vlist:
        for v in vlist[stage]:
            edges=f.readline().split('\n')[0].split(',')
            for e in edges:
                if e[0] not in edges_to:
                    edges_to[e[0]]=[]
                edges_to[e[0]].append(e[1:])
#                 if e[1] not in edges_from:
#                     edges_from[e[1]]=[]
#                 edges_from[e[1]].append(e[0]+' '+e[3])
for stage in range(stages-2,-1,-1):
    for v in vlist[stage]:
        for e in edges_to[v]:
            w=int(e.split(' ')[1])
            pv=e.split(' ')[0]
            if cost[v]>cost[pv]+w:
                cost[v]=cost[pv]+w
                assigned[v]=pv
current=vlist[0][0]
for i in range(stages-1):
    print(current,end='')
    current=assigned[current]
    print('----------->',end='')
print(current)
print('\n\nMinimum cost is: '+str(cost[vlist[0][0]]))

                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
