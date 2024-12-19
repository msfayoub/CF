fin = open('lifeguards.in', 'r')
fout = open("lifeguards.out", "w")

n=int(fin.readline().strip())
pairs=[]
in_out=[]


for i in range(n):
    X=tuple(map(int,fin.readline().split()))
    pairs.append(X)
    in_out.append((X[0],1))
    in_out.append((X[1],-1))


A=[0 for i in range(2*n)]
in_out.sort()
pairs.sort()
A[0]=in_out[0][1]
for i in range(1,2*n):
    A[i]=A[i-1]+in_out[i][1]

m = min(1000000000, min(pairs[1][0], pairs[0][1]) - pairs[0][0])

for i in range(1, n - 1):
    x = min(pairs[i][1], pairs[i + 1][0]) - max(pairs[i][0], pairs[i - 1][1])
    if x > 0:
        m = min(m, x)
    else:
        m = 0
        break

if n > 1 and m != 0:
    if pairs[n - 1][1] > pairs[n - 2][1]:
        m = min(m, pairs[n - 1][1] - pairs[n - 2][1])


somme=0
for i in range(2*n):
    if A[i]>0:
        if i+1<2*n:
            somme+=in_out[i+1][0]-in_out[i][0]

result=0
with open('lifeguards.out', 'w') as outfile:
    outfile.write(str(somme-m)+'\n')
