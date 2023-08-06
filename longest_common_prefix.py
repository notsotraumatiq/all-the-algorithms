class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        result = []

        i,j = 0,0

        strs.sort()
        first = strs[0]
        last = strs[-1]

        while i < len(first) and i < len(last):
            if first[i] != last[i]:
                break
            i += 1

        return "".join(first[0:i])
