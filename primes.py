"""This module contains 1 Function that
return list of primes as default
and check prime if commanded"""
def primechecker(target,check=False):
    # the idea is creating list of places
    #initiated to False then initialize first 2 numbers
    #to deduce the rest from the odd ones and set there
    #places to True    
    l=[False]*(target+1)
    l[2],l[3]=True,True
    for i in range(5,target+1,2):
        for j in range(2,int(i**0.5)+1):
            if l[j]:
                if i%j==0:
                    l[i]=False
                    break
                l[i]=True
    p=[i for i in range(target+1) if l[i]]
    if check:
        return l[target]
    else:
        return p
