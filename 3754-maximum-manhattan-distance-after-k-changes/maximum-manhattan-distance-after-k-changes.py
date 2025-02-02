class Solution:
    def maxDistance(self, s: str, k: int) -> int:

        cnt={'N':0,'S':0,'E':0,'W':0}

        final = 0
       


        def solve(cnt, k):
            ans = 0

            maxi_y=max(cnt['N'] , cnt['S'])
            mini_y=min(cnt['N'] , cnt['S'])

            convert = min( mini_y, k)

            # print(maxi_y, mini_y, convert, k)

            maxi_y += convert
            mini_y -= convert
            k -= convert

            ans += maxi_y - mini_y
            # print(maxi_y, mini_y, convert, k, ans)


            maxi_x=max(cnt['E'] , cnt['W'])
            mini_x=min(cnt['E'] , cnt['W'])

            convert = min( mini_x, k)


            # print(maxi_x, mini_x, convert, k)


            maxi_x += convert
            mini_x -= convert
            k -= convert

            ans += maxi_x - mini_x
            # print(maxi_x, mini_x, convert, k, ans)


            return ans

        for i in s:
            if i in cnt:
                cnt[i]+=1

            final = max(final , solve(cnt, k))
    
        
        

    

        
    
        return final



      
        