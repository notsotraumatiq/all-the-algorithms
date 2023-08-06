class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        h = set()

        i ,j = 0 , 0
        count = 0
        while j < len(s):
            if s[j] not in h:
                h.add(s[j])
                count = max(count, j - i + 1)
                j += 1
            else:
                h.remove(s[i])
                i += 1

        return count



print(Solution().lengthOfLongestSubstring("abcabcbb"))
