n=int(input("No. of jobs: "))
availibilty=int(input("input no. of slots available: "))
inp=dict()
inp["job_name"]=[]
inp["profit"]=[]
inp["deadline"]=[]
for i in range(n):
    print("\nenter details of job "+str(i+1)+" in order of",end="")
    a=input("job_name profit deadline: ")
    l=a.split(" ")
    inp['job_name'].append(l[0])
    inp['profit'].append(int(l[1]))
    inp['deadline'].append(l[2])
out=[]
profit=0
for i in range(availibilty):
    out.append('free0')
for j in range(n):
    max_profit=max(inp['profit'])
    ind=inp['profit'].index(max_profit)
    d=int(inp['deadline'][ind])
    if d> availibilty:
        d=availibilty
    if d <= availibilty:
        for s in range(d-1,-1,-1):
            if out[s]=='free0':
                out[s]=inp['job_name'][ind]
                profit=profit+int(inp['profit'][ind])
                break
    inp['job_name'].pop(ind)
    inp['profit'].pop(ind)
    inp['deadline'].pop(ind)
                
    
print('\nSequence of the jobs should be:  ',end="")
print(out)
print('Max profit is :'+str(profit))