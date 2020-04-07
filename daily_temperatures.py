# 739. Daily Temperatures


from typing import List


class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        stack = []
        wait = [0] * len(T)

        for i in range(len(T)):
            while len(stack) > 0 and T[stack[-1]] < T[i]:
                j = stack.pop()
                wait[j] = i - j

            stack.append(i)
        return wait
