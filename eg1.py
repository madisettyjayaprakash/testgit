#!/bin/python3

import sys
def fun1(n2,k2):
    a3=[]
    h=0
    fun2(n2,k2,a3,h)

def fun2(n1,k1,a1,i):
    if(k1==1):
        s=0
        for x in range(0,i+1):
            print(a1[x])
            s=s+int(a1[x])
        if s==n1:
            p=1
            q=int(a1[0])
            for x in range(0,i+1):
                s2=0
                for z in range(p+1,q+1):
                    s2=s2+((x_i[z]-x_i[p])*w_i[z])
                a2=a2+list(str(s2))
                t1=q
                t2=p
                p=t1
                q=t1+t2
    elif k1>1:
        for l in range(1,n1):
            a1=a1+list(str(l))
            #print(a1)
            fun2(n1,k1-1,a1,l)
                    
    

    
a2=[]
n,k = input().strip().split(' ')
n,k = [int(n),int(k)]
for a0 in range(n):
    x_i,w_i = input().strip().split(' ')
    x_i,w_i = [int(x_i),int(w_i)]
fun1(n,k)
print(a2)       
