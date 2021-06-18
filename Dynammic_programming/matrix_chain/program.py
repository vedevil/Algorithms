import numpy as np
with open('input.txt','r') as f:
    n=int(f.readline().split('\n')[0])
    inf=999999
    matrix_dim=np.full((n,2),0)
    matrix_val=np.full((n,n),inf)
    matrix_par=np.full((n,n),0)
    for i in range(n):
        dim=f.readline().split('\n')[0]
        d1,d2=dim.split(' ')[0],dim.split(' ')[1]
        matrix_dim[i][0]=d1
        matrix_dim[i][1]=d2
for i in range(n):
    matrix_val[i][i]=0
for d in range(1,n):
    for i in range(n-d):
        j=i+d
        for k in range(i,j):
            val=matrix_val[i][k]+matrix_val[k+1][j]+matrix_dim[i][0]*matrix_dim[k+1][0]*matrix_dim[j][1]
            if val<matrix_val[i,j]:
                matrix_val[i,j]=val
                matrix_par[i][j]=k+1
        # else:
        #     matrix_val[i][j]=matrix_dim[i][0]*matrix_dim[j][0]*matrix_dim[j][1]
print(matrix_val)
print(matrix_par)
print('Minimal '+str(matrix_val[0][n-1])+' operations are required')
    
        
