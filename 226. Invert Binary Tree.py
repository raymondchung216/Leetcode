# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def swapChildren(self, node):
        rightTemp = None
        leftTemp = None
        if node.right != None:
            rightTemp = node.right
        if node.left != None:
            leftTemp = node.left
        node.right = leftTemp
        node.left = rightTemp
        return


    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # First thought is to createa fuction that swaps its children and call it recursively
        if root is not None:
            self.invertTree(root.left)
            self.invertTree(root.right)
            self.swapChildren(root)
        return root
    
        