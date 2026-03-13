class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # tabulation
        # O(n)

        n = len(nums)
        if n <= 2:
            return max(nums)

        dp = [0] * n
        dp[0] = nums[0]  # there is no house before the first one
        dp[1] = max(nums[0], nums[1])

        for i in range(2, n):
            # there is 2 options for money at index i -> will be the prev2 + current
            # or the prev1 if prev1 > prev2 + current
            dp[i] = max(dp[i - 1], nums[i] + dp[i - 2])

        return dp[n - 1]


s = Solution()
test = [[1, 2, 3, 1], [2, 7, 9, 3, 1]]

for t in test:
    print(s.rob(t))
