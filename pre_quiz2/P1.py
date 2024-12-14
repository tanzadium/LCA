def transpose(A):
    return [[A[j][i] for j in range(len(A))] for i in range(len(A[0]))]

A = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12],[-1, -2, -3, -4]]

At = transpose(A)

print(A)
print('is transposed to')
print(At)