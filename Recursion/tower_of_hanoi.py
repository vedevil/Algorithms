def tower_of_hanoi(n,source,auxiliary,destination):
    if n==0:
        return
    else:
        tower_of_hanoi(n-1,source, destination,auxiliary)
        print('Move disc from '+source+' to '+destination)
        tower_of_hanoi(n-1, auxiliary, source, destination)
l=input('Enter pole names(seperated by space) \nIn order: ').split(' ')
num=int(input('Enter no. of disc'))
tower_of_hanoi(num, l[0], l[1], l[2])