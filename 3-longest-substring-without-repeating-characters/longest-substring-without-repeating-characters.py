class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        mp={}
        longest=0
        start = 0

        for end in range(len(s)):
            ch=s[end]

            mp[ch] = mp.get(ch, 0) + 1
            # print(mp)

            while mp[ch] > 1:

                chs=s[start]

                mp[chs]-=1
                start += 1
                # print(mp)

            # print(start, end)

            longest = max (longest , end - start +1 )

        
        return longest

        