# 62. Unique Paths


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        result = [[1 for x in range(n)] for y in range(m)]

        for i in range(1, m):
            for j in range(1, n):
                result[i][j] = result[i - 1][j] + result[i][j - 1]

        return result[-1][-1]
