class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # O(n)
        # O(1)
        if not nums:
            return 0
        nums = set(nums)
        res = 1

        for num in nums:
            if num - 1 not in nums:
                count = 1
                while num + count in nums:
                    count += 1

                if count > res:
                    res = count

        return res


sol = Solution()
tests = [[100, 4, 200, 1, 3, 2], [0, 3, 7, 2, 5, 8, 4, 6, 0, 1], [1, 0, 1, 2]]

for test in tests:
    print(sol.longestConsecutive(test))
