X = list(map(int, input().split()))
n, m, k = X[0], X[1], X[2]
operations = []
A = list(map(int, input().split()))
for i in range(m):
    operations.append(list(map(int, input().split())))
B = [0] * n
D = [0] * m
for _ in range(k):
    order = list(map(int, input().split()))
    li, ri = order[0] - 1, order[1]
    D[li]+=1
    if ri<m:
        D[ri]-=1

li, ri, di = operations[0][0] - 1, operations[0][1], operations[0][2] * D[0]
B[li] += di
if ri < n:
    B[ri] -= di

for ele in range(1,m):
    D[ele]+=D[ele-1]
    li, ri, di = operations[ele][0] - 1, operations[ele][1], operations[ele][2] * D[ele]
    B[li] += di
    if ri < n:
        B[ri] -= di


A[0] += B[0]
print(A[0], end=' ')
for i in range(1, n):
    B[i] += B[i - 1]
    A[i] += B[i]
    print(A[i], end=' ')
