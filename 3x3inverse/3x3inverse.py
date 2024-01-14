from fractions import Fraction

def decimalinverse3x3(matrix):
    c11 = matrix[1][1] * matrix[2][2] - matrix[1][2] * matrix[2][1]
    c12 = -(matrix[1][0] * matrix[2][2] - matrix[1][2] * matrix[2][0])
    c13 = matrix[1][0] * matrix[2][1] - matrix[1][1] * matrix[2][0]
    c21 = -(matrix[0][1] * matrix[2][2] - matrix[0][2] * matrix[2][1])
    c22 = matrix[0][0] * matrix[2][2] - matrix[0][2] * matrix[2][0]
    c23 = -(matrix[0][0] * matrix[2][1] - matrix[0][1] * matrix[2][0])
    c31 = matrix[0][1] * matrix[1][2] - matrix[0][2] * matrix[1][1]
    c32 = -(matrix[0][0] * matrix[1][2] - matrix[0][2] * matrix[1][0])
    c33 = matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    ct = [[c11, c21, c31], [c12, c22, c32], [c13, c23, c33]]
    inverseDet = 1/(matrix[0][0] * c11 - matrix[0][1] * c12 + matrix[0][2] * c13)
    inverseMatrix = ct
    for i in range(3):
        for j in range(3):
            inverseMatrix[i][j] *= inverseDet
    return inverseMatrix

def fractionalinverse3x3(matrix):
    c11 = matrix[1][1] * matrix[2][2] - matrix[1][2] * matrix[2][1]
    c12 = -(matrix[1][0] * matrix[2][2] - matrix[1][2] * matrix[2][0])
    c13 = matrix[1][0] * matrix[2][1] - matrix[1][1] * matrix[2][0]
    c21 = -(matrix[0][1] * matrix[2][2] - matrix[0][2] * matrix[2][1])
    c22 = matrix[0][0] * matrix[2][2] - matrix[0][2] * matrix[2][0]
    c23 = -(matrix[0][0] * matrix[2][1] - matrix[0][1] * matrix[2][0])
    c31 = matrix[0][1] * matrix[1][2] - matrix[0][2] * matrix[1][1]
    c32 = -(matrix[0][0] * matrix[1][2] - matrix[0][2] * matrix[1][0])
    c33 = matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    ct = [[c11, c21, c31], [c12, c22, c32], [c13, c23, c33]]
    det = matrix[0][0] * c11 - matrix[0][1] * c12 + matrix[0][2] * c13
    inverseMatrix = ct
    for i in range(3):
        for j in range(3):
            inverseMatrix[i][j] = str(Fraction(inverseMatrix[i][j], det))
    return inverseMatrix

def main():
    # |a b c|
    # |d e f|
    # |h i j|
    a = 2
    b = 0
    c = 1
    d = 1
    e = 1
    f = 2
    h = 0
    i = 2
    j = 1
    print(decimalinverse3x3([[a, b, c], [d, e, f], [h, i, j]]))
    print(fractionalinverse3x3([[a, b, c], [d, e, f], [h, i, j]]))

if __name__ == "__main__":
    main()