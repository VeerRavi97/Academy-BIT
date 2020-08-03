import math

n1=int(input("No of inputs in set 1 "))
print("Enter inputs in set 1");
l1={}
l2={}
l3={}
l4={}
l5={}
l6={}

for i in range(n1):
    ip=input()
    key,value=ip.split(" ")
    l1[key]=float(value)
   
n2=int(input("No of elements in set 2 "))
print("Enter inputs in set 2");

for i in range(n2):
    ip=input()
    key,value=ip.split(" ")
    l2[key]=float(value)

keys1=l1.keys()
keys2=l2.keys()
set1=set()
set2=set()
temp1=set()
temp2=set()

    
for i in keys1:
    set1.add(i)
for i in keys2:
    set2.add(i)
temp1=set1-set2
temp2=set2-set1
set1=temp1
set2=temp2


for i in keys1:
    for j in keys2:
        if (i==j):
            l3[i]=abs((l1[i])-(l2[i]))
            l4[i]=l3[i]*l3[i]

for i in set1:
    l3[i]=l1[i]
    l4[i]=l3[i]*l3[i]
for i in set2:
    l3[i]=l2[i]
    l4[i]=l3[i]*l3[i]

keys1=l3.keys()
keys2=l4.keys()

ans=0
ans2=0

for i in keys1:
    ans=ans+l3[i]
    ans2=ans2+l4[i]

EuclieanDistance=math.sqrt(ans2)
hammingDistance=ans
print("hamming Distance is "+str(ans))
print("Eucleadian Distance is "+str(ans2))
