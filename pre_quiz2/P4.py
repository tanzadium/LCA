def swoprow(A, i, j):
    result = [row[:] for  row in A]
    result[i], result[j] = result[j], result[i]
    return result

if __name__=="__main__":
    A = [[1,2,3,4], [5,6,7,8], [9,10,11,12], [-1, -2, -3, -4]]
    print(A)
    print('After swop')
    Ap = swoprow(A, 0, 3)
    print('A=', A)
    print("A'=", Ap)