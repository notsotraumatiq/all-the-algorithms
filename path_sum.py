# 112. Path Sum

from typing import List


# Definition for a binary tree node.

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        return self.maxself(root, sum)

    def maxself(self, root, summer):
        if not root:
            return False
        if not root.left and not root.right and root.val == summer:
            return True

        summer -= root.val

        self.maxself(root.left, summer)
        self.maxself(root.right, summer)
