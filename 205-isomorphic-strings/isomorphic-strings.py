class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        mp_s={}
        mp_t={}

        n=len(s)

        for i in range(n):

            if s[i] in mp_s:
                mp_s[s[i]].append(i)
            elif s[i] not in mp_s:
                mp_s[s[i]]= [i]


            if t[i] in mp_t:
                mp_t[t[i]].append(i)
            elif t[i] not in mp_t:
                mp_t[t[i]] = [i]


        return list(mp_s.values()) == list(mp_t.values())
