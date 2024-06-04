class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        def rev(i, j):
            while i<j:
                nums[i], nums[j] = nums[j], nums[i]
                i+=1
                j-=1

        n=len(nums)-1
        k=k%(n+1)
        rev(0, n-k)
        rev(n-k+1, n)
        rev(0, n)

        

        