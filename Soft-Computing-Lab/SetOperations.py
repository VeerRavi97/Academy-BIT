
 
print(F"Enter the number of elements in A ")

m=int(input())




print(F"Enter the number of elements in B ")

n=int(input())


print(F"Enter the number of elements in U ")

p=int(input())

a=set()
b=set()
u=set()

print(F"Enter the elements in A ")

for index in range(0,m):
   x=input()
   a.add(int(x))

print(F"Enter the elements in B ")

for index in range(0,n):
   x=int(input())
   b.add(x)


print(F"Enter the elements in Universal ")

for index in range(0,p):
   x=int(input())
   u.add(x)


 
# union
print("Union :", a | b)
 
# intersection
print("Intersection :", a & b)
 
# difference
print("Difference :", a - b)
 
# symmetric difference
print("Symmetric difference :", a ^ b)

print("UNIVERSAL :",u)

def Diff(li1, li2):
    return (list(set(li1) - set(li2)))
 
# Driver Code
li=list(u)
li1 = list(a)
li2 = list(b)
print(F"compliment of A")
print(Diff(li, li1))


print(F"compliment of B")
print(Diff(li, li2))
