num=int(raw_input())
num1=raw_input().split()
if num==len(num1):
  num1=map(int,num1)
  a=sorted(num1)
  for b in a:
    print b,
