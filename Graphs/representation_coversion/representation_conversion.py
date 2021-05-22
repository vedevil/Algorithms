
import numpy as np

def adlisttoadmatrix(adli,vlist):
    matrix=np.zeros((len(vlist),len(vlist)))
    for k in adli:
        frin=vlist.index(k)
        for ele in adli[k]:
            to=list(ele)[0]
            toin=vlist.index(to)
            w=int(list(ele)[1])
            matrix[frin][toin]=w
    return matrix            


        
        