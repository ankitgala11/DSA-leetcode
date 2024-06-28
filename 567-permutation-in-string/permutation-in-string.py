class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        g=[0]*26
        r=[0]*26
 
        n=len(s1)
        if n>len(s2):return False

        for i in s1:
            g[ ord(i) - ord('a')] += 1

        for i in range(n):
            r[ord(s2[i]) - ord('a')] += 1

        if g == r:
            return True

        j=0
        for i in range(n, len(s2)):
            r[ord(s2[i]) - ord('a')] += 1
            r[ord(s2[j]) - ord('a')] -= 1

            j+=1

            if g == r:
                return True

        return False




        