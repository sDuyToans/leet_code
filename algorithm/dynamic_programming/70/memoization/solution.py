# Climbing stair
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        # memoization approach with memorization
        mem = {}

        def recursive(n):
            if n == 1:
                return 1
            if n == 2:
                return 2
            if n in mem:
                return mem[n]
            else:
                step = recursive(n - 1) + recursive(n - 2)
                mem[n] = step
                return step

        return recursive(n)





sol = Solution()
tests = [2, 3]

for test in tests:
    print(sol.climbStairs(test))