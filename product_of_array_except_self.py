# 238. Product of Array Except Self

from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        array = [1] * len(nums)

        left_sum = 1
        right_sum = 1

        for i in range(len(nums)):
            array[i] *= left_sum
            left_sum *= nums[i]

        for i in reversed(range(len(nums))):
            array[i] *= right_sum
            right_sum *= nums[i]

        return array
