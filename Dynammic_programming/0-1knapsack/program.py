import numpy as np
with open('input.txt','r') as f:
    n=int(f.readline().split('\n')[0])
    items=np.zeros((n,2))
    for i in range(n):
        a=f.readline().split('\n')[0]
        items[i][0]=int(a.split(' ')[0])
        items[i][1]=int(a.split(' ')[1])
    items=items[items[:,0].argsort()]
    max_weight=int(f.readline().split('\n')[0])
    matrix=np.zeros((n+1,max_weight+1))
    for i in range(1,n+1):
        for j in range(1,max_weight+1):
            if j-items[i-1][0]>=0:
                ind=int(j - items[i-1][0])
                val=max(matrix[i-1][j],matrix[i-1][ind]+items[i-1][1])
            else:
                val=matrix[i-1][j]
            matrix[i][j]=val
print(matrix)
max_profit=matrix[n][max_weight]
print('Max profit is: '+str(max_profit))
profit_remains=max_profit
for i in range(n,0,-1):
   l=list(matrix[i][:])
   if profit_remains in l:
       ind=l.index(int(profit_remains))
       if matrix[i][ind]!=matrix[i-1][ind]:
           print('Weight: '+str(items[i-1][0]),end=' ')
           print('Value: '+str(items[i-1][1]))
           profit_remains-=items[i-1][1]