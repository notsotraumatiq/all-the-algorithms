class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:


        #  y = target - x
        #  [2, 7, 11 15]

        #  {2: 0, 3: 0}

        h = {}

        for i, num in enumerate(nums):
            y = target - num
            if y not in h:
                h[num] = i
            else:
                return [h[y], i]

        return []


