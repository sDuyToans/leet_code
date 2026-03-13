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

        dp2 = nums[0]  # there is no house before the first one
        dp1 = max(nums[0], nums[1])
        dpi = 0

        for i in range(2, n):
            # there is 2 options for money at index i -> will be the prev2 + current
            # or the prev1 if prev1 > prev2 + current
            dpi = max(dp1, dp2 + nums[i])
            dp2 = dp1
            dp1 = dpi

        return max(dp1, dp2)


s = Solution()
test = [[1, 2, 3, 1], [2, 7, 9, 3, 1]]

for t in test:
    print(s.rob(t))
