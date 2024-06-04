class Solution:
    def majorityElement(self, nums: List[int]) -> int:

       
        ans=nums[0]
        cnt=1

        for i in range(1 , len(nums)):
            
            if nums[i]==ans:
                cnt+=1
            else:
                cnt-=1

            if cnt==0:
                ans=nums[i]
                cnt=1

        cnt=0

        for i in nums:
            if i==ans:
                cnt+=1

       
        if len(nums)//2 <cnt:return ans
        return -1




        