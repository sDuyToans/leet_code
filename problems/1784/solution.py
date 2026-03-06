class Solution(object):
    def checkOnesSegment(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # O(n)
        # n = len(s)

        # counts = []
        # i = 0

        # while i < n:
        #     if s[i] == '0':
        #         i += 1
        #     elif s[i] == '1':
        #         j = i
        #         while j < n and s[j] == '1':
        #             j += 1
        #         counts.append(s[i:j])
        #         i = j

        # return len(counts) == 1

        # if 01 in s that will be wrong
        # O(n)
        n = len(s)

        for i in range(n - 1):
            if s[i] == '0' and s[i + 1] == '1':
                return False

        return True
