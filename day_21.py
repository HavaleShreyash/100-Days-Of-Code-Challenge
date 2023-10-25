# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        q = 0

        def su(node):
            nonlocal q
            if node is None:
                return
            if node.val % 2 == 0:
                if node.left and node.left.left:
                    q += node.left.left.val
                if node.left and node.left.right:
                    q += node.left.right.val
                if node.right and node.right.right:
                    q += node.right.right.val
                if node.right and node.right.left:
                    q += node.right.left.val
            su(node.left)
            su(node.right)

        su(root)
        return q

# Example usage:
# Construct the binary tree from your example
root = TreeNode(6)
root.left = TreeNode(7)
root.right = TreeNode(8)
root.left.left = TreeNode(2)
root.left.right = TreeNode(7)
root.right.left = TreeNode(1)
root.right.right = TreeNode(3)
root.left.left.left = TreeNode(9)
root.left.right.left = TreeNode(1)
root.left.right.right = TreeNode(4)
root.right.right.right = TreeNode(5)

solution = Solution()
result = solution.sumEvenGrandparent(root)
print(result)  # Output should be 18
