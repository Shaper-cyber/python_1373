class Matrix:

    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        return '\n'.join(' '.join([str(itm) for itm in line]) for line in self.matrix)

 #   len(self.matrix) == len(other.matrix) and
    def __add__(self, other):
        try:
            if  len(self.matrix) == len(other.matrix) and len(self.matrix[0]) == len(other.matrix[0]):
                mat_add = [map(sum, zip(*args)) for args in zip(self.matrix, other.matrix)]
                return Matrix(mat_add)
        except Exception:
            pass



mat1 = [[31, 22],
        [37, 43],
        [51, 86]]
mat2 = [[3, 5, 32],
        [2, 4, 6],
        [-1, 64, -8]]
mat3 = [[3, 5, 8, 3],
        [8, 3, 7, 1]]
mat4 = [[1, 1],
        [1, 1],
        [1, 1]]

a = Matrix(mat1)
b = Matrix(mat2)
c = Matrix(mat3)
d = Matrix(mat4)
print(a)
print(b)
print(c)
print(a+b)