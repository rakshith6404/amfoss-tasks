def enter_value(N):
    sum = N*(N+1)//2
    return sum
n=int(input())
for i in range(0,n):
    v=int(input())
    v-=1
    a=v//3
    b=v//5
    c=v//10
    c=v//15
    print(3*enter_value(a)+5*enter_value(b)-15*enter_value(c))
    n-=1

   