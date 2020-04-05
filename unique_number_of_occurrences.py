# 1207. Unique Number of Occurrences

from typing import List


class Solution:
    def uniqueOccurrences(self, nums: List[int]) -> bool:
        hash_table = {}

        for i in range(len(nums)):
            if nums[i] not in hash_table:
                hash_table[nums[i]] = 1
            hash_table[nums[i]] += 1
        result = []
        for value in hash_table.values():
            result.append(value)
        if len(result) != len(set(result)):
            return False
        return True
