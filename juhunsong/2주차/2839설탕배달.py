import sys

n = int(sys.stdin.readline())

count=0
if n%5==0:
    print (n//5)
else:
    while n>0:
        n = n-3
        count+=1
        if n%5==0:
            count+=(n//5)
            print(count)
            break
        elif n==0:
            print(count)
            break
        elif n==1 or n==2:
            print(-1)
            break