class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) > len(s):return []
        given = [0] *26
        req = [0] *26
        

        n = len(p)

        for i in range(n):

            given[ ord(p[i]) - ord('a')] += 1


        ans=[]
        for i in range(n):
            req[ ord(s[i]) - ord('a')] += 1

        if req == given:
            ans.append(0)

        
        j=0

        for i in range (n, len(s)):

            req[ ord(s[i]) - ord('a')] += 1

            req[ ord(s[j]) - ord('a')] -= 1


            j+=1
            if req == given:
                ans.append(j)



        return ans



