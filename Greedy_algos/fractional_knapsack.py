n=int(input("No. of items to be put in knapsack? " ))
weight_limit=int(input("What is capacity of your knapsack? "))
inp=dict()
inp['object_name']=[]
inp['weight']=[]
inp['value']=[]
out=dict()
out['object_name']=[]
out['weight']=[]
out['value']=[]
ratio=[]
ks_value=0
print("Enter item and its attributes as follows ")
print("item_name weight value value")
for i in range(n):
    s=input("Enter object name,weight and value of item "+str(i+1)+": ")
    l=s.split(" ")
    inp['object_name'].append(l[0])
    inp['weight'].append(int(l[1]))
    inp['value'].append(int(l[2]))
    ratio.append(int(l[2])/int(l[1]))
while weight_limit!=0:
    max_value=max(ratio)
    ind=ratio.index(max_value)
    if inp['weight'][ind]<= weight_limit:
        ks_value=ks_value+inp['value'][ind]
        weight_limit=weight_limit-inp['weight'][ind]
        out['object_name'].append(inp['object_name'][ind])
        out['weight'].append(inp['weight'][ind])
        out['value'].append(inp['value'][ind])
        inp['object_name'].pop(ind)
        inp['weight'].pop(ind)
        inp['value'].pop(ind)
    else:
        ks_value=ks_value+ratio[ind]*weight_limit
        out['object_name'].append(inp['object_name'][ind])
        out['weight'].append(weight_limit)
        out['value'].append(ratio[ind]*weight_limit)
        inp['object_name'].pop(ind)
        inp['weight'].pop(ind)
        inp['value'].pop(ind)
        weight_limit=0
print("items knapsack can hold are: ")
for i in range(len(out['object_name'])):
    print(str(out['object_name'][i])+str("   ")+str(out['weight'][i])+str("   ")+str(out['value'][i]))
print("value of items in knasack is "+str(ks_value))