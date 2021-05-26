import numpy as np
inp=input('Give string: ')
inp_list=list(inp)
x=np.array(inp_list)
unique_list=list(np.unique(x))
unique_terms=len(unique_list)
required_length=1
i=2
while unique_terms>i:
    required_length+=1
    i*=2
bincodes=[]
for i in range(unique_terms):
    s='0'*(required_length-(len(bin(i))-2))
    t=bin(i)[2:]
    bincodes.append(s+t)
it=0
print('Codes table: ')
for t in unique_list:
    print(t+'    '+str(bincodes[it]))
    it+=1
print("\nFixed length encoding: ")
for s in inp:
    ind=unique_list.index(s)
    print(bincodes[ind],end='')
    
