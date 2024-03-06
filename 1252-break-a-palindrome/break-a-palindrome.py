class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        n = len(palindrome)

        if n == 1:
            return ""

        ans=""

        for i in range(n):

            if palindrome[i] != "a":
                if i == n-1:
                    ans = palindrome[:i] + "a"
                
                else:

                    ans = palindrome[:i] + "a" + palindrome[i+1:]
                break

        if ans==ans[::-1]:ans=""
        if not ans:
            ans = palindrome[:-1] + chr(ord(palindrome[-1]) + 1)


        return ans

