class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s2t, t2s = {}, {}
        for i in range(len(s)):
            if s[i] in s2t and s2t[s[i]] != t[i]:
                return False
            if t[i] in t2s and t2s[t[i]] != s[i]:
                return False
            s2t[s[i]] = t[i]
            t2s[t[i]] = s[i]
        return True
        # mp_s={}
        # mp_t={}

        # n=len(s)

        # for i in range(n):

        #     if s[i] in mp_s:
        #         mp_s[s[i]].append(i)
        #     elif s[i] not in mp_s:
        #         mp_s[s[i]]= [i]


        #     if t[i] in mp_t:
        #         mp_t[t[i]].append(i)
        #     elif t[i] not in mp_t:
        #         mp_t[t[i]] = [i]


        # return list(mp_s.values()) == list(mp_t.values())
