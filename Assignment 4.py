from __future__ import print_function
n=int(input("Enter the degree of highest power:"))
c=[0]*(n+1)
for i in range(0,n+1):
    m=int(input("Enter value of c:"))
    c[i]=m
print("The polynomial is:")
for i in range(0,n):
    print(c[i],"x^",n-i,"+",end="")
print(c[n],"x^0")

#Evaluating at given value x
sum=0
x=int(input("Enter value of x:"))
for i in range(0,n+1):
    sum+=c[i]*(x**(n-i))
print(sum)

#Second Polynomial
n2=int(input("Enter the degree of highest power of second polynomial:"))
c2=[0]*(n2+1)
for i in range(0,n2+1):
    m2=int(input("Enter value of c:"))
    c2[i]=m2

print("The polynomial is:")
for i in range(0,n2):
    print(c2[i],"x^",n2-i,"+",end="")
print(c2[n2],"x^0")

""" y=min(n,n2)
y=y+1 """


""" k=0
while(k<=y):
    sum2=0
    sum2+=c[k]+c2[k]
    print(sum2,"x^",k,"+",end="")
    k=k+1

r=max(n,n2)
diff=r+1-y """

#Addition of Two Polynomials
print("Added polynomial:")
if(n>=n2):
    for i in range(0,n-n2):
        print(c[i],"x^",n-i,"+",end="")
    for i in range(0,n2):
        sum2=0
        sum2+=c[n-n2+i]+c2[i]
        print(sum2,"x^",n2-i,"+",end="")
    print(c[n]+c2[n2],"x^0")
elif(n2>n):
    for i in range(0,n2-n):
        print(c2[i],"x^",n2-i,"+",end="")
    for i in range(0,n):
        sum2=0
        sum2+=c2[n2-n+i]+c[i]
        print(sum2,"x^",n-i,"+",end="")
    print(c2[n2]+c[n],"x^0")

#Multiplication of Polynomials
print("Multiplication of the two polynomials:")
Q=[0]*(n+n2+1)
sum3=[0]*(n+n2+1)
for i in range(n):
    for j in range(n2):
        sum3[(n-i)+(n2-j)]+=c[i]*c2[j]
        Q[(n-i)+(n2-j)]=sum3[(n-i)+(n2-j)]

for i in range(0,n+n2):
    print(Q[i],"x^",i,"+",end="")
    #i=i-1
print(Q[n+n2],"x^",n+n2)





 