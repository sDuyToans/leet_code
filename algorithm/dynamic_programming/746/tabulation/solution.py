class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        n = len(cost)
        dp1 = cost[1]
        dp2 = cost[0]
        dpi = 0

        for i in range(2, n):
            dpi = min(dp1, dp2) + cost[i]
            dp2 = dp1
            dp1 = dpi

        return min(dp1, dp2)


s = Solution()
tests = [[10, 15, 20], [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]]

for t in tests:
    print(s.minCostClimbingStairs(t))
