n1,n2=raw_input().split()
for n in range(int(n1)+1,int(n2)):
  if n>1:
    for a in range(2,n):
      if(n%a)==0:
        break
    else:
      print n,
