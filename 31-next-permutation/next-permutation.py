from copy import deepcopy


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.

        # 1 2 6 9 8 7 5 4
        # piche se jao and find pehela aisa number joh aage wale se chota ho
        # agar nahi milla matlab array reverse mein hai toh reverse karke return
        # agar milla toh piche se us number tak mein pehela us number se bada ele nikalo
        # usko uske sath replace
        # then us number se aage ki puri string ko reverse ya sort
        """

        def rev(nums, i, j):

            while i < j:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j -= 1

        n = len(nums)
        idx = -1
        for i in range(n - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                idx = i
                break

        if idx == -1:
            rev(nums, 0, n - 1)
            return

        for i in range(n - 1, idx, -1):
            if nums[i] > nums[idx]:
                nums[i], nums[idx] = nums[idx], nums[i]
                break

        i = idx + 1
        j = n - 1

        rev(nums, i, j)
