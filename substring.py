s=input()
s=s.lower()
count={}
sum=0
for i in s:
    if i in count:
        count[i]+=1
    else:
        count[i]=1

for v in count.values():
    if v==1 or v>1:
       sum=sum+1
print(sum)
