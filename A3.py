n=7
count=0
i=1
while(i<=n):
    if(n%i==0):
        count+=1
if(count==2):
    print("Prime")
else:
    print("Not a prime")
