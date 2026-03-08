class Solution(object):
    def tribonacci(self, n):
        """
        :type n: int
        :rtype: int
        """
        # tracking 3 variables -> better memory, only need to maintain 3 variables instead of array n + 1
        # O(n)
        if n == 0:
            return 0
        if n == 1:
            return 1
        if n == 2:
            return 1

        t0 = 0
        t1 = 1
        t2 = 1

        for i in range(3, n + 1):
            t0, t1, t2 = t1, t2, t0 + t1 + t2

        return t2

sol = Solution()
tests = [4, 25]
for t in tests:
    print(sol.tribonacci(t))