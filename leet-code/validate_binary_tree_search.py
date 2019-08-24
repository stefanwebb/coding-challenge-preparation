# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        if root is None:
            return True
        
        stack = [(root, (-float("inf") , float("inf")))]
        
        while len(stack) > 0:
            thisNode, thisInt = stack.pop()
            
            if thisNode.left is not None:
                leftInt = (thisInt[0], thisNode.val)
                if thisNode.left.val <= leftInt[0] or thisNode.left.val >= leftInt[1]:
                    return False
                stack.append((thisNode.left, leftInt))
            
            if thisNode.right is not None:
                rightInt = (thisNode.val, thisInt[1])
                if thisNode.right.val <= rightInt[0] or thisNode.right.val >= rightInt[1]:
                    return False
                stack.append((thisNode.right, rightInt))
                
        return True
