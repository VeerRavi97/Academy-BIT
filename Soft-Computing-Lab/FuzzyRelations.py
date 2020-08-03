import numpy as np
       //incomplete 
def Containment(x,y,m,n):
   z = []
   
   for i in range(0,m*n+1):
        x1=i//m
        y1=i%m
        ans=0
        num1=x[x1][y1]
        num2=y[x1][y1]
        if num1<=num2:
          ans=1;
        z.append(ans)
   return np.array(z).reshape((m,n)) 


def maxMin(x, y):
    z = []
    for x1 in x:
        for y1 in y.T:
            z.append(max(np.minimum(x1, y1)))
    return np.array(z).reshape((x.shape[0], y.shape[1]))

def maxProduct(x, y):
    z = []
    for x1 in x:
        for y1 in y.T:
            z.append(max(np.multiply(x1, y1)))
    return np.array(z).reshape((x.shape[0], y.shape[1]))



def Compliment(r):
   z = []
   for x in r:
      z.append(1-x)
   return z        
      
 
 


print("Enter your Choice\n 1.For MaxMin\n 2.For MaxProduct\n 3.For Compliment\n 4.For Containment\n")
choice=int(input());


r1 = np.array([[1, 0, .7], [.3, .2, 0], [0, .5, 1]])
r2 = np.array([[.6, .6, 0], [0, .6, .1], [0, .1, 0]])
r3=np.array([[.5,.8],[.1,1],[0,.6]])
r4=np.array([[.4,.6,0],[.9,1,.1]])


if choice==1:
    print("Enter the dimensions of R")
    m,n=input().split();
    m=int(m)
    n=int(n)
    print("Enter the inputs in R ");
    r=[];
    for i in range(0,m*n):
        num=float(input())
        r.append(num)
    r=np.array(r).reshape(m,n)
    
    print("Enter the dimensions of S")
    m,n=input().split();
    m=int(m)
    n=int(n)
    print("Enter the inputs in S ");
    s=[];
    for i in range(0,m*n):
        num=float(input())
        s.append(num)
    s=np.array(s).reshape(m,n) 
    ans=maxMin(r,s)

elif choice==2:
    print("Enter the dimensions of R")
    m,n=input().split();
    m=int(m)
    n=int(n)
    print("Enter the inputs in R ");
    r=[];
    for i in range(0,m*n):
        num=float(input())
        r.append(num)
    r=np.array(r).reshape(m,n)
    
    print("Enter the dimensions of S")
    m,n=input().split();
    m=int(m)
    n=int(n)
    print("Enter the inputs in S ");
    s=[];
    for i in range(0,m*n):
        num=float(input())
        s.append(num)
    s=np.array(s).reshape(m,n) 
    ans=maxProduct(r,s)

elif choice==3:
    print("Enter the dimensions of R")
    m,n=input().split();
    m=int(m)
    n=int(n)
    print("Enter the inputs in R ");
    r=[];
    for i in range(0,m*n):
        num=float(input())
        r.append(num)
    ans=Compliment(r)
    Compliment=np.array(ans).reshape(m,n) 
    
    

elif choice==4:
    print("Enter the dimensions of R")
    m,n=input().split();
    m=int(m)
    n=int(n)
    print("Enter the inputs in R ");
    r=[];
    for i in range(0,m*n):
        num=float(input())
        r.append(num)
    r=np.array(r).reshape(m,n)
    
    print("Enter the dimensions of S")
    m,n=input().split();
    m=int(m)
    n=int(n)
    print("Enter the inputs in S ");
    s=[];
    for i in range(0,m*n):
        num=float(input())
        s.append(num)
    s=np.array(s).reshape(m,n) 
    ans=Containment(r,s,m,n)
