n=int(input("Enter total number of students:" ))
L=[]
sum=0
x=0
p=0
f=0
for i in range(0,n):
    m=int(input("Enter marks out of 100:"))
    if(m>=0):
        sum+=m
        L.append(m)  
    if(m<0):
        x=x+1

avg=sum/(n-x)

for i in range(0,n-x):
    if(L[i]>=60):
        p=p+1 
    else:
        f=f+1

print("Average of marks obtained:")
print(avg)
max=L[0]
min=L[0]
for i in range(0,n-x):
    if(L[i]>max):
        max=L[i]

    if(L[i]<min):
        min=L[i]
print("Highest marks:",max)
print("Lowest marks:",min)

print("Number of absent students:")
print(x)
pp=(p*100)/(n-x)
fp=(f*100)/(n-x)
print("Percentage of pass students:",pp)
print("Percentage of fail students:",fp)

print("Marks of 3 toppers:")
freq={}
for i in L:
    if(i in freq):
        freq[i]+=1
    else:
        freq[i]=1
key1=list(freq.keys())
val1=list(freq.values())
key1.sort()
val1.sort()
print(key1[len(key1)-1])
print(key1[len(key1)-2])
print(key1[len(key1)-3])
k=val1[len(val1)-1]
for key,value in freq.items():
	if k==value:
		print("marks with highest freq",key)




        

