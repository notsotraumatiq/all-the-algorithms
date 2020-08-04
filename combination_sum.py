class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        result = []
        # sort not necessary
        candidates.sort()
        self.backtrack(result, [], candidates, target, 0)
        return result

    def backtrack(self, result, temp, candidates, target, index):
        if target < 0:
            return
        elif target == 0:
            result.append(temp[:])

        else:
            for j in range(index, len(candidates)):
                temp.append(candidates[j])
                self.backtrack(result, temp, candidates,
                               target - candidates[j], j)
                temp.pop()
