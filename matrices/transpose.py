"""
transpose a matrix
columns to row
row to columns

a matrix is a list of list
the elements of parent list are rows
the elements of the child list are columns
"""

class matrix_rotate():
    def __init__(self,matrix):
        self.matrix = matrix
        self.nrows = len(matrix)
        self.ncols = len(matrix[0])
        print ("num_rows =", self.nrows)
        print ("num_columns =", self.ncols)
        for i in range(self.nrows):
            print (self.matrix[i])
        print ("------------------------------")

    def transpose(self):
        A = self.matrix
        for i in range(self.nrows):
            for j in range(i, self.ncols):
                A[j][i],A[i][j] = A[i][j],A[j][i]

        for i in range(self.nrows):
            print (self.matrix[i])
        print ("------------------------------")

    def reverse(self):
        for i in range(self.nrows):
            self.matrix[i].reverse()
        for i in range(self.nrows):
            print (self.matrix[i])
        print ("------------------------------")


A = [[1,2,3],[4,5,6],[7,8,9]]
print (len(A))
mr = matrix_rotate(A)
mr.transpose()
mr.reverse()
