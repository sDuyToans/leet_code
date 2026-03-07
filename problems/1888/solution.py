class Solution(object):
    def minFlips(self, s):
        """
        :type s: str
        :rtype: int
        """
        # 111000 -> 2 ways
        # 1: 010101
        # 2: 101010
        n = len(s)
        s = s + s

        alt1 = []
        alt2 = []

        for j in range(len(s)):
            alt1.append('0' if j % 2 == 0 else '1')
            alt2.append('1' if j % 2 == 0 else '0')

        diff1 = 0
        diff2 = 0
        left = 0
        ans = float('inf')

        for right in range(len(s)):
            if s[right] != alt1[right]:
                diff1 += 1
            if s[right] != alt2[right]:
                diff2 += 1

            if right - left + 1 > n:
                if s[left] != alt1[left]:
                    diff1 -= 1
                if s[left] != alt2[left]:
                    diff2 -= 1
                left += 1

            if right - left + 1 == n:
                ans = min(ans, diff1, diff2)

        return ans


s = Solution()
tests = ["111000", "010", "1110", "01001001101"]
expected = [2, 0, 1, 2]

for i in range(len(tests)):
    print("Test", tests[i])
    print("Output:", s.minFlips(tests[i]))
    print("Expected:", expected[i])
    if s.minFlips(tests[i]) == expected[i]:
        print("Passed")
    else:
        print("Failed")
    print()
