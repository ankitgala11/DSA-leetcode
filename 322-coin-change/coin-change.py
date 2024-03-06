import sys

sys.setrecursionlimit(10**8)


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        n = len(coins)

        def solve(i, amt):

            if amt == 0:
                return 0

            if i >= n or amt < 0:
                return float("inf")


            if dp[i][amt] != -1:
                return dp[i][amt]



            take = 1 + solve(i, amt - coins[i])

            nottake = solve(i + 1, amt)



            dp[i][amt] = min(take, nottake)
            return dp[i][amt]

        def solveTab():
            dp = [[0] * (amount + 1) for _ in range(n + 1)]

            for i in range(amount + 1):
                dp[n][i] = float("inf")

            for i in range(n - 1, -1, -1):
                for amt in range(1 , amount + 1):
                    
                    take = float("inf")
                    if amt - coins[i] >= 0:
                        take = 1 + dp[i][amt - coins[i]]

                    nottake = dp[i + 1][amt]

                    dp[i][amt] = min(take, nottake)

            return dp[0][amount]

        # dp = [[-1] * (amount + 1) for _ in range(n)]
        # ans = solve(0, amount)

        ans=solveTab()

        if ans == float("inf"):
            return -1
        else:
            return ans


