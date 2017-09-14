#!/usr/bin/env python3
"""steps for 3 disks: 
1. move 1st disk to destination   
2. 2nd disk to auxiliary
3. 1st disk to auxiliary      //moving n-1 disks to auxiliary
4. 3rd disk to destination    //moving nth disk to destination
5. 1st disk to source           ~~~
6. 2nd disk to destination    
7. 1st disk to destination    //moving n-1 disks to destination
Number of steps is 2^(n-1)
"""
numofdisks=int(input("Enter number of disks"))
step=0
def towerOfHanoi(n,source,destination,auxiliary):
    step=step+1
    if(n==1):
        print("%d. Move disk %d from %s to %s" %(step,n,source,destination))
        return
    else:
        towerOfHanoi(n-1,source,auxiliary,destination)
        print("%d. Move disk %d from %s to %s" %(step,n,source,destination))
        towerOfHanoi(n-1,auxiliary,destination,source)
towerOfHanoi(numofdisks,'Source','Destination','Auxiliary')