from typing import List


class Solution:

    def encode(self, strs: List[str]) -> str:
        encode_str = ""

        for s in strs:
            current_len = str(len(s)) + "#"
            encode_str += current_len + s

        return encode_str

    def decode(self, s: str) -> List[str]:
        decode_str = []

        i = 0
        while i < len(s):
            j = i
            # find #
            while s[j] != '#':
                j += 1

            length = int(s[i:j])
            word = s[j + 1:j + length + 1]
            decode_str.append(word)
            i = j + length + 1

        return decode_str


