from collections import defaultdict

class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:

        adj=defaultdict(list)

        for i in edges:
            adj[i[0]].append(i[1])
            adj[i[1]].append(i[0])

        vis=set()

        def dfs(i):
            vis.add(i)

            for nbr in adj[i]:
                if i not in degree:
                    degree[i] = 1
                else:
                    degree[i] += 1

              
             
                if nbr not in vis:
                    dfs(nbr)
            



        ans=0

        for i in range(n):
            degree={}
            if i not in vis:

                dfs(i) 
                print(degree)
             
           

                temp=len(degree)-1
                flag=False
                for k, v in degree.items():
             
                    if temp!=v:
                        flag=True
                        break
                print(flag)
                if flag==False:
                    ans+=1
           

       
        return ans
                


        