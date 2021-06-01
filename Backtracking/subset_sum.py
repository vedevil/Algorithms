def subset_sum(subset,si,ei,node,weight,sol):
    if node['sw']==weight:
        print(sol)
    if si==ei:
        return
    else:
        for i in range(2):
            if node['sw']<weight and node['wr']+node['sw']>=weight:
                if i==0:
                    node['sw']+=0
                    node['wr']-=0
                    subset_sum(subset, si+1, ei, node,weight,sol)
                    node['sw']-=0
                    node['wr']+=0
                else:
                    node['sw']+=subset[si]
                    node['wr']-=subset[si]
                    sol.append(subset[si])
                    subset_sum(subset, si+1, ei, node,weight,sol)
                    node['sw']-=subset[si]
                    node['wr']+=subset[si]
                    sol.pop()
subset_s=input("Enter universal subset").split(" ")
subset=list(map(lambda x:int(x), subset_s))
weight=int(input("Enter required sum"))
node=dict()
node['sw']=0
node['wr']=sum(subset)
solution=[]
subset_sum(subset, 0, len(subset), node, weight,solution)