class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        profit = 0
        n = len(prices)

        for i in range(1, n):
            if prices[i] > prices[i-1]:
                profit += prices[i] - prices[i-1]

        return profit


sol = Solution()

tests = [
    [7, 1, 5, 3, 6, 4],
    [7, 6, 4, 3, 1],
    [1, 2, 3, 4, 5]
]

for t in tests:
    print("Input:", t)
    print("Output:", sol.maxProfit(t))
    print()
