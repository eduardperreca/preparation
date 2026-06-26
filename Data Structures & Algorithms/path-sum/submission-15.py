# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        queue = deque()
        if not root:
            return False
        queue = [(root, root.val)]

        while queue:
            el, weigth = queue.pop()
            if el.right == None and el.left == None:
                if weigth == targetSum:
                    return True
            if el.right != None:
                queue.append((el.right, weigth + el.right.val))
            if el.left != None:
                queue.append((el.left, weigth + el.left.val))
        return False