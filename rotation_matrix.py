## Hackerrank problem link:
## https://www.hackerrank.com/contests/smart-interviews/challenges/si-rotation-of-matrix/problem

def rotation_matrix(tn, A, N):
    tmp_mat = []
    
    #transpose of the original matrix
    for i in range(N):
        tmp_list = []
        for j in range(N):
            tmp_list.append(A[j][i])
        tmp_mat.append(tmp_list)
            
    print(f'Test Case #{tn}:')
    #print the transpose matrix in reverse order
    for i in range(N):
        for j in reversed(range(N)):
            print(tmp_mat[i][j], end=' ')
        print()

if __name__ == "__main__":
    T = int(input().strip())
    for ti in range(T):
        N = int(input().strip())
        mat = [] #empty matrix
        for ni in range(N):
            rowList = list(map(int, input().strip().split(' ')))
            mat.append(rowList)
        rotation_matrix(ti+1, mat, N)
