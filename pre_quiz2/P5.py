def gauss_jordan(A, b):
    n = len(A)
    matrix = [A[i] + b[[i][0]] for i in range(n)]

    for i in range(n):
        rotate = matrix[i][i]
        matrix[i] = [x / rotate for x in matrix[i]]
    
        for r in range(n):
            if r != i:
                factor = matrix[r][i]
                matrix[r] = [matrix[r][j] - factor * matrix[i][j] for j in range(len(matrix[0]))] 
    
    x = [[matrix[i][-1]] for i in range(n)]
    return x 

if __name__ == '__main__':
    A = [[4,1,1], [1, 2, -2], [1, 2, 3]]
    b = [[6], [9], [10]]
    x = gauss_jordan(A,b)
    print('Gaussian-Jordan elimination:')
    print("A=", A)
    print("b=", b)
    print("x=", x)