t=int(input())
for case in range(t):
    n=int(input())
    A=list(map(int,input().split()))
    B=list(map(int,input().split()))
    result=0
    T = []
    for i in range(n):
        T.append(-min(A[i],B[i]))
    rrr=min(T)
    j=T.index(rrr)
    for i in range(n):
        if i!=j:
            result+=max(A[i],B[i])

    result+=A[j]+B[j]
    print(result)

