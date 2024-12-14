def matdot(A,B):
    if len(A[0]) != len(B):
        return None
    result = [[0] * len(B[0]) for _ in range(len(A))]
    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(B)):
                result[i][j] += A[i][k] * B[k][j]
    return result
if __name__=="__main__":
    A = [[1, 2, 3], [-1, 0, 4]]
    B = [[10, 20], [5, -2], [7, 9]]
    M = [[8], [6]]
    AB = matdot(A, B)
    BA = matdot(B, A)
    AM = matdot(A, M)
    BM = matdot(B, M)
    print('A=', A)
    print('B=', B)
    print('A dot B =', AB)
    print('B dot A =', BA)
    print('A dot M =', AM)
    print('B dot M =', BM)