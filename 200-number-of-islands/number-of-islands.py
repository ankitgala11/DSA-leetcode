class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        n=len(grid)
        m=len(grid[0])

        def bfs(i, j):
            q=[(i, j)]
            grid[i][j]="0"

            while q:

                i, j=q.pop(0)

                x=i+1
                y=j
                if x>=0 and x<n and y>=0 and y<m and grid[x][y]=="1":
                    grid[x][y]="0"
                    q.append((x,y))


                x=i-1
                y=j
                if x>=0 and x<n and y>=0 and y<m and grid[x][y]=="1":
                    grid[x][y]="0"
                    q.append((x,y))

                x=i
                y=j+1
                if x>=0 and x<n and y>=0 and y<m and grid[x][y]=="1":
                    grid[x][y]="0"
                    q.append((x,y))

                x=i
                y=j-1
                if x>=0 and x<n and y>=0 and y<m and grid[x][y]=="1":
                    grid[x][y]="0"
                    q.append((x,y))




        cnt=0
        for i in range(n):
            for j in range(m):

                if grid[i][j] == '1':
                    cnt+=1
                    bfs(i, j)


        return cnt










        # n = len(grid)
        # m = len(grid[0])

        # def dfs(i, j):
        #     grid[i][j] = "0"

        #     x = i
        #     y = j + 1

        #     if x >= 0 and x < n and y >= 0 and y < m and grid[x][y] == "1":
        #         dfs(x, y)

        #     x = i
        #     y = j - 1

        #     if x >= 0 and x < n and y >= 0 and y < m and grid[x][y] == "1":
        #         dfs(x, y)

        #     x = i + 1
        #     y = j

        #     if x >= 0 and x < n and y >= 0 and y < m and grid[x][y] == "1":
        #         dfs(x, y)

        #     x = i - 1
        #     y = j

        #     if x >= 0 and x < n and y >= 0 and y < m and grid[x][y] == "1":
        #         dfs(x, y)

        # cnt = 0
        # for i in range(n):
        #     for j in range(m):

        #         if grid[i][j] == "1":
        #             cnt += 1
        #             dfs(i, j)

        # return cnt
