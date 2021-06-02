num=int(input('Find which fibonaccinumber: '))
l=[]
for i in range(num):
    l.append(-1)
l[0]=0
l[1]=1
if num > 2:
    for i in range(2,num):
        l[i]=l[i-1]+l[i-2]
    print(str(num)+'th fibonacci number is: '+str(l[num-1]))
if num ==1:
    print(str(num)+'st fibonacci number is: '+str(l[num-1]))
if num ==2:
    print(str(num)+'nd fibonacci number is: '+str(l[num-1]))