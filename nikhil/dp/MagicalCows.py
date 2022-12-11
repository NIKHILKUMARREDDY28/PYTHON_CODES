C,N,M = map(int,input().split())
ini = [0 for i in range(N)]
for i in range(N):
    ini[i] = int(input())

prev = [0 for i in range(N+1)]
for i in ini:
    prev[i] += 1
ans =[]
for i in range(0,M  ):
    today = [0 for k in range(N+1)]
    for c in range(1,N+1):
        if 2 * c <= C :
            today[2 * c] += prev[c]
            #print(today[2*c])
        else:
            today[c] += 2 * prev[c]
            #print(today[c])
    ans.append(sum(prev))
    prev = list(today)
for i in ans:
    print(i)

