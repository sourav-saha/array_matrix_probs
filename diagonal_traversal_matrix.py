## Hackerrank problem link:
## https://www.hackerrank.com/contests/smart-interviews/challenges/si-diagonal-traversal-of-matrix/problem

def one_diagonal_sum(A, si, sj, N):
    s = 0
    while si < N and sj < N:
        s += A[si][sj]
        si += 1
        sj += 1
    return s
    
def diagonal_sum(A, N):
    result = []
    #upper matrix sum
    for j in reversed(range(N)):
        result.append(one_diagonal_sum(A, 0, j, N))
    #lower matrix sum
    for i in range(1, N):
        result.append(one_diagonal_sum(A, i, 0, N))
        
    for x in range(len(result)):
        print(result[x], end=' ')
    print()

if __name__ == "__main__":
    T = int(input().strip())
    for ti in range(T):
        N = int(input().strip())
        A = []
        for ni in range(N):
            rowList = list(map(int, input().strip().split(' ')))
            A.append(rowList)
            
        diagonal_sum(A, N)
