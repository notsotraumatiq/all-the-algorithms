class Solution:
    def romanToInt(self, s: str) -> int:
        h = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }

        result = 0
        for i, num in enumerate(s):
            if i < len(s) - 1 and h[num] < h[s[i + 1]]:
                result -= h[num]
            else:
                result += h[num]
        return result


print(Solution().romanToInt("III"))
print(Solution().romanToInt("IV"))
