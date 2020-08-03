# -*- coding: utf-8 -*-
"""
Created on Wed Jul 25 20:14:41 2018

@author: VeerRavi
"""
a={}
b={}
print("Enter the number of inputs in A :")
m=int(input())

print("Enter the number of inputs in B :" )
n=int(input())

print("Enter the elememts in A")

for i in range(0,m):
  k,v=input().split( )
  a[int(k)]=float(v)
  
print("Enter the elememts in B")
for i in range(0,n):
  k,v=input().split( )
  b[int(k)]=float(v)
  
union={}

for  k1,v1 in a.items():
  for k2,v2 in b.items():
    v=-1
    if(k1==k2):
      v=max(v1,v2)
      union[k1]=v
    else:
      union[k1]=v1
      if(union.get(k2)==None):
       union[k2]=v2
      

intersection={}

for  k1,v1 in a.items():
  for k2,v2 in b.items():
    v=-1
    if(k1==k2):
      v=max(v1,v2)
      intersection[k1]=v
    


ComplimentofA={}

for k,v in a.items():
  ComplimentofA[k]=1-v;
  
  
ComplimentofB={}

for k,v in b.items():
  ComplimentofB[k]=1-v;
