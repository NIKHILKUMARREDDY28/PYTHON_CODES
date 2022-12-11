m = int(input())
n = int(input())
P = [0] * (n+1)
def f(n):
    P[0] = 1
    i = 3
    while (i * i <= n):
        if (P[i // 2] == 0):
            for j in range(3 * i, n + 1, 2 * i):
                P[j // 2] = 1

        i += 2
if __name__ == "__main__":
    f(n)
    for i in range(m, n + 1):
        if (i == 2):
            print(i, end=" ")
        elif (i % 2 == 1 and P[i // 2] == 0):
            print(i, end=" ")