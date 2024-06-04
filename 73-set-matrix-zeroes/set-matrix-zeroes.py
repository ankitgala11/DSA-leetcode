class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        r=len(matrix)
        c=len(matrix[0])

  



        for i in range(r):
            for j in range(c):

                if matrix[i][j]==0:
                    for row in range(r):
                        if row!=i and matrix[row][j]!=0:matrix[row][j]='#'


                    for col in range(c):
                        if col!=j and matrix[i][col]!=0:matrix[i][col]='#'


                    

                
        for i in range(r):
            for j in range(c):

                if matrix[i][j]=="#":
                    matrix[i][j]=0

        return matrix
                    

        
        