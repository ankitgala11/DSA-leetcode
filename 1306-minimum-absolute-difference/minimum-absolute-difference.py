class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:

        arr.sort()
        diff=float('inf')


        ans=[]
        n=len(arr)
        j=1


        for i in range(n-1):

            curr = abs(arr[j] - arr[i])

            if curr < diff:
                diff = curr
                ans=[]
                ans.append([arr[i], arr[j]])
            
            elif curr == diff:
                ans.append([arr[i], arr[j]])

            
            j+=1

        return ans





        