def determinant(A):
    if len(A) == 1:
        return A[0][0]
    if len(A) == 2:
        return A[0][0] * A[1][1] - A[0][1] * A[1][0]
    det = 0
    for c in range(len(A)):
        det += ((-1)**c) * A[0][c] * determinant([row[:c] + row[c+1:] for row in A[1:]])
    return det

if __name__=="__main__":
    A = [[3, 4, 5], [1, -1, 0], [8, 2, 7]]
    B = [[1, 2, 3, 4], [-1, 0, 0.5, 9], [0, -6, 0.7, 0.5], [4, 4, 2, 1]]
    C = [[3, 4, 5], [1, -1, 0], [-7, 7, 0]]
    detA = determinant(A)
    detB = determinant(B)
    detC = determinant(C)
    print('A =', A)
    print('det A =', detA)
    print('B =', B)
    print('det B =', detB)
    print('C =', C)
    print('det C =', detC)