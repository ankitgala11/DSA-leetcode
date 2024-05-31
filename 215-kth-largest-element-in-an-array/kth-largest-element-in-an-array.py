class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        


        nums.sort(reverse=True)
         

        if k>len(nums):return False

        else:return nums[k-1]