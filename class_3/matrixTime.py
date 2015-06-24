import timeit as t
from numpy import *

def vectorMatrixMultiplication(matrix,vector):
    width = len(matrix[0])
    answer = [0] * width
    for j in range(width):
        for n in range(len(vector)):
            answer[j] += vector[n] * matrix[n][j]

    return answer

def matrixMultiplication(matrix1,matrix2):
    return [vectorMatrixMultiplication(matrix2,matrix1[i]) for i in range(len(matrix1))]

matrix1 = [[1,3,9,2],[2,4,6,8]]
matrix2 = [[2,1],[3,2],[6,0],[5,4]]

npTime = t.timeit('dot(matrix1, matrix2)', setup="from __main__ import dot, matrix1, matrix2", number = 100000)
myTime = t.timeit('matrixMultiplication(matrix1, matrix2)', setup="from __main__ import matrixMultiplication, matrix1, matrix2", number = 100000)

print "numpy takes", (npTime - myTime) / npTime * 100, "percent less time"
