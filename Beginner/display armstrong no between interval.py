n1,n2=raw_input().split()
for i in range(int(n1)+1,int(n2)):
  temp=i
  sum=0
  count=len(str(i))
  while(temp>0):
    digit=temp%10
    sum=sum+digit**count
    temp=temp/10
  if(i==sum):
   print i,
