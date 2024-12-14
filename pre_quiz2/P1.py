def transpose(matrix):
    dimension  = len(matrix[0])
    L = sum(matrix, [])
    return [L[i::dimension] for i in range(dimension)]
  
if __name__ == '__main__':
    A = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [-1, -2, -3, -4]]
    At = transpose(A)
    print(A)
    print('is transposed to')
    print(At)