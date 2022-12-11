def setrowsZero(row):
    rowsize = len(row)
    for i in range(rowsize):
        row[i] = -1


def setcolumnzero(matrix, column):
    rowsize = len(matrix)
    for i in range(rowsize):
        matrix[i][column] = -1




def setZeros(matrix ):
    # Write your code here.
    rowsize = len(matrix)
    colsize = len(matrix[0])

    for row in range(rowsize):
        for column in range(colsize):
            if matrix[row][column] == 0:
                setrowsZero(matrix[row])
                setcolumnzero(matrix, column)

T = int(input())
for i in range(T):
    N, M = map(int, input().split())
    matrix = []
    for i in range(N):
        arr = input().split()
        arr = list(map(int,arr))
        matrix.append(arr)
    setZeros(matrix)
    for i in range(N):
        for j in range(M):
            if matrix[i][j]== -1:
                matrix[i][j] = 0

    print(matrix)