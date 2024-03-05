class Solution:
    def isHappy(self, n: int) -> bool:
        

        s=set()

        while True:
            if n==1:
                return True


            temp=str(n)
            ans=0

            for i in temp:
                ans+=int(i)**2

            
            if ans in s:
                return False
                
            s.add(ans)
            n=ans

