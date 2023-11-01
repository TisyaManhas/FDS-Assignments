from __future__ import print_function
n=int(input("Enter the highest power of the polynomial:"))
A=[]

for i in range(0,n+1):
    B=[]
    c=int(input("Enter the coefficient:"))
    p=int(input("Enter the power:"))
    B.append(c)
    B.append(p)
    A.append(B)
for i in range(len(A)-1):
    x1=A[i]
    print(x1[0],"x^",x1[1],"+",end="")
x1=A[len(A)-1]
print(x1[0],"x^",x1[1])

n2=int(input("Enter the highest power of the second polynomial:"))
A2=[]

for i in range(0,n2+1):
    B2=[]
    c=int(input("Enter the coefficient:"))
    p=int(input("Enter the power:"))
    B2.append(c)
    B2.append(p)
    A2.append(B2)
for i in range(len(A2)-1):
    x1=A2[i]
    print(x1[0],"x^",x1[1],"+",end="")
x1=A2[len(A2)-1]
print(x1[0],"x^",x1[1])