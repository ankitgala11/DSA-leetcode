import copy

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        def isValid(i, j):

            if i>=0 and i<r and j>=0 and j<c:
                return True
            return False
            

        def bfs(temp, q):
            ans = 0
            while q:
                i, j, time = q.pop(0)
                ans=max(ans, time)


                if isValid(i+1, j) and temp[i+1][j] == 1:
                    temp[i+1][j] = 2
                    q.append((i+1, j, time+1))

                if isValid(i-1, j) and temp[i-1][j] == 1:
                    temp[i-1][j] = 2
                    q.append((i-1, j, time+1))

                if isValid(i, j+1) and temp[i][j+1] == 1:
                    temp[i][j+1] = 2
                    q.append((i, j+1, time+1))

                if isValid(i, j-1) and temp[i][j-1] == 1:
                    temp[i][j-1] = 2
                    q.append((i, j-1, time+1))


            return ans








        temp=copy.deepcopy(grid)
        q=[]

        r=len(temp)
        c=len(temp[0])


        for i in range(r):
            for j in range(c):

                if temp[i][j] == 2:

                    q.append((i, j, 0))


        ans = bfs(temp, q)

        for i in range(r):
            for j in range(c):

                if temp[i][j] == 1:

                    return -1

        return ans




        