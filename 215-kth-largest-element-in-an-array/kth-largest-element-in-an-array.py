import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        


        # nums.sort(reverse=True)

        # if k>len(nums):return False
        # else:return nums[k-1]


        minh=[]
        for i in nums:
            
            heapq.heappush(minh, i)

            if len(minh)>k:
                heapq.heappop(minh)

        return minh[0]

