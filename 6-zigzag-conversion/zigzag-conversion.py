class Solution:
    def convert(self, s: str, numRows: int) -> str:

        if numRows == 1 or numRows>= len(s):
            return s


        idx = 0
        dir = 1


        ans = [[] for i in range(numRows)]

        for ch in s:
            # print(ans, ch)

            ans[idx].append(ch)

            if idx == 0:
                d=1

            elif idx == numRows-1:
                d=-1

            idx += d




        result = ""
            
        for i in ans:
            for j in i:

                result += j




        return result

        