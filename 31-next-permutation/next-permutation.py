class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        def rev(nums, i, j):

            while i<j:
                nums[i] , nums[j] = nums[j] , nums[i]
                i+=1
                j-=1

            


        idx = -1
        n = len(nums)

        for i in range(n-2, -1, -1):

            if nums[i] < nums[i+1]:
                idx=i
                break

        if idx == -1:
            rev(nums, 0, n-1)
            return nums  


        for i in range(n-1, idx, -1):
            if nums[i]>nums[idx]:
                nums[i] , nums[idx] = nums[idx] , nums[i]
                break

        
        rev(nums, idx+1, n-1)
     


        




