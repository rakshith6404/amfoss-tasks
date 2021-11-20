a=0
b=1
sum=0
N=int(input())
for i in range(0,N):
  num=int(input())
  while b<=num:
    if b%2==0:
      sum+=b
    a,b=b,a+b
  print(sum)

