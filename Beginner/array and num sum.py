num,array=raw_input().split()
k=raw_input().split()
if int(num)==len(k):
  k=map(int,k)
  val=k[0:int(array)]
  print sum(i for i in val)
