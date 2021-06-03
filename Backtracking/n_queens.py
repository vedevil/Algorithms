import numpy as np

def underattack(m): 
    under_attack=False
    num_rows,num_cols=m.shape
    for row in range(num_rows):
        count=0
        for column in range(num_cols):
            if m[row][column]=='Q':
                count+=1
        if count>1:
            under_attack= True
            return under_attack
    for column in range(num_cols):
        count=0
        for row in range(num_rows):
            if m[row][column]=='Q':
                count+=1
        if count>1:
            under_attack= True
            return under_attack
        
def n_queens(si,ei,m):
    if si==ei+1:
        print(m,end='\n\n')
    else:
        for i in range(ei+1):
            m[si][i]='Q'
            if not underattack(m):
                n_queens(si+1, ei, m)
            m[si][i]='.'

length=int(input('No of Queens: '))
m=np.full((length,length), '.')
n_queens(0, length-1, m)