def add_mat(mat1, mat2, outmat):

    file1 = open(mat1, 'r')
    file2 = open(mat2, 'r')
    
    mat1 = [line.split() for line in file1]
    mat2 = [line.split() for line in file2]
    
    if len(mat1) != len(mat2):
        with open(outmat, 'w') as out:
            out.write('')
        return

    result = []
    for i in range(len(mat1)):
        row = []
        for j in range(len(mat1[i])):
            sum = int(mat1[i][j]) + int(mat2[i][j])
            row.append(sum)
        result.append(row)

    with open(outmat, 'w') as result_file:
        for row in result:
            result_file.write(' '.join(map(str, row)) + '\n')

add_mat('mat1.txt', 'mat2.txt', 'outmat.txt')
add_mat('mat1.txt', 'mat3.txt', 'outmat1.txt')