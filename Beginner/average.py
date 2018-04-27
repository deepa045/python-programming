num=int(raw_input())
num2=raw_input().split()
num2=map(int,num2)
a=0
if num==len(num2):
  for i in num2:
    a=a+i
    avg=a/num
  print avg
