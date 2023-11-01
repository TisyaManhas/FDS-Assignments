n=int(input("Enter total number of students:"))
a=int(input("Enter the number of students playing cricket:"))
b=int(input("Enter the number of students playing badminton:"))
c=int(input("Enter the number of students playing football:"))
La=[]
Lb=[]
Lc=[]
print("Enter roll no of cricketers:")
for i in range(0,a):
    m=int(input())
    La.append(m)
print("Enter roll no of badminton players:")
for i in range(0,b):
    m2=int(input())
    Lb.append(m2)
print("Enter roll no of football players:")
for i in range(0,c):
    m3=int(input())
    Lc.append(m3)
count1=0
print("Roll No List of students who play both cricket and badminton: ")
for i in La:
    for j in Lb:
        if i==j:
            print(i)
            count1=count1+1                     #play both cricket and badminton
count2=0
for i in Lb:
    for j in Lc:
        if i==j:
            count2=count2+1                     #play both badminton and football
count3=0
for i in La:
    for j in Lc:
        if i==j:
            count3=count3+1                     #play both cricket and football
""" print("Roll No List of students who play either cricket or badminton but not both: ")
for i in La:
    for j in Lb:
        if i!=j:
            print(j) """
# no of students who play all the sports
x=0
for i in La:
    for j in Lb:
        for k in Lc:
            if i==j and i==k and j==k:
                x=x+1                              #count of students playing all the sports                             

y=n-(a+b+c)+x                                     #no of students who do not play any sport
count1=0
""" print("Number of students who play neither cricket nor badminton: ")
for i in Lc:
    for j in La:
        for k in Lc:
            if i!=j and i!=k:
                count1=count1+1
count1=count1+y   """
""" print(count1)                                    #adding no of students who play no game
print("Number of students who do not play any game: ")
print(y)
 """

 for s in range(0,i):
    for p in range(0,j):
        M[s][p]=0
        for k in range(0,i):
            M[s][p]+=L1[s][p]*L2[p][s]
for p in range(0,i):                                           #Subtracted Matrix       
    print(M[p] )
print