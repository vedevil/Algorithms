import numpy as np
total=0
def under_attack(m,r,c): 
    underattack=False
    num_rows,num_cols=m.shape
    for column in range(num_cols):
        count=0
        for row in range(num_rows):
            if m[row][column]=='Q':
                count+=1
        if count>1:
            underattack= True
    if r+1<num_rows:
        if m[r+1][c]=='Q':
            underattack=True
        if c+1<num_cols:
            if m[r+1][c+1]=='Q':
                underattack= True
        if c-1>=0:
            if m[r+1][c-1]=='Q':
                underattack= True
    if r-1>=0:
        if m[r-1][c]=='Q':
            underattack=True
        if c+1<num_cols:
            if m[r-1][c+1]=='Q':
                underattack= True
        if c-1>=0:
            if m[r-1][c-1]=='Q':
                underattack= True
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