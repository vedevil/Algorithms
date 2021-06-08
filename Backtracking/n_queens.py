import numpy as np
total=0
def under_attack(m,r,c): 
    underattack=False
    num_rows,num_cols=m.shape
    count=0
    for row in range(num_rows):
        if m[row][c]=='Q':
            count+=1
    if count>1:
        underattack= True
    if r>c:
        while c>=0:
            if 
    return underattack
   
def n_queens(si,ei,m):
    if si==ei+1:
        global total
        total+=1
        print(m,end='\n\n')
    else:
        for i in range(ei+1):
            m[si][i]='Q'
            if not under_attack(m,si,i):
                n_queens(si+1, ei, m)
            m[si][i]='.'

length=int(input('No of Queens: '))
m=np.full((length,length), '.')
n_queens(0, length-1, m)
print('\n\nTotal  such arrangement possible: '+str(total))