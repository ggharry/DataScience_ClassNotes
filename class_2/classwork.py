def vectorMatrixMultiplication(matrix,vector):
    width = len(matrix[0])
    answer = [0] * width
    for j in range(width):
        for n in range(len(vector)):
            answer[j] += vector[n] * matrix[n][j]

    return answer

# vector = [1,2,3]
# matrix = [[1,2],[5,6],[9,0]]
# print vectorMatrixMultiplication(matrix,vector)

def matrixMultiplication(matrix1,matrix2):
    return [vectorMatrixMultiplication(matrix2,matrix1[i]) for i in range(len(matrix1))]

# matrix1 = [[1,3,9,2],[2,4,6,8]]
# matrix2 = [[2,1],[3,2],[6,0],[5,4]]
# print matrixMultiplication(matrix1,matrix2)