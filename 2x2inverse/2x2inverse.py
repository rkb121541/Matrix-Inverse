from fractions import Fraction

def decimalinverse2x2(matrix):
    inverseDet = 1/(matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0])
    inverseMatrix = [[matrix[1][1], -matrix[0][1]], [-matrix[1][0], matrix[0][0]]]
    for i in range(2):
        for j in range(2):
            inverseMatrix[i][j] *= inverseDet
    return inverseMatrix
    
def fractionalinverse2x2(matrix):
    det = matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    inverseMatrix = [[matrix[1][1], -matrix[0][1]], [-matrix[1][0], matrix[0][0]]]
    for i in range(2):
        for j in range(2):
            inverseMatrix[i][j] = str(Fraction(inverseMatrix[i][j], det))
    return inverseMatrix

def main():
    # |a b|
    # |c d|
    a = 3
    b = 2
    c = 1
    d = 5
    print(decimalinverse2x2([[a, b], [c, d]]))
    print(fractionalinverse2x2([[a, b], [c, d]]))

if __name__ == "__main__":
    main()