n2,k=map(int,input().split())
m=list(map(int,input().split()))
if k==1:
    print(min(l))
elif k==2:
    print(max(l[0],l[n2-1]))
else:
    print(max(l))
