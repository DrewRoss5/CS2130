class MatrixRelation:
    def __init__(self, matrix):
        self.matrix = matrix

    def __eq__(self, other):
        if not isinstance(other, MatrixRelation):
            return False
        return self.matrix == other.matrix

    def __str__(self):
        result = '\n'.join(map(str, self.matrix))
        return result

    """
        ***********************************************************************
        * TODO:  Add your code to the methods below
        ***********************************************************************
    """
    def join(self, other):
        # create a copy of the other matrix and 
        result = other
        for row in range(len(self.matrix)):
            for i in range(len(self.matrix[row])):
                if self.matrix[row][i] == 1:
                    result.matrix[row][i] = 1
        return other

    def transpose(self):
        # switch the places of rows and columns in a new matrix
        result = []
        size = len(self.matrix)
        for x in range(size):
            row = []
            for y in range(size):
                row.append(self.matrix[y][x])
            result.append(row)  
        return MatrixRelation(result)

    def reflexive_closure(self):
        # create a reflexive version of this matrix
        result = []
        size = len(self.matrix)
        for y in range(size):
            row = []
            for x in range(size):
                if x == y:
                    row.append(1)
                else:
                    row.append(self.matrix[y][x])
            result.append(row)
        return MatrixRelation(result)

    def symmetric_closure(self):
        # create a symetric version of this matrix
        # create a deep copy of the matrix
        result = []
        size = len(self.matrix)
        for y in range(size):
            row = []
            for x in range(size):
                row.append(self.matrix[x][y])
            result.append(row)
        # make the matrix symmetric
        for y in range(size):
            for x in range(size):
                if result[x][y] == 1:
                    result[y][x] = 1
        return MatrixRelation(result)


    def in_degree(self, vertex):
        in_degree = 0
        size = len(self.matrix)
        for i in range(size):
            if self.matrix[i][vertex] == 1:
                in_degree += 1
        return in_degree


    def out_degree(self, vertex):
        out_degree = 0 
        for i in self.matrix[vertex]:
            if i == 1:
                out_degree += 1
        return out_degree
        

    def is_rooted_tree(self):
        # determine if the matrix is a rooted tree (i.e one element has an in-degree of zero and all others have an in degree of one)
        zero_count = 0
        size = len(self.matrix)
        for i in range(size):
            in_degree = self.in_degree(i)
            if in_degree != 1 and in_degree != 0:
                print(f'In degree of {i} is {in_degree}')
                return False
            elif in_degree == 0:
                zero_count += 1
        return zero_count == 1
