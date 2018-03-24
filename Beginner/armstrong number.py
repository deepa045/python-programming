n=int(raw_input())
temp=n
sum=0
count=len(str(n))
while(n>0):
  digit=n%10
  sum=sum+digit**count
  n=n/10
if (temp==sum):
  print "yes"
else:
  print "no"
  
