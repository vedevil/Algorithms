def iscycle(adli,vlist):
    cycle=False
    flag=dict()
    queue=[]
    for v in vlist:
        flag[v]=-1
    current=vlist[0]
    queue.append(current)
    while len(queue)!=0:
        explore=queue.pop(0)
        flag[explore]=1
        for n in adli[explore]:
            if flag[n]==0:
                cycle=True
            if flag[n]==-1:
                queue.append(n)
                flag[n]=0
    if cycle==True:
        return True
    else:
        return False
        