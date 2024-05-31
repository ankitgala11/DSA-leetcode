class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        ans={}

        for word in strs:

            temp="".join(sorted(word))
            # print(temp)

            if temp in ans:
                ans[temp].append(word)
            else:
                ans[temp]=[word]


        
        return ans.values()