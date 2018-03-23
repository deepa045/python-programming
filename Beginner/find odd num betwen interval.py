n1,n2=raw_input().split()
a=[]
for i in range(int(n1)+1,int(n2)):
  if(i%2==1):
    a.append(i)
for n in a:
  print n,
