class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        j=0

        for i in range(1, len(nums)):
            if nums[i]==nums[j]:
                continue

            else:
                j+=1
                nums[j]=nums[i]
        print(nums)
        return j+1

        